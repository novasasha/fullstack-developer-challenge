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
