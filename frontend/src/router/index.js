import Vue from 'vue'
import VueRouter from 'vue-router'
import PlayerStatsPage from '@/views/PlayerStatsPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'PlayerStats',
    component: PlayerStatsPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
