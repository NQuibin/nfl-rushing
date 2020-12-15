<template>
  <v-container
    fluid
    class="px-12"
  >
    <v-row>
      <v-col cols="12">
        <h1>the Rush</h1>
      </v-col>
    </v-row>
    <header-inputs
      @search="onSearch"
      @download="onDownload"
    />
    <player-stats-table
      :total-player-stats="totalPlayerStats"
      :stats="stats"
      :page="filters.page"
      :is-loading="isLoading"
      @update="onUpdate"
    />
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import HeaderInputs from '@/components/HeaderInputs'
import PlayerStatsTable from '@/components/PlayerStatsTable'

export default {
  name: 'PlayerStatsPage',
  components: {
    HeaderInputs,
    PlayerStatsTable
  },
  data () {
    return {
      isLoading: true,
      filters: {}
    }
  },
  computed: {
    ...mapGetters({
      playerStats: 'playerStats/playerStats',
      totalPlayerStats: 'playerStats/totalPlayerStats'
    }),
    headers () {
      return [
        { text: 'Player', align: 'start', value: 'player' },
        { text: 'Team', value: 'team' },
        { text: 'Pos', value: 'pos' },
        { text: 'Att/G', value: 'att_g' },
        { text: 'Att', value: 'att' },
        { text: 'Yds', value: 'yds' },
        { text: 'Avg', value: 'avg' },
        { text: 'Yds/G', value: 'yds_g' },
        { text: 'TD', value: 'td' },
        { text: 'Lng', value: 'lng' },
        { text: '1st', value: 'first' },
        { text: '1st%', value: 'first_percentage' },
        { text: '20+', value: 'twenty_plus' },
        { text: '40+', value: 'forty_plus' },
        { text: 'FUM', value: 'fum' }
      ]
    },
    stats () {
      return this.playerStats || []
    }
  },
  methods: {
    ...mapActions({
      getPlayerStats: 'playerStats/getPlayerStats',
      downloadPlayerStats: 'playerStats/downloadPlayerStats'
    }),
    async onSearch (text) {
      this.isLoading = true
      this.filters.player = text
      this.filters.page = 1

      try {
        await this.getPlayerStats({
          player: text,
          sortField: this.filters.sortField,
          ascending: this.filters.ascending,
          pageSize: this.filters.pageSize
        })
      } finally {
        this.isLoading = false
      }
    },
    async onUpdate (options) {
      this.isLoading = true

      const { sortBy, sortDesc, page, itemsPerPage } = options
      this.filters = {
        player: this.filters.player || '',
        sortField: sortBy.length ? sortBy[0] : null,
        ascending: sortDesc.length ? !sortDesc[0] : null,
        page: page,
        pageSize: itemsPerPage
      }

      try {
        await this.getPlayerStats(this.filters)
      } finally {
        this.isLoading = false
      }
    },
    async onDownload () {
      await this.downloadPlayerStats(this.filters)
    }
  }
}
</script>
