<template>
  <nav class="flex">
    <div id="nav-container" class="nav-container flex items-center w-full">
      <div class="logo">
        <router-link to="/">
          <h3>FindTheMovie</h3>
        </router-link>
      </div>
      <div class="search-container rounded" style="width: 280px">
        <div class="search-bar flex items-center p-2">
          <input type="text" id="search-input" placeholder="Search here..." />
          <i class="fas fa-search"></i>
        </div>
        <SearchBox id="searchContainer" :data="search_result"></SearchBox>
      </div>
      <div class="hamburger" @click="showMenu">
        <div class="line top"></div>
        <div class="line mid"></div>
        <div class="line bot"></div>
      </div>
    </div>
    <div class="flex items-center nav-links">
      <ul class="flex">
        <router-link tag="li" to="/" active-class="link-active" exact>
          <a class="first" href="#">Home</a>
        </router-link>

        <li>
          <a href="#">Contact</a>
        </li>
        <li>
          <a href="#">About</a>
        </li>
      </ul>
      <ul class="flex items-center users">
        <router-link v-if="this.$store.getters.isLogged == false" to="/register" tag="li" active-class="users-link-active">
          <a href="#"> <Icon type="md-add" class="mr-1" />Register </a>
        </router-link>
        <router-link v-if="this.$store.getters.isLogged == false" to="/login" tag="li">
          <a class="login-btn" href="#">
            <Icon type="md-log-in" class="mr-1" />Login
          </a>
        </router-link>
        <router-link v-if="this.$store.getters.isLogged == true" :to="{name:'logout'}" tag="li">
          <a class="">
            Logout
          </a>
        </router-link>
      </ul>
    </div>
  </nav>
</template>

<script>
import axios from "axios";
import SearchBox from "../util/SearchBox";
export default {
  data() {
    return {
      fetch_json: null,
      search_result: null,
      denemeData:null
    };
  },
  components: {
    SearchBox,
  },
  methods: {
    showMenu: function () {
      var menu = document.querySelector(".nav-links");
      var hamburger = document.querySelector(".hamburger");
      hamburger.classList.toggle("active");
      menu.classList.toggle("active");
    },
    getData: function () {
      axios
        .get("https://find-movie-api.herokuapp.com/api/movies-series/all-in-one")
        .then((response) => {
          this.fetch_json = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    
  },
  computed: {
    deneme(){
      return this.$store.getters.isLogged;
    }
  },
  mounted() {
    this.getData();

    const search = document.getElementById("search-input");
    search.addEventListener("input", () => searchTitles(search.value));
    const searchTitles = async (searchData) => {
      const filteredData = this.fetch_json;
      let matches = filteredData.filter((data) => {
        const regex = new RegExp(`\\b${searchData}`, "gi");
        return data.title.match(regex);
      });

      if (searchData.length === 0) {
        matches = [];
      }
      this.search_result = matches;

      if (matches != null || matches != "") {
        let item = document.getElementById("searchContainer");
        document.getElementById("app").onclick = function (e) {
          let clicked = item.contains(e.target);
          if (!clicked) {
            this.search_result = null
            matches = []
            search.value = ''
            return searchTitles(search.value)
          }
        };
      }
    };
  },
};
</script>

<style scoped>
/* Normal Design */
.logo {
  font-weight: 600;
  text-transform: uppercase;
  font-size: 13px;
}
.login-btn {
  transition: 0.25s;
  border-radius: 4px;
  border: 2px solid #6fbc9d;
  color: #6fbc9d;
}
.login-btn:hover {
  background-color: #6fbc9d;
  color: #424759 !important;
  border-color: #6fbc9d;
}
nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #100e1b;
  color: #f3f2f8;
  padding: 15px;
  font-weight: 600;
  font-size: 13px;
  z-index: 9999;
}
.nav-links li a {
  display: flex;
  align-items: center;
  padding: 10px 30px;
}
.nav-links li a:hover {
  color: #f1c453;
}
.nav-links li {
  position: relative;
}
.link-active::after {
  position: absolute;
  content: "";
  bottom: 0;
  border-radius: 6px;
  width: 100%;
  background-color: #6fbc9d;
  height: 2px;
}
.users-link-active::after {
  position: absolute;
  content: "";
  bottom: 0;
  border-radius: 6px;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  background-color: #6fbc9d;
  height: 2px;
}
.search-container {
  margin-left: 15px;
  margin-right: 15px;
  position: relative;
  background-color: #39325d;
}
.low-res-menu-item {
  display: none;
}
/* Responsive Design */
@media screen and (max-width: 1024px) {
  .users-link-active::after {
    width: 100%;
  }
  .nav-links {
    position: absolute;
    flex-direction: column;
    background-color: #100e1b;
    width: 100%;
    top: 62px;
    left: 0;
    z-index: 9998;
    /* display: none; */
    clip-path: circle(100px at 90% -50%);
    -webkit-clip-path: circle(100px at 90% -50%);
    transition: all 0.5s ease-in-out;
  }
  .nav-links ul {
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 100%;
  }
  .users {
    border-top: 2px solid #a17374;
  }
  .login-btn {
    border: none;
    border-radius: 0;
    border-color: rgba(255, 255, 255, 0.2);
    color: white;
  }
  .nav-links.active {
    clip-path: circle(1500px at 90% -20%);
    -webkit-clip-path: circle(1500px at 90% -20%);
  }
  .nav-links li {
    width: 100%;
    height: 100%;
  }
  .nav-links li a {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    padding: 16px;
    font-size: 14px;
    border-top: 2px solid rgba(255, 255, 255, 0.2);
    transition: 0.25s !important;
  }
  .nav-links li a:hover {
    background-color: #f3c457;
    color: #424759;
    border-color: #f3c457;
  }
  .users {
    border-top: none;
  }
  .first {
    border-top: none !important;
  }
  .low-res-menu-item {
    display: block;
  }
  .search-container {
    width: 80% !important;
  }
  .hamburger {
    cursor: pointer;
    z-index: 9999;
  }
  .hamburger.active {
    position: relative;
    margin-top: 10px;
  }
  .hamburger.active .top {
    transform: rotate(45deg);
    position: absolute;
    transition: 0.15s;
  }
  .hamburger.active .mid {
    transform: rotate(-45deg);
    transition: 0.35s;
  }
  .hamburger.active .bot {
    opacity: 0;
    transition: 0.25s;
  }
  .line {
    height: 3px;
    width: 30px;
    background-color: white;
    margin: 5px;
    border-radius: 4px;
  }
}
@media screen and (max-width: 420px) {
  .hamburger {
    margin: 0;
  }
  .search-container {
    margin: 0;
    margin-right: 5px;
    width: 100% !important;
  }
  .logo {
    display: none;
  }
}
</style>