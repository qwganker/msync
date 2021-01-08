<template>
  <a-layout style="height: 100%;">
    <a-layout-sider :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }">
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="inline"
        :default-selected-keys="['writeadmin']"
        :default-open-keys="['blogadmin', 'writeadmin']"
      >
        <a-menu-item key="writeadmin">
          <router-link to="/writeadmin" />
          <a-icon type="highlight" /><span>创作中心</span>
        </a-menu-item>
        <a-sub-menu key="blogadmin">
          <span slot="title"
            ><a-icon type="database" /><span>文章管理</span></span
          >
          <a-menu-item key="jianshu">
            <router-link to="/blogadmin/jianshu" />
            简书
          </a-menu-item>
          <a-menu-item key="csdn">
            <router-link to="/blogadmin/csdn" />
            CSDN
          </a-menu-item>
          <a-menu-item key="toutiao">
            <router-link to="/blogadmin/toutiao" />
            头条
          </a-menu-item>
          <a-menu-item key="oschina">
            <router-link to="/blogadmin/oschina" />
            开源中国
          </a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout :style="{ marginLeft: '200px' }">
      <router-view></router-view>
    </a-layout>
  </a-layout>
</template>

<script>
export default {};
</script>
<style scoped>
.logo {
  height: 32px;
  background-image: url(../assets/images/icon.svg);
  background-repeat: no-repeat;
  background-size: 100% 100%;
  -moz-background-size: 50% 50%;
  margin: 16px;
  background-color: black;
}
</style>