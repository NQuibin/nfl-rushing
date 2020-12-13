import PlayerStatsClient from '@/clients/PlayerStatsClient'
import { SET_PLAYER_STATS, SET_TOTAL_PLAYER_STATS } from '@/store/player-stats/mutation-types'

const getClient = () => {
  return new PlayerStatsClient()
}

export const getPlayerStats = async ({ commit }, options) => {
  const client = getClient()

  try {
    const response = await client.getPlayerStats({ ...options })
    commit(SET_PLAYER_STATS, response.data.data)
    commit(SET_TOTAL_PLAYER_STATS, response.data.total)
  } catch (err) {
    throw new Error(`Cannot fetch player stats. - ${err}`)
  }
}
