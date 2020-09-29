<template>
  <div class="best-series-container">
      <h3 class="pt-5 pb-5 best-series-title" ><Icon type="md-return-right" size="14" class="mr-1" />The Best Series</h3>
      <SwiperRoot :best="data"></SwiperRoot>
  </div>
</template>

<script>
import SwiperRoot from '../swipers/SwiperRoot'
export default {
components : {
    SwiperRoot
},
props : ["data"]
}
</script>

<style scoped>
.best-series-container{
  position: relative;
  padding-bottom: 20px;
}
.best-series-container::after{
  height: 2px;
  width: 100%;
  position: absolute;
  content: "";
  bottom: 0;
  left: 0;
  background-color: rgba(255, 255, 255, .2);
}
.best-series-title{
    color: #fff;
    text-transform: uppercase;
    font-weight: 600;
    font-size: 13px;
}
@media screen and (max-width:640px){
  .best-series-title{
      padding-top: 13px !important;
      padding-bottom: 13px !important;
  }
}
</style>