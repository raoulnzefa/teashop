<template>

  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">


        <form class="has-text-centered box sign-up-box" @submit.prevent="submitForm">
          <h1 class="title box sign-up-box">Login</h1>
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

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">
              {{ error }}
            </p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button button-green-prm" style="color: white">
                Log in
              </button>
            </div>
          </div>
          <router-link style="color: #92ddc8; font-weight: 700" to="/sign-up">
            <div class="box sign-up-box has-text-centered" style="background: #22BD70">
              Click here to sign up!
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
export default {
  name: "LogInView",
  data() {
    return {
      username: '',
      password: '',
      errors: [],
    }
  },
  mounted() {
    document.title = "Log In | TeaShop"
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem("token")

      const formData = {
        username: this.username,
        password: this.password
      }

      await  axios
          .post("/api/v1/token/login/", formData)
          .then(response => {
            const token = response.data.auth_token

            this.$store.commit('setToken', token)

            axios.defaults.headers.common['Authorization'] = "Token " + token

            localStorage.setItem('token', token)

            const toPath = this.$route.query.to || '/my-account'
            this.$router.push(toPath)
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }
          })
    }
  }
}
</script>

<style lang="scss" scoped>

$primary-color: #3EB489;
$secondary-color: #92ddc8;

label {
  font-weight: 500;
}

 .button-green-prm {
   background: $secondary-color;
 }

.sign-up-box {
  background: $primary-color;
  color: white;
}
</style>