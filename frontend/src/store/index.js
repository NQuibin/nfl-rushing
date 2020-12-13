import Vue from 'vue'
import Vuex from 'vuex'

import playerStats from '@/store/player-stats'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    playerStats
  }
})
