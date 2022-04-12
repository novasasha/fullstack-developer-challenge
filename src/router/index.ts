import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'instructions',
    component: () => import('@/pages/HomeInstructions.vue'),
  },
  {
    path: '/exercise-1',
    name: 'exercise-1',
    component: () => import('@/pages/Exercise-1.vue'),
  },
  {
    path: '/exercise-2',
    name: 'exercise-2',
    component: () => import('@/pages/Exercise-2.vue'),
    redirect: { name: 'page-1' },
    children: [
      {
        path: 'page-1',
        name: 'page-1',
        component: () => import('@/components/Exercise-2/Page-1.vue'),
      },
      {
        path: 'page-2',
        name: 'page-2',
        component: () => import('@/components/Exercise-2/Page-2.vue'),
      },
    ],
  },
  {
    path: '/exercise-3',
    name: 'exercise-3',
    component: () => import('@/pages/Exercise-3.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
