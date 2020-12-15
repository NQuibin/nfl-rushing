<template>
  <v-container
    fluid
    class="player-stats-container px-12"
  >
    <v-snackbar
      v-model="showSnack"
      color="error"
      :timeout="2000"
    >
      {{ snackMessage }}
    </v-snackbar>
    <v-row>
      <v-col cols="12">
        <h1>
          <img
            class="player-stats-container__logo d-inline-block mr-3"
            alt="theScore logo"
            src="@/assets/the_score.png"
          />
          the Rush
        </h1>
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
      filters: {},
      showSnack: false,
      snackMessage: null
    }
  },
  computed: {
    ...mapGetters({
      playerStats: 'playerStats/playerStats',
      totalPlayerStats: 'playerStats/totalPlayerStats'
    }),
    stats () {
      return this.playerStats || []
    }
  },
  methods: {
    ...mapActions({
      getPlayerStats: 'playerStats/getPlayerStats',
      downloadPlayerStats: 'playerStats/downloadPlayerStats'
    }),
    displaySnackError () {
      this.showSnack = true
      this.snackMessage = 'Cannot fetch player stats, please try again.'
    },
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
      } catch (err) {
        this.displaySnackError()
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
      } catch (err) {
        this.displaySnackError()
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

<style lang="scss" scoped>
.player-stats-container {
  &__logo {
    height: 32px;
    width: 32px;
    vertical-align: sub;
  }
}
</style>
