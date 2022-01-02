import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SearchByDates from '../views/SearchByDates'
import SearchByCountry from '../views/SearchByCountry'
import LatestEarthquakes from '../views/LatestEarthquakes'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search-by-dates',
    name: 'SearchByDates',
    component: SearchByDates
  },
  {
    path: '/search-by-country',
    name: 'SearchByCountry',
    component: SearchByCountry
  },
  {
    path: '/latest',
    name: 'LatestEarthquakes',
    component: LatestEarthquakes
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
