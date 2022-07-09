<template>
<div class="page-my-account">
  <div class="columns is-multiline">

    <div class="box column is-12" style="background: #3EB489">
      <h1 style="color: #F8F8FF" class="title"><i class="fa-regular fa-user fa-lg" ></i> <i class="has-text-light">{{ currentUser.username }}</i></h1>
    </div>

    <div class="column is-12">
      <button class="button is-success mr-2">Change details</button>
      <button @click="logout()" class="button is-danger">Log out</button>
    </div>


    <div class="box column is-12" style="background: #3EB489">
      <h2 class="title has-text-light">My orders:</h2>

      <OrderSummary
        v-for="order in orders"
        :key="order.id"
        :order="order" />
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";

import OrderSummary from "@/components/OrderSummary";

export default {
  name: "MyAccountView",
  components: {
    OrderSummary
  },
  data() {
    return {
      orders: [],
      currentUser: {
        username: '',
        email: '',
      }
    }
  },
  mounted() {
    document.title = 'My account | TeaShop'

    this.getMyOrders()
    this.getMyDetails()

  },
  methods: {
    logout() {
      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem('token')
      localStorage.removeItem('cart')

      this.$store.commit('removeToken')
      this.$store.commit('clearCart')

      this.$router.push('/')
    },
    async getMyDetails() {
      this.$store.commit('setIsLoading', true)

      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token

      await axios
          .get('/api/v1/current-user/')
          .then(response => {
            this.currentUser = response.data
            console.log(response.data)
          })
          .catch(error => {
             console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    },
    async getMyOrders() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/orders/')
          .then(response => {
            this.orders = response.data
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    }
  },
}
</script>

<style scoped>
.page-my-account {
  min-height: 25vw;
}
</style>