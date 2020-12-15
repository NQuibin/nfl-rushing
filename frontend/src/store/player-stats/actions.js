import PlayerStatsClient from '@/clients/PlayerStatsClient'
import { SET_PLAYER_STATS, SET_TOTAL_PLAYER_STATS } from '@/store/player-stats/mutation-types'

const getClient = () => {
  return new PlayerStatsClient()
}

export const getPlayerStats = async ({ commit }, options) => {
  const client = getClient()

  try {
    const response = await client.getPlayerStats({
      player: options.player,
      sort_field: options.sortField,
      ascending: options.ascending,
      page: options.page,
      page_size: options.pageSize
    })

    commit(SET_PLAYER_STATS, response.data.data)
    commit(SET_TOTAL_PLAYER_STATS, response.data.total)
  } catch (err) {
    throw new Error(`Cannot fetch player stats. - ${err}`)
  }
}

export const downloadPlayerStats = async (_, options) => {
  const client = getClient()
  client.downloadPlayerStats({
    player: options.player,
    sort_field: options.sortField,
    ascending: options.ascending
  })
}
