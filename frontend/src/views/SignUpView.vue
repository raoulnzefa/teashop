<template>

  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4 has-text-centered box sign-up-box">
        <h1 class="title box sign-up-box">Sign Up</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>

          <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input type="password" class="input" v-model="password2">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">
              {{ error }}
            </p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button button-green-prm">
                Sign up
              </button>
            </div>
          </div>

          <router-link style="color: #92ddc8; font-weight: 700" to="/log-in">
            <div class="box sign-up-box has-text-centered" style="background: #22BD70">
              Click here to log in!
            </div>
          </router-link>

        </form>
      </div>
    </div>
    <div style="min-height: 10rem"></div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "SignUpView",
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  mounted() {
    document.title = "Sign Up | TeaShop"
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('The username is missing')
      }

      if (this.password === '') {
        this.errors.push('The password is too short')
      }

      if (this.password !== this.password2) {
        this.errors.push('The passwords doesn\'t match')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
            .post("/api/v1/users/", formData)
            .then(response => {
              toast({
                message: 'Account created, please log in!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'top-center'
              })

              this.$router.push('/log-in')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }

                console.log(JSON.stringify(error.response.data))
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
            })
      }

    }
  }
}
</script>

<style lang="scss" scoped>
$primary-color: #3EB489;
$secondary-color: #92ddc8;

.sign-up-box {
  background: $primary-color;
  color: white;
}

label {
  font-weight: 500;
}

 .button-green-prm {
   background: $secondary-color;
 }
</style>