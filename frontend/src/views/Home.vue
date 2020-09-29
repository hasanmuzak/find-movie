<template>
  <div>
    <div class="container mx-auto">
      <!-- <p v-if="firstName">Welcome {{this.$store.state.firstname}}</p> -->

      <SwiperBestMovies :data="getBestMovies"></SwiperBestMovies>
      <SwiperBestSeries :data="getBestSeries"></SwiperBestSeries>
      <div class="w-full flex flex-col lg:flex-row body-container pt-5">
        <div class="w-full lg:w-1/6 home-filter-section">
          <Button class="show-btn" type="info" @click="showBox">
            {{showData}}
            <Icon class="ml-2" :type="showIcon" size="16" />
          </Button>
          <div class="filter-box-home-container">
            <FilterBox></FilterBox>
          </div>
        </div>
        <div class="w-full lg:w-4/6">
          <MovieList :data="getAllMoviesAndSeries.results"></MovieList>
        </div>
        <div class="w-full lg:w-1/6">
          <div class="mt-5 lg:m-0">
            <LatestMovies></LatestMovies>
          </div>
          <div class="my-5">
            <LatestSeries></LatestSeries>
          </div>
        </div>
      </div>
    </div>
    <div>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import SwiperBestMovies from "../components/layouts/SwiperBestMovies";
import SwiperBestSeries from "../components/layouts/SwiperBestSeries";
import FilterBox from "../components/util/FilterBox";
import MovieList from "../components/util/MovieList";
import LatestMovies from "../components/layouts/LatestMovies";
import LatestSeries from "../components/layouts/LatestSeries";
import Footer from "../components/layouts/Footer";

import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    SwiperBestMovies,
    SwiperBestSeries,
    FilterBox,
    MovieList,
    LatestMovies,
    LatestSeries,
    Footer,
  },
  data() {
    return {
      showData: "Show Filter Box",
      showIcon: "md-eye",
    };
  },

  methods: {
    showBox: function () {
      if (this.showData == "Show Filter Box") {
        this.showData = "Hide Filter Box";
        this.showIcon = "md-eye-off";
      } else {
        this.showData = "Show Filter Box";
        this.showIcon = "md-eye";
      }
      var filterBox = document.querySelector(".filter-box-home-container");
      filterBox.classList.toggle("active");
    },
    ...mapActions([
      "bestMoviesAction",
      "bestSeriesAction",
      "allMoviesAndSeriesAction"
    ]),
  },
  computed: {
    ...mapGetters(["getBestMovies","getBestSeries","getAllMoviesAndSeries"]),
  },
  mounted() {
    this.bestMoviesAction();
    this.bestSeriesAction();
    this.allMoviesAndSeriesAction();
  },
};
</script>

<style scoped>
.show-btn {
  font-size: 12px;
  color: black;
  width: 100%;
  margin-bottom: 12px;
  display: none;
}
@media screen and (max-width: 1024px) {
  .home-filter-section {
    padding: 8px;
  }
  .show-btn {
    display: block;
  }
  .filter-box-home-container {
    display: none;
  }
  .filter-box-home-container.active {
    display: block;
    margin-bottom: 8px;
  }
}
@media screen and (max-width: 640px) {
  .container {
    padding: 20px !important;
  }
}
</style>