<template>
  <div class="movie-list-section">
    <div
      v-if="this.$store.state.loading == true"
      class="grid grid-cols-2 grid-rows-2 h-full pb-10"
    >
      <div
        v-if="this.$store.state.loading == true"
        class="flex flex-col justify-between p-2"
      >
        <div class="loading-image"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
      </div>

      <div
        v-if="this.$store.state.loading == true"
        class="flex flex-col justify-between p-2"
      >
        <div class="loading-image"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
      </div>

      <div
        v-if="this.$store.state.loading == true"
        class="flex flex-col justify-between p-2"
      >
        <div class="loading-image"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
      </div>

      <div
        v-if="this.$store.state.loading == true"
        class="flex flex-col justify-between p-2"
      >
        <div class="loading-image"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
        <div class="loading-bar"></div>
      </div>
    </div>

    <div v-if="this.$store.state.loading == false" class="grid md:grid-cols-2">
      <div
        class="px-2 pb-4 movie-main-container"
        v-for="(item, index) in data"
        :key="index"
      >
        <div
          class="item-img"
          :style="{ backgroundImage: `url(${item.review_img})` }"
        >
          <router-link
            target="_blank"
            :to="{ name: 'detail', params: { slug: item.slug } }"
          >
            <a class="movie-title mb-1">{{ item.title }}</a>
          </router-link>

          <div class="movie-hidden-info p-2 flex flex-col">
            <span
              class="short-summary border-gray-800 text-yellow-400  mb-1 pb-1 border-b-2 uppercase font-semibold"
            >
              Summary
            </span>
            <p class="movie-hidden-summary">{{ item.short_desc }}</p>
            <div class="flex items-center justify-between">
              <div>
                <span
                  class="tag"
                  v-for="(tag, index) in item.category"
                  :key="index"
                  >{{ tag }}</span
                >
              </div>
              <div>
                <router-link
                  target="_blank"
                  :to="{ name: 'detail', params: { slug: item.slug } }"
                >
                  <Button type="success">
                    Visit
                    <Icon type="ios-arrow-forward" class="ml-1" size="16" />
                  </Button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="flex justify-between items-center info-container">
          <div class="flex flex-col w-full p-2 movie-info-body">
            <span class="ml-2 movie-info imdb">IMDb</span>
            <span class="self-center movie-info-desc">{{ item.imdb }}</span>
          </div>
          <div class="flex flex-col w-full p-2 movie-info-body">
            <span class="ml-2 movie-info">
              <Icon type="md-time" size="14" />
            </span>
            <span class="self-center movie-info-desc">{{item.length}}</span>
          </div>
        </div>
      </div>
    </div>

    <div v-if="this.$store.state.loading == 'failed'" class="h-full px-2">
      <div class="failed-container">
        <div class="bg-gray-900 rounded-md p-10 h-full">
          <h3 class="w-full text-xl text-center text-purple-400">
            Oops
            <i class="fas fa-exclamation-circle ml-2"></i>
          </h3>
          <p class="text-red-400 mt-5 text-center font-">
            There is a server problem! Try again later please...
            <i class="ml-2 fas fa-heart-broken"></i>
          </p>
        </div>
      </div>
    </div>

    <Page
      v-if="!this.$store.state.loading"
      class="pagination-custom"
      :total="this.$store.state.allMoviesAndSeries.count"
      :page-size="4"
      @on-change="sendPage"
      :current="this.$store.state.currentPage"
    />
  </div>
</template>

<script>
export default {
  props: ["data"],
  methods: {
    sendPage: function(event) {
      if (window.innerWidth < 1024) {
        window.scrollTo(0, 650);
      }
      if (window.innerWidth > 1024) {
        window.scrollTo(0, 870);
      }
      this.$store.state.currentPage = event;
      this.$store.commit("fetchFilteredData", this.$store.state.filteredData);
    },
  },
};
</script>

<style scoped>
.short-summary {
  font-size: 12px;
}
.failed-container {
  height: 740px;
}
.loading-image {
  width: 100%;
  height: 200px;
  background-image: linear-gradient(
    135deg,
    rgb(43, 49, 63) 0%,
    rgb(20, 22, 23) 100%
  );
  border-radius: 4px;
  background-size: 400% 400%;
  position: relative;
  overflow: hidden;
}
.loading-image::before {
  height: 50px;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.02);
  position: absolute;
  left: 0;
  top: 0;
  content: "";
  animation: loadingIMGAnimation 0.25s ease infinite;
  animation-direction: alternate-reverse;
}
.loading-bar {
  width: 100%;
  height: 6px;
  background-image: linear-gradient(
    135deg,
    rgba(45, 55, 72, 1) 0%,
    #4a5568 100%
  );
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}
.loading-bar::before {
  height: 6px;
  width: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  position: absolute;
  left: 0;
  content: "";
  animation: loadingBarAnimation 1s ease infinite;
}

@keyframes loadingIMGAnimation {
  0% {
    top: 100%;
  }
  100% {
    top: 0;
  }
}

@keyframes loadingBarAnimation {
  0% {
    left: 0;
  }
  100% {
    left: 100%;
  }
}

.movie-title {
  color: #ffffff;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.85);
  top: 0;
  left: 0;
  width: 100%;
  z-index: 9;
  padding: 14px;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 12px;
}
.movie-title:hover {
  color: #687c91;
}
.movie-hidden-summary {
  line-height: 22px;
  font-size: 13px;
  margin-bottom: 8px;
}
.tag {
  padding: 4px 6px;
  background-color: #f3c457;
  color: black;
  border-radius: 4px;
  margin-right: 5px;
  font-size: 10px;
  font-weight: 800;
  text-transform: uppercase;
}

.movie-hidden-info {
  opacity: 0;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  color: white;
  background-color: #1a1d23;
  transition: 0.25s all ease-in-out;
  z-index: 2;
}

.movie-main-container {
  position: relative;
}
.item-img:hover .movie-hidden-info {
  opacity: 1;
}
.info-container {
  background-color: #1a1d23;
}
.movie-info-body:hover {
  background-color: #2b303b;
}
.movie-info-body:nth-child(1) {
  border-right: none;
}
.movie-info-body:nth-child(2) {
  border-right: none;
}
.movie-info-body:nth-child(3) {
  border-right: none;
}
.movie-info-desc {
  color: white;
}
.movie-info {
  color: white;
  font-size: 12px;
  font-weight: 600;
}
.item-img {
  width: 100%;
  height: 350px;
  background-position: right top;
  background-size: cover;
  background-repeat: no-repeat;
  position: relative;
}
.item-img::after {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.36);
}
.imdb {
  color: #f3c457;
}
.movie-list-section {
  height: 880px;
  position: relative;
}
@media screen and (max-width: 768px) {
  .movie-list-section {
    height: auto;
  }
}
@media screen and (max-width: 500px) {
  .item-img {
    height: 280px;
  }
}
</style>
