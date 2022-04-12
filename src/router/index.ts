import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Instructions',
    component: () => import(/* webpackChunkName: "instructions" */ '@/pages/Instructions.vue'),
  },
  // {
  //   path: '/exercise-1',
  //   name: 'Exercise 1',
  //   component: () => import(/* webpackChunkName: "exercise-1" */ '@/pages/Exercise-1.vue'),
  // },
  // {
  //   path: '/exercise-2',
  //   name: 'Exercise 2',
  //   component: () => import(/* webpackChunkName: "exercise-2" */ '@/pages/Exercise-2.vue'),
  //   redirect: { name: 'page-1' },
  //   children: [
  //     {
  //       path: 'page-1',
  //       name: 'page-1',
  //       component: () => import(
  //         /* webpackChunkName: "exercise-2-page-1" */ '@/components/Exercise-2/Page-1.vue'
  //       ),
  //     },
  //     {
  //       path: 'page-2',
  //       name: 'page-2',
  //       component: () => import(
  //         /* webpackChunkName: "exercise-2-page-2" */ '@/components/Exercise-2/Page-2.vue'
  //       ),
  //     },
  //   ],
  // },
  // {
  //   path: '/exercise-3',
  //   name: 'Exercise 3',
  //   component: () => import(/* webpackChunkName: "exercise-3" */ '@/pages/Exercise-3.vue'),
  // },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
