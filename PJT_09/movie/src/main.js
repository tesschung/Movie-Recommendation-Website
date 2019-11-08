import Vue from 'vue'
import App from './App.vue'
// for bootstrap
import 'expose-loader?$!expose-loader?jQuery!jquery'
import 'popper.js/dist/popper.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
