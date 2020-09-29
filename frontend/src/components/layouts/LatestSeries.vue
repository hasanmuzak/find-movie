<template>
  <div>
    <LatestItems :data="latestMovies" :title="title"></LatestItems>
  </div>
</template>

<script>
import Axios from 'axios'
import LatestItems from '../util/LatestItems'
export default {
  components:{
    LatestItems
  },
  data() {
    return {
      latestMovies : null,
      title:'Latest Series'
    }
  },
  methods : {
    fetchLatestMovies : function(){
      Axios.get('https://find-movie-api.herokuapp.com/api/movies-series/best/series/latest').then(response=>{
        this.latestMovies = response.data;
      }).catch(err =>{
        console.log(err);
      })
    }
  },
  mounted() {
    this.fetchLatestMovies();
  },
}
</script>

<style>

</style>