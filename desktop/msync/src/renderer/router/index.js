import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/index'),
    redirect: '/jianshu',
    children: [
      {
        path: '/jianshu',
        component: () => import('@/pages/jianshu')
      },
      {
        path: '/csdn',
        component: () => import('@/pages/csdn')
      }
    ]
  }
]

const router = new Router({
  routes
});

export default router;
