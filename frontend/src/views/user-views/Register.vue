<template>
  <div>
    <div class="flex justify-center register-form mt-20 xs:mt-32">
    <form class="form p-5 rounded" action method="POST">
      <h3 class="register-title flex items-center w-full justify-center">
        <Icon type="md-person-add" class="mr-2 reg-icn" size="22" />Register
      </h3>
      <span v-if="failedRegistration" class="mb-3 justify-center flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Username or Email is already taken!</span>
      <input @focus="$v.username.$touch()" v-model="username" class="custom-input" type="text" placeholder="Username" />
      <span v-if="!$v.username.required" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Username is required!</span>
      <span v-if="!$v.username.minLength" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Username must contain at least 6 characters.</span>
      <span v-if="!$v.username.maxLength" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Username must contain at most 20 characters.</span>
      <div class="flex mt-4">
        <input @focus="$v.firstName.$touch()" v-model="firstName" class="custom-input mr-2" type="text" placeholder="First Name" />
        <input @focus="$v.lastName.$touch()" v-model="lastName" class="custom-input" type="text" placeholder="Last Name" />
      </div>
       <span v-if="!$v.firstName.required" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>First name is required</span>
      <span v-if="!$v.lastName.required" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Last name is required</span>
      <input @focus="$v.email.$touch()" v-model="email" class="custom-input mt-4" type="text" placeholder="Email" />
       <span v-if="!$v.email.email" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Enter a valid email!</span>
        <span v-if="!$v.email.required" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Enter is required!</span>
      <input  @focus="$v.password.$touch()" v-model="password" class="custom-input mt-4" type="password" placeholder="Password" />
      <span v-if="!$v.password.required" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Password is required!</span>
      <span v-if="!$v.password.minLength" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Password must contain at least 6 characters!</span>
      <span v-if="!$v.password.maxLength" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Password must contain at most 20 characters!</span>
      <input  @focus="$v.password2.$touch()" v-model="password2" class="custom-input mt-4" type="password" placeholder="Password Confirm" />
      <span v-if="!$v.password2.sameAs" class="mt-3 flex items-center text-red-400 font-semibold"><i class="fas fa-exclamation-circle mr-2"></i>Passwords don't match!</span>
      <Button :disabled="$v.$invalid" :loading="loading" class="submit-btn" @click="registerUser" type="info">
        <Icon v-if="!loading" type="md-add" class="mr-2"  />
        <span v-if="!loading">Register</span>
        <span v-if="loading">Please wait...</span>
      </Button>
    </form>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import {required, minLength, maxLength, email, sameAs} from 'vuelidate/lib/validators';
export default {
  data() {
    return {
      username : null,
      firstName : null,
      lastName: null,
      email:null,
      loading: null,
      password:null,
      password2:null,
      failedRegistration : null
    };
  },
  methods: {
    registerUser : function(){
      this.loading = true
      axios.post('http://localhost:8000/auth/users/', {
        email : this.email,
        username : this.username,
        first_name : this.firstName,
        last_name : this.lastName,
        password : this.password
      }).then((response)=>{
        console.log(response.data);
        this.loading = false
        this.$router.push({name : 'login'});
      }).catch(err=>{
        this.loading = false
        this.failedRegistration = true;
        console.log(err);
      });
    }
  },
  validations : {
    username : {
      required,
      minLength : minLength(6),
      maxLength : maxLength(20)
    },
    firstName : {
      required,
    },
    lastName : {
      required,
    },
    email:{
      required,
      email
    },
    password : {
      required,
      minLength : minLength(6),
      maxLength : maxLength(20)
    },
    password2 : {
      required,
      minLength : minLength(6),
      maxLength : maxLength(20),
      sameAs : sameAs('password')
    },
  }
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
.submit-btn{
    border-color: black !important;
  }
.submit-btn:focus{
  border-color: black !important;
}
.reg-icn {
  color: #6fbc9d;
}
.register-title {
  color: white;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 16px;
  padding-bottom: 12px;
  letter-spacing: 1px;
  position: relative;
  margin-bottom: 16px;
}
.register-title::after {
  position: absolute;
  width: 50%;
  height: 3px;
  background-color: #6fbc9d;
  content: "";
  left: 0;
  bottom: 0;
}
.register-title::before {
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
  max-width: 450px;
}
.custom-input {
  padding: 10px 6px 12px 12px;
  outline: none;
  border: 2px solid rgb(46, 51, 53);
  background-color: rgb(20, 22, 23);
  width: 100%;
  border-radius: 4px;
  transition: 0.15s;
  color: #c0c0c0;
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