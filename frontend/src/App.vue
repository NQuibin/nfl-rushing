<template>
  <v-app>
    <v-main>
      <player-stats-page />
    </v-main>
  </v-app>
</template>

<script>
import PlayerStatsPage from '@/views/PlayerStatsPage'

export default {
  name: 'App',
  components: {
    PlayerStatsPage
  }
}
</script>
