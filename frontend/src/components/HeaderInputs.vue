<template>
  <v-row>
    <v-col cols="12"
    >
      <v-row align="center">
        <v-col
          cols="12"
          sm="3"
        >
          <v-text-field
            v-model.trim="searchText"
            outlined
            hide-details
            placeholder="Filter by player name"
            height="36"
            @keydown.enter="$emit('search', searchText)"
          />
        </v-col>
        <v-col>
          <v-btn
            depressed
            color="primary"
            class="mr-3"
            @click="$emit('search', searchText)"
          >
            Search
          </v-btn>
          <v-btn
            depressed
            color="secondary"
            @click="$emit('download')"
          >
            Download
          </v-btn>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'HeaderInputs',
  data () {
    return {
      searchText: null
    }
  }
}
</script>
