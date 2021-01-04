<template>
  <a-layout id="components-layout-demo-fixed-sider">
    <a-layout-sider
      :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }"
    >
      <a-menu
        @click="onSelectSite"
        theme="dark"
        mode="inline"
        :default-selected-keys="['4']"
      >
        <a-menu-item key="jianshu">简书</a-menu-item>
        <a-menu-item key="csdn">csdn</a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout :style="{ marginLeft: '200px' }">
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
          <mavon-editor
            style="z-index:1"
            :toolbars="markdownOption"
            v-model="mdText"
          />
        </a-col>
      </div>
    </a-layout>
  </a-layout>
</template>

<script>
import * as API from "@/apis/blog.js";

export default {
  components: {},
  data() {
    return {
      currentSiteType: "",
      cateList: [],
      blogList: [],
      mdText: "",
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

  methods: {
    onSelectBlog(e) {
      API.fetchBlogContent({ siteType: this.currentSiteType, id: e.key }).then(
        resp => {
          this.mdText = JSON.parse(resp.data).content
        }
      );
    },
    onSelectCate(e) {
      API.fetchBlogList({ siteType: this.currentSiteType, id: e.key }).then(
        resp => {
          this.blogList = JSON.parse(resp.data);
          console.log(this.blogList)
        }
      );
    },
    onSelectSite(e) {
      this.fetchBlogCate(e.key);
    },
    fetchBlogCate(type) {
      this.currentSiteType = type;
      switch (type) {
        case "jianshu":
          API.fetchBlogCate({ siteType: "jianshu" }).then(resp => {
            this.cateList = JSON.parse(resp.data);
          });
          break;
        case "csdn":
          break;
        default:
          alert("错误的类型");
      }
    },

    onPublish(type) {
      switch (type) {
        case "jianshu":
          API.publishBlog({ siteType: "jianshu", text: this.mdText });
          break;
        case "csdn":
          break;
        default:
          alert("错误的类型");
      }
    }
  }
};
</script>
<style scoped>
#components-layout-demo-fixed-sider .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

.ant-layout.ant-layout-has-sider {
  flex-direction: row;
  height: 100%;
}
</style>