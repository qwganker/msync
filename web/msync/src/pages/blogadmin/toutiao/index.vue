<template>
  <div style="height: 100%;">
    <a-col style="height: 100%;" :span="4">
      <a-menu @click="onSelectBlog" mode="inline" style="height: 100%;">
        <a-menu-item v-for="blog in blogList" :key="blog.article_attr.gid">{{
          blog.article_attr.rich_title
        }}</a-menu-item>
      </a-menu>
    </a-col>
    <a-col :span="20">
      <div style="padding:10px">
        <a-button
          type="primary"
          style="margin-right:10px"
          @click="onPublishUpdate"
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
      siteType: "toutiao",
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
    this.fetchAllBlog();
  },

  methods: {
    fetchAllBlog() {
      API.fetchBlogList({
        siteType: this.siteType
      }).then(resp => {
        this.blogList = JSON.parse(resp.data).contents;
        console.log(JSON.stringify(this.blogList))

        for (let i in this.blogList) {
          console.log(JSON.stringify(this.blogList[i].article_attr))
          console.log("-----------------------------------------")
          // console.log(JSON.stringify(this.blogList[i]))
        }

      });
    },
    findBlog(id) {
      for (let i = 0; i < this.blogList.length; i++) {
        const e = this.blogList[i];
        if (e.article_attr.gid === id) {
          return e;
        }
      }
    },
    onPublishUpdate() {
      let blog = this.findBlog(this.currentSelectedBlogId);
      API.publishUpdate({
        siteType: this.siteType,
        id: blog.article_attr.gid,
        title: this.mdText.title,
        content: this.mdText.content
      }).then();
    },
    onSelectBlog(e) {
      let blog = this.findBlog(e.key);
      this.currentSelectedBlogId = e.key;

      this.mdText.title = blog.article_attr.rich_title;

      API.fetchContent({
        siteType: this.siteType,
        id: e.key
      }).then(resp => {
        this.mdText.content = JSON.parse(resp.data).content;
      });
    },
    onDelete() {
      API.deleteBlog({
        siteType: this.siteType,
        blog: this.findBlog(this.currentSelectedBlogId)
      });
      // this.fetchAllBlog()
    }

  }
};
</script>

<style>
</style>