<template>
  <div class="box mb-4">
    <h3 class="is-size-4 mb-6">
      Order #{{ order.id }}
    </h3>

    <h4 class="is-size-5">
      Products
    </h4>

    <table class="table is-fullwidth">
      <thead>
      <tr>
        <th>Product</th>
        <th>Price</th>
        <th>Qty</th>
        <th>Total</th>
      </tr>
      </thead>

      <tbody>
      <tr
          v-for="item in order.items"
          :key="item.product.id"
      >
        <td style="width: 30%">{{ item.product.name }}</td>
        <td style="width: 20%">{{ item.product.price }}€</td>
        <td style="width: 20%">{{ item.quantity }}</td>
        <td style="width: 30%">{{ getItemTotal(item).toFixed(2) }}€</td>
      </tr>
      </tbody>
    </table>
  </div>

</template>

<script>
export default {
  name: "OrderSummary",
  props: {
    order: Object
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    orderTotalLength(order) {
      return order.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
  }
}
</script>

<style scoped>

</style>