<template>
  <a-layout id="components-layout-demo-fixed-sider">
    <a-layout-sider
      :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }"
    >
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="inline"
        :default-selected-keys="['jianshu']"
      >
        <a-menu-item key="jianshu">
          <router-link to="/jianshu" />
          简书
        </a-menu-item>
        <a-menu-item key="csdn">
          <router-link to="/csdn" />
          csdn
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout :style="{ marginLeft: '200px', height: '100%' }">
      <router-view></router-view>
    </a-layout>
  </a-layout>
</template>

<script>

export default {

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