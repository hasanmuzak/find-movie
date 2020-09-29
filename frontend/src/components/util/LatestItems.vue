<template>
  <div class="main-container">
    <h3 class="container-title flex items-center mt-2">
      <Icon type="md-play" class="mr-1" />{{title}}
    </h3>
    <div class="flex latest-container" v-for="(item,index) in data" :key="index">
      <div class="img" :style="{backgroundImage: `url(${item.review_img})`}"></div>
      <div class="flex flex-col justify-between w-full px-1">
        <a class="title ml-1" href="#">{{item.title}}</a>
        <div class="flex justify-between items-center">
          <span class="text-white rate-spn">
            <Icon type="md-star" class="icon mr-1" size="16" />{{item.imdb}}
          </span>
          <span class="text-white rate-spn">
            <Icon type="md-calendar" class="icon mr-1" size="16" />{{item.production_year}}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props : ["data", "title"]
};
</script>

<style scoped>
.container-title {
  color: white;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 13px;
  margin-bottom: 8px;
}
.main-container {
  background-color: #343746;
  padding: 6px 11px;
  border-radius: 4px;
}
.latest-container {
  margin-top: 6px;
  border-top: 2px solid #6fbc9d36;
  padding-top: 6px;
}
.latest-container:first-of-type {
  border: none;
}
.rate-spn {
  font-size: 13px;
  font-weight: 600;
}
.icon {
  color: #f3c457;
}
.title {
  color: #6fbc9d;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
}
.title:hover {
  color: #f3c457;
}
.img {
  background-size: cover;
  background-position: top;
  background-repeat: no-repeat;
  min-width: 50px;
  height: 50px;
  border-radius: 4px;
}
</style>