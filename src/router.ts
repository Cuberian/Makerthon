import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import App from './views/App.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/',
      name: 'App',
      component: App
    },
    {
      path: '/About',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
