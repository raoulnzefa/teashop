import { createRouter, createWebHistory } from 'vue-router'

import store from "@/store";

import ProductView from '../views/ProductView.vue';
import CategoryView from "@/views/CategoryView";
import SearchView from "@/views/SearchView";
import CartView from "@/views/CartView";
import SignUpView from "@/views/SignUpView";
import LogInView from "@/views/LogInView";
import MyAccountView from "@/views/MyAccountView";
import CheckoutView from "@/views/CheckoutView";
import SuccessView from "@/views/SuccessView";
import HomeView from "@/views/HomeView";


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/cart/checkout',
    name: 'checkout',
    component: CheckoutView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/success',
    name: 'success',
    component: SuccessView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'product',
    component: ProductView
  },
  {
    path: '/:category_slug',
    name: 'category',
    component: CategoryView
  },
  {
    path: '/sign-up',
    name: 'signUp',
    component: SignUpView
  },
  {
    path: '/log-in',
    name: 'logIn',
    component: LogInView
  },
  {
    path: '/my-account',
    name: 'myAccount',
    component: MyAccountView,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({name: 'logIn', query: {to: to.path} });
  } else {
    next()
  }
})

export default router
