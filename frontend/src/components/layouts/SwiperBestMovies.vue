<template>
  <div class="best-movies-container">
    <h3 class="pt-10 pb-6 best-movies-title">
      The Best Movies
      <Icon type="md-return-left" size="14" class="ml-1" />
    </h3>
    <SwiperRoot :best="data"></SwiperRoot>
  </div>
</template>

<script>
import SwiperRoot from "../swipers/SwiperRoot";
export default {
  components: {
    SwiperRoot,
  },
  props: ["data"],
};
</script>

<style scoped>
.best-movies-container {
  position: relative;
  padding-bottom: 30px;
}
.best-movies-container::after {
  height: 2px;
  width: 100%;
  position: absolute;
  content: "";
  bottom: 0;
  left: 0;
  background-color: rgba(255, 255, 255, 0.2);
}
.best-movies-title {
  color: #fff;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 13px;
}
@media screen and (max-width: 640px) {
  .best-movies-title {
    padding-top: 0 !important;
    padding-bottom: 13px !important;
  }
}
</style>
