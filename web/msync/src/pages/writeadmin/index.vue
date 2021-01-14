<template>
  <div>
    <a-card :hoverable="true">
      <a-form-model
        ref="ruleForm"
        :model="form"
        :rules="rules"
        :label-col="labelCol"
        :wrapper-col="wrapperCol"
      >
        <a-form-model-item ref="title" label="标题" prop="title">
          <a-input
            v-model="form.title"
            @blur="
              () => {
                $refs.title.onFieldBlur();
              }
            "
          />
        </a-form-model-item>
        <a-form-model-item label="内容" prop="content">
          <mavon-editor
            style="z-index:1"
            :toolbars="markdownOption"
            v-model="form.content"
          />
        </a-form-model-item>
        <a-form-model-item ref="cate" label="分类" prop="cate">
          <a-input v-model="form.cate" />
        </a-form-model-item>
        <a-form-model-item label="站点" prop="sites">
          <a-checkbox-group v-model="form.sites">
            <a-checkbox value="csdn" name="csdn">
              csdn
            </a-checkbox>
            <a-checkbox value="jianshu" name="jianshu">
              简书
            </a-checkbox>
            <a-checkbox value="toutiao" name="toutiao">
              头条
            </a-checkbox>
          </a-checkbox-group>
        </a-form-model-item>
        <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
          <a-button type="primary" @click="onPublish">
            发布
          </a-button>
          <a-button style="margin-left: 10px;" @click="resetForm">
            重置
          </a-button>
        </a-form-model-item>
      </a-form-model>
    </a-card>
  </div>
</template>

<script>
import * as API from "@/apis/blog.js";

export default {
  data() {
    return {
      labelCol: { span: 2 },
      wrapperCol: { span: 18 },
      other: "",
      form: {
        title: "",
        content: "",
        cate: "",
        sites: []
      },
      rules: {
        title: [{ required: true, message: "请填写标题", trigger: "blur" }],
        content: [{ required: true, message: "请填写内容", trigger: "blur" }],
        sites: [
          {
            type: "array",
            required: true,
            message: "请选择发布的网站",
            trigger: "change"
          }
        ]
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
    async onPublish() {
      await this.$refs.ruleForm.validate(async valid => {
        if (!valid) {
          return false;
        }

        for (let i in this.form.sites) {
          await API.publishNew({
            siteType: this.form.sites[i],
            title: this.form.title,
            cate: this.form.cate,
            content: this.form.content
          }).then();
        }
      });
    },
    resetForm() {
      this.$refs.ruleForm.resetFields();
    }
  }
};
</script>

<style>
</style>