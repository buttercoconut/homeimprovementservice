import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QuoteRequestView from '../views/QuoteRequestView.vue'

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/quote', name: 'QuoteRequest', component: QuoteRequestView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
