import Vue from 'vue'
import axios from 'axios'

import App from './App'
import router from './router'
// import store from './store'
import mavonEditor from 'mavon-editor'

import Antd from 'ant-design-vue';
import 'mavon-editor/dist/css/index.css'
import 'ant-design-vue/dist/antd.css';

Vue.use(Antd);

Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

Vue.use(mavonEditor)

/* eslint-disable no-new */

new Vue({
  // store,
  router,
  render: h => h(App)
}).$mount('#app')
