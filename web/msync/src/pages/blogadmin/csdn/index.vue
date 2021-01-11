<template>
  <div style="height: 100%;">
    <a-col style="height: 100%;" :span="2">
      <a-menu @click="onSelectCate" mode="inline" style="height: 100%;">
        <a-menu-item v-for="cate in cateList.list.column" :key="cate.id">{{
          cate.title
        }}</a-menu-item>
      </a-menu>
    </a-col>
    <a-col style="height: 100%;" :span="4">
      <a-menu @click="onSelectBlog" mode="inline" style="height: 100%;">
        <a-menu-item
          v-for="blog in blogList.category_article_list_unTop"
          :key="blog.id"
          >{{ blog.title }}</a-menu-item
        >
      </a-menu>
    </a-col>
    <a-col :span="18">
      <div style="padding:10px">
        <a-button type="primary" @click="onPublishUpdate">发布更新</a-button>
        <a-button type="danger" @click="onDelete">删除</a-button>
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
import showdown from 'showdown'
export default {
  components: {},
  data() {
    return {
      currentSelectedBlogId: "",
      currentSelectedCateId: "",
      cateList: {
        list: {
          column: []
        }
      },
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
      for (let i = 0; i < this.blogList.category_article_list_unTop.length; i++) {
        const e = this.blogList.category_article_list_unTop[i];
        if (e.id === id) {
          return e;
        }
      }
    },
    findCate(id) {
      for (let i = 0; i < this.cateList.list.column.length; i++) {
        const e = this.cateList.list.column[i];
        if (e.id === id) {
          return e;
        }
      }
    },

    onPublishUpdate() {
      var converter = new showdown.Converter()
      let blog = this.findBlog(this.currentSelectedBlogId);
      API.publishUpdate({
        siteType: "csdn",
        data: {
          id: blog.article_url.substr(blog.article_url.lastIndexOf('/') + 1),
          title: this.mdText.title,
          markdowncontent: this.mdText.content,
          content: converter.makeHtml(this.mdText.content),
          readType: "public",
          tags: "",
          status: 0,
          categories: this.findCate(this.currentSelectedCateId).title,
          original_link: "",
          authorized_status: "",
          Description: this.mdText.content,
          resource_url: "",
          not_auto_saved: "",
          source: "pc_mdeditor",
          type: "original"
        }
      }).then();
    },
    onSelectBlog(e) {
      let blog = this.findBlog(e.key);

      this.currentSelectedBlogId = blog.id;
      this.mdText.title = blog.title;

      let id = blog.article_url.substr(blog.article_url.lastIndexOf('/') + 1)

      API.fetchContent({
        siteType: "csdn",
        id: id
      }).then(resp => {
        this.mdText.content = JSON.parse(resp.data).data.markdowncontent;
      });
    },
    onSelectCate(e) {
      this.mdText.title = ""
      this.mdText.content = ""
      this.currentSelectedCateId = e.key;
      API.fetchBlogList({
        siteType: "csdn",
        id: e.key
      }).then(resp => {
        this.blogList = resp.data;
      });
    },
    onSelectSite(e) {
      this.fetchBlogCateList(e.key);
    },
    fetchBlogCateList(type) {
      API.fetchBlogCategoryList({ siteType: "csdn" }).then(resp => {
        this.cateList = resp.data;
      });
    },
    onPublish() {
      API.publishUpdate({
        siteType: "csdn",
        id: this.currentSelectedBlogId
      });
    },
    onDelete() {
      API.deleteBlog({
        siteType: "csdn",
        id: this.currentSelectedBlogId
      });

      this.onSelectCate({ key: this.currentSelectedCateId });
    }
  }
};
</script>

<style>
</style>