import state from '@/store/player-stats/state'
import getters from '@/store/player-stats/getters'
import mutations from '@/store/player-stats/mutations'
import * as actions from '@/store/player-stats/actions'

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
