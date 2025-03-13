import { createRouter, createWebHistory } from 'vue-router'
import UserList from './views/UserList.vue'
import UserDetail from './views/UserDetail.vue'

const routes = [
  { path: '/', name: 'Home', component: UserList },
  { path: '/users/:id', name: 'UserDetail', component: UserDetail }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
