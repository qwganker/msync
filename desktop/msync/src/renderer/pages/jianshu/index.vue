<template>
  <div>
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
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>