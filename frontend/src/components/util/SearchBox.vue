<template>
  <div id="" class="searchBox w-full" v-if="data != '' && data != null">
    <div
      class="flex w-full box-container py-2"
      v-for="(item, index) in data"
      :key="index"
    >
      <div
        class="search-img"
        :style="{ backgroundImage: `url(${item.review_img})` }"
      ></div>
      <div class="search-info flex flex-col w-full justify-between p-1">
        <a class="movie-link" href="#">{{ item.title }}</a>
        <p class="lg:hidden info my-2">{{ item.short_desc }}</p>
        <p class="director my-1">{{ item.director }}</p>
        <div class="flex justify-between">
          <span class="rate">
            <Icon class="search-icn" type="ios-star" />{{ item.imdb }}
          </span>
          <span class="rate">
            <Icon class="search-icn" type="md-calendar" />{{
              item.production_year
            }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["data"],

};
</script>

<style scoped>
.box-container {
  border-bottom: 2px solid #6fbc9d7a;
}
.box-container:nth-last-child(1) {
  border-bottom: none;
}
.info {
  line-height: 18px;
  font-size: 11px;
}
.movie-link {
  color: #f3c457;
  text-transform: capitalize;
}
.movie-link:hover {
  color: #efea5a;
}
.rate {
  font-size: 12px;
}
.director {
  font-size: 10px;
}
.search-icn {
  color: #f1c453 !important;
}
.search-img {
  width: 80px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top;
}
.searchBox {
  position: absolute;
  background-color: #1a1c23;
  padding: 6px;
  max-height: 350px;
  overflow-y: scroll;
}
.searchBox::-webkit-scrollbar {
  width: 5px;
}
.searchBox::-webkit-scrollbar-track {
  background: transparent;
}
.searchBox::-webkit-scrollbar-thumb {
  background: #6fbc9d;
  border-radius: 4px;
}
@media screen and (max-width: 640px) {
  .director,
  .rate {
    font-size: 13px;
  }
  .info {
    display: none;
  }
}
@media screen and (max-width: 420px) {
  .searchBox {
    height: 270px;
  }
}
</style>