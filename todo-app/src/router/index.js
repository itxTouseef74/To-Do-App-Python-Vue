import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from '../views/Login.vue'


const guard = function (to, from, next) {
  console.log('Token:', localStorage.getItem('token'));
  if (localStorage.getItem('token')) {
    next();
  } else {
    next('/login');
  }
};
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      beforeEnter:(to ,from , next)=>{
        guard(to , from , next)
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
 ]
})

export default router
