<template>
  <div>
    <swiper v-if="this.$store.state.swiperLoader === false" class="swiper" :options="swiperOption">
      <swiper-slide v-for="(movie,index) in best" :key="index">
        <div
          class="swiper-item-container flex flex-col justify-end"
          :style="{backgroundImage: `url(${movie.review_img})`}"
        >
          <div class="flex flex-col swiper-item-body">
            <router-link target="_blank" :to="{ name: 'detail', params: {slug : movie.slug} }">
              <span class="swiper-item-link">{{movie.title}}</span>
            </router-link>
            <div class="flex justify-between">
              <span>
                <Icon size="16" type="md-star" class="rate-icn" />
                {{movie.imdb}}
              </span>
              <span>
                <Icon size="16" type="md-calendar" class="mr-1 rate-icn" />
                {{movie.production_year}}
              </span>
            </div>
          </div>
        </div>
      </swiper-slide>
    </swiper>
    <swiper v-if="this.$store.state.swiperLoader === true" class="swiper" :options="swiperOption">
      <swiper-slide>
        <div class="swiper-loading-container flex justify-between items-center">
          <div class="swiper-loader-img mr-2"></div>
          <div class="w-full h-full flex flex-col justify-around">
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="swiper-loading-container flex justify-between items-center">
          <div class="swiper-loader-img mr-2"></div>
          <div class="w-full h-full flex flex-col justify-around">
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="swiper-loading-container flex justify-between items-center">
          <div class="swiper-loader-img mr-2"></div>
          <div class="w-full h-full flex flex-col justify-around">
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="swiper-loading-container flex justify-between items-center">
          <div class="swiper-loader-img mr-2"></div>
          <div class="w-full h-full flex flex-col justify-around">
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
          </div>
        </div>
      </swiper-slide>

      <swiper-slide>
        <div class="swiper-loading-container flex justify-between items-center">
          <div class="swiper-loader-img mr-2"></div>
          <div class="w-full h-full flex flex-col justify-around">
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
            <div class="swiper-loader"></div>
          </div>
        </div>
      </swiper-slide>
    </swiper>
    <swiper
      v-if="this.$store.state.swiperLoader === 'failed'"
      class="swiper"
      :options="swiperFailedOption"
    >
      <swiper-slide class="failed-swipper-container">
        <div class="bg-gray-900 failed-swiper rounded-md flex justify-center items-center flex-col">
           <h3 class="w-full text-xl text-center text-purple-400">
            Oops
            <i class="fas fa-exclamation-circle ml-2"></i>
          </h3>
          <p class="text-red-400 mt-5 text-center font-">
            There is a server problem! Try again later please...
            <i class="ml-2 fas fa-heart-broken"></i>
          </p>
        </div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>

export default {
  name: "Swiper-Root",
  data() {
    return {
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 15,
        autoplay: {
          delay: 4000,
          disableOnInteraction: false,
        },
        breakpoints: {
          1024: {
            slidesPerView: 5,
          },
          768: {
            slidesPerView: 4,
          },
        },
      },
      
      swiperFailedOption: {
        slidesPerView: 1,
      },
    };
  },
  props: ["best"],
};
</script>

<style scoped>
.failed-swipper-container{
  width: 100% !important;
}
.failed-swiper{
  height: 150px;
  width: 100% !important;
}
.swiper-loader-img {
  width: 250px;
  height: 90%;
  background-image: linear-gradient(
    135deg,
    rgba(45, 55, 72, 1) 0%,
    #303c52 100%
  );
  border-radius: 4px;
}
.swiper-loader {
  width: 100%;
  height: 6px;
  background-image: linear-gradient(
    135deg,
    rgba(45, 55, 72, 1) 0%,
    #303c52 100%
  );
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}

.swiper-loader::before {
  position: absolute;
  left: 0;
  top: 0;
  background-color: rgba(255, 255, 255, 0.116);
  content: "";
  width: 50%;
  height: 100%;
  animation: loadingBarAnimation 0.5s ease infinite;
  animation-direction: alternate-reverse;
}

@keyframes loadingBarAnimation {
  0% {
    left: 0;
  }
  100% {
    left: 100%;
  }
}
.swiper-loading-container {
  height: 100px;
}
.rate-icn {
  color: #f3c457;
}
.swiper-item-link {
  font-size: 13px;
  text-transform: uppercase;
  margin-bottom: 6px;
  color: #6fbc9d;
}
.swiper-item-link:hover {
  color: #84dfbb;
}
.swiper-item-body {
  background-color: black;
  padding: 6px;
  color: white;
  font-weight: 600;
  font-size: 12px;
}
.swiper-item-container {
  width: 100%;
  height: 330px;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  z-index: 1;
}
@media screen and (max-width: 600px) {
  .swiper-item-container {
    height: 240px;
  }
}
@media screen and (max-width: 400px) {
  .swiper-item-container {
    height: 200px;
  }

  .swiper-item-body div span {
  }
  .swiper-item-link {
    font-size: 11px;
  }
}
</style>