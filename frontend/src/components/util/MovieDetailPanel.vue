<template>
  <div class="detail-container flex flex-col md:flex-row p-6 md:mt-6">
    <div
      v-if="this.$store.state.detailLoader == true"
      class="loading-panel flex items-center justify-center w-full h-full"
    >
      <sync-loader size="10px"></sync-loader>
      <span class="ml-2 find text-green-400 font-semibold">Find</span>
      <span class="ml-2 text-yellow-400 font-semibold the">The</span>
      <span class="ml-2 find text-green-400 font-semibold">Movie</span>
    </div>
    <div
      v-if="this.$store.state.detailLoader == 'failed'"
      class="loading-panel flex items-center justify-center w-full h-full"
    >
      <span class="text-red-400 font-semibold"
        >Server problem! Please try again later...
        <i class="ml-2 fas fa-heart-broken"></i
      ></span>
    </div>
    <div
      class="img w-full md:w-1/3 rounded"
      :style="{ backgroundImage: `url(${movieData.review_img})` }"
    ></div>
    <p></p>
    <div class="detail-content w-full md:w-2/3 px-4">
      <Breadcrumb>
        <BreadcrumbItem to="/">Home</BreadcrumbItem>
        <BreadcrumbItem>{{ movieData.title }}</BreadcrumbItem>
      </Breadcrumb>
      <div class="flex justify-between my-3">
        <p class="text-red-400 uppercase font-semibold text-sm">
          {{ movieData.title }}
        </p>
        <p
          class="text-black bg-yellow-400 py-1 px-2 rounded uppercase font-semibold text-xs"
        >
          <i class="fas fa-tv mr-1"></i>
          {{ movieData.status }}
        </p>
      </div>
      <p class="detail-desc text-gray-400">{{ movieData.short_desc }}</p>
      <div class="detail-body-container p-2 rounded mt-4">
        <div class="stars-container">
          <span class="text-yellow-500">Director :</span>
          <span class="text-gray-600 ml-1">{{ movieData.director }}</span>
        </div>
        <div class="stars-container">
          <span class="text-yellow-500">Stars :</span>
          <div class="inline">
            <span class="ml-1 text-gray-600">{{ movieData.stars }}</span>
          </div>
        </div>
      </div>
      <div class="download-options-container mt-5" v-if="linkData[0] != null">
        <h3
          class="mb-4 pb-2 download-options-heading text-sm flex items-center text-yellow-400"
        >
          <i class="fas fa-download mr-2"></i>Download Options
        </h3>
        <div v-if="movieData.status == 'movie'" class="grid sm:grid-cols-3">
          <a
            v-if="movieData.available_4k"
            :href="linkData[0].link_4k"
            class="w-full sm:w-auto sm:mt-0 mt-3 download-link bg-yellow-400 font-semibold rounded p-2 text-xs text-black text-center"
          >
            Download 4K
            <Icon type="ios-magnet" />
          </a>
          <a
            v-if="movieData.available_fhd"
            :href="linkData[0].link_fhd"
            class="w-full sm:w-auto sm:mt-0 mt-3 download-link bg-yellow-400 font-semibold rounded p-2 text-xs text-black text-center"
          >
            Download 1080P
            <Icon type="ios-magnet" />
          </a>
          <a
            v-if="movieData.available_hd"
            :href="linkData[0].link_hd"
            class="w-full sm:w-auto sm:mt-0 mt-3 download-link bg-yellow-400 font-semibold rounded p-2 text-xs text-black text-center"
          >
            Download 720P
            <Icon type="ios-magnet" />
          </a>
        </div>
        <div v-if="movieData.available_fhd == true && movieData.status == 'serie'">
          <h3 class="text-purple-400 font-semibold uppercase block mb-2">
            1080p :
          </h3>
          <div
            v-if="movieData.status == 'serie'"
            class="grid grid-cols-2 sm:grid-cols-3"
          >
            <div
              v-for="(item, index) in linkData"
              :key="index"
              class="mt-2 sm:mt-3 w-full sm:w-auto serie-url-container sm:mr-3"
            >
              <a
                :href="item.link_fhd"
                class="mr-2 block download-link bg-yellow-400 font-semibold rounded p-2 text-xs text-black text-center"
              >
                Season {{ item.season_number }} - 1080p
                <Icon type="ios-magnet" />
              </a>
            </div>
          </div>
        </div>
        <div v-if="movieData.available_hd && movieData.status == 'serie' == true" class="mt-2">
          <h3 class="text-purple-400 font-semibold uppercase block my-2">
            720p :
          </h3>
          <div
            v-if="movieData.status == 'serie'"
            class="grid grid-cols-2 sm:grid-cols-3"
          >
            <div
              v-for="(item, index) in linkData"
              :key="index"
              class="mt-2 sm:mt-3 w-full sm:w-auto serie-url-container sm:mr-3"
            >
              <a
                :href="item.link_hd"
                class="mr-2 block download-link bg-yellow-400 font-semibold rounded p-2 text-xs text-black text-center"
              >
                Season {{ item.season_number }} - 720p
                <Icon type="ios-magnet" />
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="detail-ranks-container py-3 flex justify-between">
        <div class="flex">
          <span class="flex items-center text-green-600 font-semibold text-xs">
            <Icon type="md-star" class="mr-2" size="16" />IMDb :
          </span>
          <span class="ml-1 font-semibold text-xs text-gray-400">{{
            movieData.imdb
          }}</span>
        </div>
        <div class="flex">
          <span class="flex items-center text-green-600 font-semibold text-xs">
            <Icon type="md-calendar" class="mr-2" size="16" />Production Year :
          </span>
          <span class="ml-1 font-semibold text-xs text-gray-400">{{
            movieData.production_year
          }}</span>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import SyncLoader from "vue-spinner/src/SyncLoader";
