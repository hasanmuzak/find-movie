<template>
  <div class="flex justify-center login-form mt-20 xs:mt-32">
    <form @submit.prevent="login" class="form p-5 rounded" action method="POST">
      <h3 class="login-title flex items-center w-full justify-center">
        <Icon type="md-log-in" class="mr-2 log-icn" size="22" />login
      </h3>
      <p v-if="authFail == true" class="text-red-400 text-center my-2 text-sm">Incorrect username or password...</p>
      <input v-model.lazy="username" class="custom-input" type="text" placeholder="Username" />
      <input v-model.lazy="password" class="custom-input mt-4" type="password" placeholder="Password" />
      <Button html-type="submit" class="submit-btn" type="info">
        <Icon v-if="!loading" type="md-log-in" class="mr-2" />
        <span v-if="!loading">login</span>
        <span v-if="loading">Logging in...</span>
      </Button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      username : '',
      password : '',
      authFail : false
    };
  },
  methods: {
    login : function(){
      this.$store.dispatch('userLogin', {
        username : this.username,
        password : this.password
      }).then(()=>{
        this.$router.push({name : 'home'})
        window.location.reload();
      }).catch(err => {
        this.authFail = true;
        console.log(err);
      })
    }
  },
};
</script>

<style scoped>
.submit-btn {
  background-color: #6fbc9d;
  color: rgb(34, 34, 34);
  border-radius: 4px;
  width: 100%;
  text-transform: capitalize;
  font-size: 12px;
  margin-top: 16px;
  font-weight: 600;
  padding: 10px;
  height: auto;
}
.submit-btn {
  border-color: black !important;
}
.submit-btn:focus {
  border-color: black !important;
}
.log-icn {
  color: #6fbc9d;
}
.login-title {
  color: white;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 16px;
  padding-bottom: 12px;
  letter-spacing: 1px;
  position: relative;
  margin-bottom: 16px;
}
.login-title::after {
  position: absolute;
  width: 50%;
  height: 3px;
  background-color: #6fbc9d;
  content: "";
  left: 0;
  bottom: 0;
}
.login-title::before {
  position: absolute;
  width: 50%;
  height: 3px;
  background-color: #ffffff67;
  content: "";
  right: 0;
  bottom: 0;
}
.form {
  background-color: #1b1d1f;
  width: 350px;
}
.custom-input {
  padding: 10px 6px 12px 12px;
  outline: none;
  border: 2px solid rgb(46, 51, 53);
  background-color: rgb(20, 22, 23);
  width: 100%;
  border-radius: 4px;
  transition: 0.15s;
  color: #e2e2e2;
  font-size: 13px;
}
.custom-input:focus {
  border: 2px solid #6fbc9d;
}
.custom-input::placeholder {
  color: #6f7277;
  font-weight: 600;
}
</style>