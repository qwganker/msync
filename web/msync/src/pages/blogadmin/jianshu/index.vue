<template>
  <div style="height: 100%;">
    <a-col style="height: 100%;" :span="2">
      <a-menu @click="onSelectCate" mode="inline" style="height: 100%;">
        <a-menu-item v-for="cate in cateList" :key="cate.id">{{
          cate.name
        }}</a-menu-item>
      </a-menu>
    </a-col>
    <a-col style="height: 100%;" :span="4">
      <a-menu @click="onSelectBlog" mode="inline" style="height: 100%;">
        <a-menu-item v-for="blog in blogList" :key="blog.id">{{
          blog.title
        }}</a-menu-item>
      </a-menu>
    </a-col>
    <a-col :span="18">
      <div style="padding:10px">
        <a-button
          type="primary"
          @click="onPublishUpdate()"
          style="margin-right:10px"
          >发布更新</a-button
        >
        <a-popconfirm
          placement="bottom"
          ok-text="是"
          cancel-text="否"
          @confirm="onDelete"
        >
          <template slot="title">
            确认删除
          </template>
          <a-button type="danger">删除</a-button>
        </a-popconfirm>
      </div>
      <div style="padding: 10px; width: 50%;">
        <a-input v-model="mdText.title"></a-input>
      </div>
      <mavon-editor
        style="z-index:1"
        :toolbars="markdownOption"
        v-model="mdText.content"
      />
    </a-col>
  </div>
</template>
<script>
import * as API from "@/apis/blog.js";

export default {
  components: {},
  data() {
    return {
      currentSelectedBlogId: "",
      currentSelectedCateId: "",
      cateList: [],
      blogList: [],
      mdText: {
        title: "",
        content: ""
      },
      markdownOption: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: false, // 全屏编辑
        readmodel: false, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: true, // 帮助
        // /* 1.3.5 */
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        // save: true, // 保存（触发events中的save事件）
        // /* 1.4.2 */
        navigation: true, // 导航目录
        // /* 2.1.8 */
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true // 预览,
      }
    };
  },

  mounted() {
    this.fetchBlogCateList();
  },

  methods: {
    findBlog(id) {
      for (let i = 0; i < this.blogList.length; i++) {
        const e = this.blogList[i];
        if (e.id === id) {
          return e;
        }
      }
    },
    onSelectBlog(e) {
      let blog = this.findBlog(e.key);

      this.currentSelectedBlogId = blog.id;
      this.mdText.title = blog.title;

      API.fetchContent({
        siteType: "jianshu",
        id: e.key
      }).then(resp => {
        this.mdText.content = JSON.parse(resp.data).content;
      });
    },
    onSelectCate(e) {
      this.mdText.title = "";
      this.mdText.content = "";
      this.currentSelectedCateId = e.key;
      API.fetchBlogList({
        siteType: "jianshu",
        id: e.key
      }).then(resp => {
        this.blogList = JSON.parse(resp.data);
      });
    },
    onSelectSite(e) {
      this.fetchBlogCateList(e.key);
    },
    fetchBlogCateList() {
      API.fetchBlogCategoryList({ siteType: "jianshu" }).then(resp => {
        this.cateList = JSON.parse(resp.data);
      });
    },
    onPublishUpdate() {
      let blog = this.findBlog(this.currentSelectedBlogId)
      
      API.publishUpdate({
        id: this.currentSelectedBlogId,
        siteType: "jianshu",
        title: this.mdText.title,
        content: this.mdText.content,
        cateId: this.currentSelectedCateId,
        autosave_control: blog.autosave_control
      });
    },
    onDelete() {
      API.deleteBlog({
        siteType: "jianshu",
        id: this.currentSelectedBlogId
      });
      this.onSelectCate({ key: this.currentSelectedCateId });
    },
    onNewBlog() {
      this.mdText.title = "";
      this.mdText.content = "";
    }
  }
};
</script>

<style>
</style>