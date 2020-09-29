import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
//IView Uİ
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import './assets/styles/index.css';
//Swiper
import {Swiper as SwiperClass, Autoplay, Pagination} from 'swiper/swiper.esm'
import GetAwesomeSwiper from 'vue-awesome-swiper/dist/exporter'
import Vuelidate from 'vuelidate'
//Store
import {store} from './store/store'

SwiperClass.use([Autoplay,Pagination])

import { routes } from './routes'

const router = new VueRouter({
  routes,
  scrollBehavior (){
    return {x:0,y:0};
  }
})

import 'swiper/swiper-bundle.css'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(ViewUI);
Vue.use(GetAwesomeSwiper(SwiperClass))
Vue.use(Vuelidate)


new Vue({
  render: h => h(App),
  router,
  store,
}).$mount('#app')
