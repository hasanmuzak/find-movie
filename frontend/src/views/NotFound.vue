<template>
  <div class="">
    <div class="not-found-container">
      <p class="oops">Ooops!</p>
      <p class="four-zero-four text-yellow-500">404</p>
      <span class="sorry text-white">I'm sorry... But the page you requested was not found :(</span>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.sorry::after{
    position: absolute;
    bottom: 0;
    left: 0;
    content: '';
    height: 3px;
    border-radius: 6px;
    width: 100%;
    background-color: rgba(255, 238, 0, 0.88);
}
.sorry{
    font-size: 26px;
    padding-bottom: 22px;
    position: relative;
}
.four-zero-four{
    font-size: 72px;
}
.oops{
    color: white;
    font-size: 40px;
}
.not-found-container {
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%,-50%);
  text-align: center;
  font-weight: 600;
  width: 100%;
}
</style>