import axios from "axios";

export default {
  // props: {
  //   movieData: {
  //     type: Object,
  //   },
  //   linkData: {
  //     type: Array,
  //   },

  // },
  data() {
    return {
      movieData: {},
      linkData: [],
    };
  },
  components: {
    SyncLoader,
  },
  methods: {
    fetchMovieDetail: async function (url) {
      this.$store.state.detailLoader = true;
      await axios
        .get("https://find-movie-api.herokuapp.com/api/movies-series/detail/" + url)
        .then(async (response) => {
          this.$store.state.detailLoader = false;
          this.movieData = response.data;
        })
        .catch((err) => {
          this.$store.state.detailLoader = "failed";
          console.log(err);
        });
    },
    fetchURLDetail: async function (url) {
      await axios
        .get("https://find-movie-api.herokuapp.com/api/movies-series/links/" + url)
        .then(async (response) => {
          this.linkData = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.fetchMovieDetail(this.$route.params.slug);
    this.fetchURLDetail(this.$route.params.slug);
  },
};
</script>

<style scoped>
.find {
  animation: findAnimation 0.25s ease infinite;
  animation-direction: alternate-reverse;
}
.the {
  animation: theAnimation 0.25s ease infinite;
  animation-direction: alternate-reverse;
}
@keyframes theAnimation {
  0% {
    margin-bottom: 30px;
  }
  100% {
    margin-bottom: 0;
  }
}
@keyframes findAnimation {
  0% {
    margin-bottom: 0;
  }
  100% {
    margin-bottom: 30px;
  }
}
.loading-panel {
  position: absolute;
  background-color: #0e1118;
  z-index: 999;
  left: 0;
  top: 0;
}
.serie-url-container:nth-of-type(1),
.serie-url-container:nth-of-type(2),
.serie-url-container:nth-of-type(3) {
  margin-top: 0;
}
.detail-content {
  position: relative;
}
.download-options-heading {
  position: relative;
}
.download-options-heading::after {
  position: absolute;
  content: "";
  height: 2px;
  width: 50%;
  bottom: 0;
  left: 0;
  background-color: #f6e05e;
}
.download-options-heading::before {
  position: absolute;
  content: "";
  height: 2px;
  width: 50%;
  bottom: 0;
  right: 0;
  background-color: #fff;
}
.download-link:nth-of-type(1) {
  margin-top: 0;
}
.download-link {
  margin-right: 10px;
  transition: 0.25s;
}
.download-link:nth-last-of-type(1) {
  margin-right: 0;
}
.download-link:hover {
  color: black;
  background-color: #cebb4e;
}
.detail-body-container {
  background-color: rgb(34, 37, 37);
}
.detail-container {
  background-color: rgb(20, 22, 23);
  border-radius: 4px;
  position: relative;
}
.detail-desc {
  line-height: 25px;
}
.img {
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}
@media screen and (max-width: 768px) {
  .img {
    height: 280px;
    margin-bottom: 10px;
  }
}

@media screen and (max-width: 620px) {
  .serie-url-container:nth-of-type(1),
  .serie-url-container:nth-of-type(2),
  .serie-url-container:nth-of-type(3) {
    margin-top: 0.5rem;
  }

  .download-link:nth-last-of-type(1) {
    margin-right: 0.5rem;
  }
}
</style>
