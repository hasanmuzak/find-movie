import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    //Authentication
    accessToken : localStorage.getItem('usr') || null,
    username : localStorage.getItem('name') || null,

    //Movie - Serie - Link Data
    links: null,
    bestMovies: null,
    bestSeries: null,
    allMoviesAndSeries: {},
    comments: null,
    currentPage: 1,
    filteredData: {},

    //Loading
    loading: null,
    swiperLoader: null,
    detailLoader: null,
  },
  getters: {
    isLogged(state){
      if(state.accessToken != null){
        return true;
      }
      else{
        return false;
      }
    },
    getLinks(state) {
      return state.links;
    },
    getBestMovies(state) {
      return state.bestMovies;
    },
    getBestSeries(state) {
      return state.bestSeries;
    },
    getAllMoviesAndSeries(state) {
      return state.allMoviesAndSeries;
    },
    getComments(state) {
      return state.comments;
    },
  },
  mutations: {
    fetchAllMovies(state) {
      state.loading = true;
      axios
        .get(
          "https://find-movie-api.herokuapp.com/api/movies-series/all")
        .then((response) => {
          state.loading = false;
          state.allMoviesAndSeries = response.data;
        })
        .catch((err) => {
          state.loading = "failed";
          console.log(err);
        });
    },
    fetchBestMovies(state) {
      state.swiperLoader = true;
      axios
        .get("https://find-movie-api.herokuapp.com/api/movies-series/best/movies")
        .then((response) => {
          state.swiperLoader = false;
          state.bestMovies = response.data;
        })
        .catch((err) => {
          state.swiperLoader = "failed";
          console.log(err);
        });
    },
    fetchBestSeries(state) {
      state.swiperLoader = true;
      axios
        .get("https://find-movie-api.herokuapp.com/api/movies-series/best/series")
        .then((response) => {
          state.swiperLoader = false;
          state.bestSeries = response.data;
        })
        .catch((err) => {
          state.swiperLoader = "failed";
          console.log(err);
        });
    },
    fetchFilteredData(state, payload) {
      state.loading = true;
      const querystring = require("query-string");
      
      if(Object.keys(payload).length === 0){
        axios
        .get(
          "https://find-movie-api.herokuapp.com/api/movies-series/all?page=" +state.currentPage)
        .then((response) => {
          state.loading = false;
          state.allMoviesAndSeries = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
      }
      else{
        state.filteredData = payload;
        axios
        .get(
          "https://find-movie-api.herokuapp.com/api/movies-series/all?page=" +
            state.currentPage,
          {
            params: {
              imdb: payload.imdb,
              status: payload.status,
              genre: payload.genre,
              is_4k: payload.resolution.is_4k,
              is_fullHD: payload.resolution.is_fullHD,
              is_HD: payload.resolution.is_HD,
            },
            paramsSerializer: (params) => {
              return querystring.stringify(params, { arrayFormat: "comma" });
            },
          }
        )
        .then((response) => {
          state.loading = false;
          state.allMoviesAndSeries = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
      }
    },

    updateStorage(state, payload){
      state.accessToken = payload.access;
      state.username = payload.username;
    },

    destroyStorage(state){
      localStorage.removeItem('usr');
      localStorage.removeItem('name');
      state.accessToken =  null;
      state.username =  null;
    }
  },
  actions: {
    bestMoviesAction({ commit }) {
      commit("fetchBestMovies");
    },
    bestSeriesAction({ commit }) {
      commit("fetchBestSeries");
    },
    allMoviesAndSeriesAction({ commit }) {
      commit("fetchAllMovies");
    },
    userLogin({commit}, userCredentials){
      return new Promise((resolve,reject)=>{
        axios.post('https://find-movie-api.herokuapp.com/api/login/', {
          username : userCredentials.username,
          password : userCredentials.password
        }).then(response =>{
          localStorage.setItem('usr',response.data.access);
          localStorage.setItem('name',response.data.username);
          commit("updateStorage",{access : response.data.access, refresh: response.data.refresh, username: response.data.username});
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    userLogout({commit}){
        commit('destroyStorage');
    }
  },
});
