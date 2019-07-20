import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
  primary: "#FF9F00",    
  secondary: '#FFDB00',
  accent: '#4312AE',
  error: '#0F4FA8'
}
  }
  )