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
    <v-row>
      <v-col cols="12"
      >
        <v-row>
          <v-col
            cols="2"
          >
            <v-text-field
              v-model.trim="searchValue"
              outlined
              placeholder="Filter by player name"
              @keydown.enter="onSearch"
            />
          </v-col>
          <v-col>
            <v-btn
              depressed
              color="primary"
              @click="onSearch"
            >
              Search
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-data-table
          height="70vh"
          :headers="headers"
          :fixed-header="true"
          :items="stats"
          :server-items-length="totalPlayerStats"
          :loading="isLoading"
          @update:options="onUpdate"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'PlayerStatsPage',
  data () {
    return {
      isLoading: true,
      searchValue: null
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
    },
    itemsLength () {
      return this.playerStats ? this.playerStats.length : 0
    }
  },
  methods: {
    ...mapActions({
      getPlayerStats: 'playerStats/getPlayerStats'
    }),
    async onSearch () {
      try {
        this.isLoading = true
        await this.getPlayerStats({ player: this.searchValue })
      } finally {
        this.isLoading = false
      }
    },
    async onUpdate (options) {
      console.log(options)
      const { sortBy, sortDesc, page, itemsPerPage } = options
      const params = {
        player: this.searchValue,
        sort_field: sortBy.length ? sortBy[0] : null,
        ascending: sortDesc.length ? !sortDesc[0] : null,
        page: page,
        page_size: itemsPerPage
      }
      try {
        await this.getPlayerStats(params)
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>
