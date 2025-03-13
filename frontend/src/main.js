import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import '@mdi/font/css/materialdesignicons.css' // Ensure MDI icons load

const vuetify = createVuetify({
  icons: {
    defaultSet: 'mdi', // Explicitly set MDI as the icon set
  },
})

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
