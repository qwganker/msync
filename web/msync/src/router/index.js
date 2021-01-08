import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/index'),
    redirect: '/blogadmin',
    children: [
      {
        path: '/blogadmin',
        component: () => import('@/pages/blogadmin'),
        children: [
          {
            path: '/blogadmin/jianshu',
            component: () => import('@/pages/blogadmin/jianshu')
          },
          {
            path: '/blogadmin/csdn',
            component: () => import('@/pages/blogadmin/csdn')
          },
          {
            path: '/blogadmin/toutiao',
            component: () => import('@/pages/blogadmin/toutiao')
          },
          {
            path: '/blogadmin/oschina',
            component: () => import('@/pages/blogadmin/oschina')
          }
        ]
      },
      {
        path: '/writeadmin',
        component: () => import('@/pages/writeadmin')
      }
    ]
  }
]

const router = new Router({
  routes
});

export default router;
