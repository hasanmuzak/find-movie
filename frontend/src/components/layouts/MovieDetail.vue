<template>
  <div class="container mx-auto">
    <MovieDetailPanel></MovieDetailPanel>
  </div>
</template>

<script>
import MovieDetailPanel from "../util/MovieDetailPanel";
export default {
  data() {
    return {
      movieDetail: null,
      urlDetail: null,
    };
  },
  components: {
    MovieDetailPanel,
  },

};
</script>

<style scoped>
</style>
