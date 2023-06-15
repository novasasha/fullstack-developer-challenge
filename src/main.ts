import { plugin as PrefectDesign } from '@prefecthq/prefect-design'
import { createPinia } from 'pinia'
import { createApp } from 'vue'
import router from '@/router'

import '@prefecthq/prefect-design/dist/style.css'

// eslint-disable-next-line import/order
import App from '@/App.vue'

const pinia = createPinia()


const app = createApp(App)
  .use(PrefectDesign)
  .use(router)
  .use(pinia)

app.mount('#app')
