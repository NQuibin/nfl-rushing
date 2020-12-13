import { SET_PLAYER_STATS, SET_TOTAL_PLAYER_STATS } from '@/store/player-stats/mutation-types'

export default {
  [SET_PLAYER_STATS] (state, data) {
    state.playerStats = data
  },
  [SET_TOTAL_PLAYER_STATS] (state, data) {
    state.totalPlayerStats = data
  }
}
