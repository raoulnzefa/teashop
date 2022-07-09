<template>

      <div class="product-column column is-3 mb-2">

        <router-link :to="product.get_absolute_url">
        <div class="product-box box" style="background: #92ddc8">

          <figure class="image mb-4">
            <img style="height: 40vh" :src="product.get_thumbnail">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <h4 class="is-size-4"><strong>{{ product.price }}€</strong></h4>

        </div>
        </router-link>

      </div>

</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object
  }
}
</script>

<style lang="scss" scoped>
$primary-color: #3EB489;
$secondary-color: #92ddc8;

.product-column {
  background:$primary-color;
}

.product-box {
  background:$secondary-color;
}

.image {
  margin: -1.25rem -1.25rem 0 -1.25rem ;
}

.box {
  min-height: 100%;
}

h3 {
  display: inline;
}

h4 {
  display: inline-block;
  margin-left: 1em;
}

</style>