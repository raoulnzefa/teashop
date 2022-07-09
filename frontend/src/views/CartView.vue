<template>

  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="box column is-12 cart-name">
        <h1 class="title has-text-centered"><i class="fas fa-solid fa-basket-shopping"></i> Cart</h1>
      </div>

      <div class="column is-12 box">

        <table class="table is-fullwidth" v-if="cartTotalLength">
          <thead>
          <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
          </tr>
          </thead>

          <tbody>
          <CartItem
            v-for="item in cart.items"
            :key="item.product.id"
            :initialItem="item"
            v-on:removeFromCart="removeFromCart"
          />
          </tbody>
        </table>

        <p v-else>You don't have any products in your cart...</p>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle"><strong>Summary</strong></h2>

        <strong>{{ cartTotalPrice.toFixed(2) }}€ </strong> | Items in cart: {{ cartTotalLength }}

        <hr>

        <router-link to="/cart/checkout" class="button button-green-prm">Proceed to checkout</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CartItem from "@/components/CartItem";
export default {
  name: "CartView",
  components: {
    CartItem
  },
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
    }
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.product.price * curVal.quantity
      }, 0)
    }
  }
}
</script>

<style lang="scss" scoped>

$primary-color: #3EB489;
$secondary-color: #92ddc8;

.cart-name {
  background:$primary-color;
}

.title {
  color: white;
  font-weight: 700;
}

.page-cart {
  min-height: 25vw;
}
</style>