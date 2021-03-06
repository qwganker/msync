import axios from 'axios';
import qs from 'qs';
import NProgress from 'nprogress';
// import store from '@/store';
import 'nprogress/nprogress.css';
import { notification } from 'ant-design-vue';

// import { RESPONSE_STATUS, STORAGE_KEY } from '@/assets/js/constants';
// import router from '@/router';
notification.config({
  placement: 'topRight',
  duration: 1.5
});

NProgress.configure({
  showSpinner: false
});

function requestInterceptor(config) {
  NProgress.start();
  // const token = store.state['LoginService'].tokenInfo.accessToken;
  // if (token) {
  //   config.headers['Authorization'] = `Bearer ${token}`;
  // }
  return config;
}

function requestErrorInterceptor() {
  NProgress.done();
  return Promise.reject(new Error('请求错误'));
}

function responseInterceptor(response) {
  NProgress.done();
  if (response.data.code === 200) {
    notification.success({ message: "成功", description: response.data.info });
    return response.data;
  } else {
    notification.error({ message: "错误", description: response.data.info });
    return Promise.reject(new Error('请求错误'));
  }
}

function responseErrorInterceptor(error) {
  NProgress.done();
  if (error.code === 'ECONNABORTED' && error.message.includes('timeout')) {
    notification.error({ message: "错误", description: '请求超时' });
  } else {
    notification.error({ message: "错误", description: '系统异常' });
  }
  return Promise.reject(error);
}
function genNetwork(instance) {
  return {
    get(url, params, config = {}) {
      return instance.get(url, { params, ...config });
    },
    getNoCache(url, params = {}) {
      const noCacheHeader = {
        'If-Modified-Since': '0'
      };
      return instance.get(url, { params, headers: noCacheHeader });
    },
    post(url, params, config = {}) {
      return instance.post(url, params, config);
    },
    put(url, data, config) {
      return instance.put(url, data, config);
    },
    delete(url, data, config = {}) {
      return instance.delete(url, { data, ...config });
    },
    form(url, params, config = {}) {
      return instance.post(url, qs.stringify(params), config);
    },
    file(url, params = {}, config = {}) {
      const formData = new FormData();
      Object.entries(params).forEach(([k, v]) => {
        if (Array.isArray(v)) {
          v.forEach(item => {
            formData.append(k, item);
          });
        } else {
          formData.append(k, v);
        }
      });
      const headers = { 'Content-Type': 'multipart/form-data' };
      return instance.post(url, formData, { headers, ...config });
    }
  };
}

const instance = axios.create({
  // baseURL: process.env.VUE_APP_BASE_URL,
  baseURL: process.env.NODE_ENV === 'development' ? '' : 'http://127.0.0.1:8000/',
  timeout: 1000 * 60 * 20,
  headers: {
    'X-Frame-Options': 'SAMEORIGIN'
  }
});

instance.interceptors.request.use(requestInterceptor, requestErrorInterceptor);

instance.interceptors.response.use(responseInterceptor, responseErrorInterceptor);

export default genNetwork(instance);
