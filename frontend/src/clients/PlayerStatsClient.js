import axios from 'axios'

export default class PlayerStatsClient {
  constructor () {
    this.client = axios.create({
      baseURL: 'http://127.0.0.1:8000'
    })
  }

  getPlayerStats (params) {
    return this.client.get('/v1/player-stats', { params })
  }

  downloadPlayerStats (params) {
    const query = new URLSearchParams(params)
    window.location.href = `${this.client.defaults.baseURL}/v1/player-stats/download?${query.toString()}`
  }
}
