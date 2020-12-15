<template>
  <v-row>
    <v-col cols="12">
      <v-data-table
        height="65vh"
        fixed-header
        sort-by="player"
        :headers="headers"
        :items="stats"
        :items-per-page="25"
        :page="page"
        :server-items-length="totalPlayerStats"
        :loading="isLoading"
        :footer-props="{ itemsPerPageOptions: [5, 10, 25] }"
        :must-sort="true"
        @update:options="$emit('update',$event)"
      />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'PlayerStatsTable',
  props: {
    totalPlayerStats: {
      type: Number,
      required: true
    },
    stats: {
      type: Array,
      required: true
    },
    page: {
      type: Number,
      default: 1
    },
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  computed: {
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
    }
  }
}
</script>
