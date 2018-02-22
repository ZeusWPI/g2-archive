import Vue from 'vue'
import Router from 'vue-router'
import AllPersons from '@/components/AllPersons.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AllPersons',
      component: AllPersons
    }
  ]
})
