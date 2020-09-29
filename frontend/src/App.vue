<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from "./components/layouts/Navbar";
export default {
  name: "App",
  components: {
    Navbar,
  },

};
</script>

<style>
#app {
}
</style>
