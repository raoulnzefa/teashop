<template>
  <tr>
    <td>
      <router-link :to="item.product.get_absolute_url">
        <img class="product-card-image" alt="product card image" :src="item.product.get_thumbnail">
      </router-link>
    </td>

    <td>
      {{ item.product.price }}€
    </td>

    <td>

      {{ item.quantity }}
      <a @click="decrementQuantity(item)" style="margin:0 1rem 0">
        <strong>-</strong>
      </a>
      <a @click="incrementQuantity(item)">
        <strong>+</strong>
      </a>

    </td>

    <td><strong>{{ getItemTotal(item).toFixed(2) }}€</strong></td>

    <td><button class="delete" @click="removeFromCart(item)"></button></td>
  </tr>

</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object
  },
  data() {
    return {
      item: this.initialItem
    }
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },

    decrementQuantity(item) {
      item.quantity -= 1

      if (item.quantity === 0) {
        this.$emit('removeFromCart', item)
      }

      this.updateCart()
    },

    incrementQuantity(item) {
      item.quantity += 1

      this.updateCart()
    },

    updateCart() {
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    },

    removeFromCart(item) {
      this.$emit('removeFromCart', item)

      this.updateCart()
    },


  },
}
</script>

<style scoped>
.product-card-image {
  width: 14vw;
}
</style>