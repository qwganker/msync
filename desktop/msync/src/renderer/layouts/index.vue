<template>
  <a-layout id="components-layout-demo-fixed-sider">
    <a-layout-sider
      :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }"
    >
      <div class="logo" />
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
          <div style="padding:10px">
            <a-button type="primary" @click="onSave">保存</a-button>
            <a-button @click="onPublish">发布</a-button>
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
    </a-layout>
  </a-layout>
</template>

<script>
import * as API from "@/apis/blog.js";

export default {
  components: {},
  data() {
    return {
      currentSelectedSiteType: "",
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

  methods: {
    findBlog(id) {
      for (let i = 0; i < this.blogList.length; i++) {
        const e = this.blogList[i];
        if (e.id === id) {
          return e
        }
      }
    },
    onSave() {
      let blog = this.findBlog(this.currentSelectedBlogId)
      // 简书
      API.updateBlogContent({ siteType: this.currentSelectedSiteType, id: blog.id, title: this.mdText.title, autosave_control: ++blog.autosave_control, text: this.mdText.content }).then();
    },
    onSelectBlog(e) {
      let blog = this.findBlog(e.key)

      this.currentSelectedBlogId = blog.id
      this.mdText.title = blog.title

      API.fetchBlogContent({ siteType: this.currentSelectedSiteType, id: e.key }).then(
        resp => {
          this.mdText.content = JSON.parse(resp.data).content
        }
      );
    },
    onSelectCate(e) {
      this.currentSelectedCateId = e.key
      API.fetchBlogList({ siteType: this.currentSelectedSiteType, id: e.key }).then(
        resp => {
          this.blogList = JSON.parse(resp.data);
        }
      );
    },
    onSelectSite(e) {
      this.fetchBlogCate(e.key);
    },
    fetchBlogCate(type) {
      this.currentSelectedSiteType = type;
      switch (type) {
        case "jianshu":
          API.fetchBlogCate({ siteType: "jianshu" }).then(resp => {
            this.cateList = JSON.parse(resp.data);
          });
          break;
        case "csdn":
          API.fetchBlogCate({ siteType: "csdn" }).then(resp => {
            this.cateList = JSON.parse(resp.data);
          });
          break;
        default:
          alert("错误的类型");
      }
    },
    onPublish() {
      switch (this.currentSelectedSiteType) {
        case "jianshu":
          API.publishBlog({ siteType: "jianshu", id: this.currentSelectedBlogId });
          break;
        case "csdn":
          break;
        default:
          alert("错误的类型");
      }
    },
    onDelete() {
      switch (this.currentSelectedSiteType) {
        case "jianshu":
          API.deleteBlog({ siteType: "jianshu", id: this.currentSelectedBlogId });
          break;
        case "csdn":
          break;
        default:
          alert("错误的类型");
      }

      this.onSelectCate({key: this.currentSelectedCateId})
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

#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

</style>