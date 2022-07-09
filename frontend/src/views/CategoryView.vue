<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="box column is-12 category-name">
        <h2 class="is-size-2 has-text-centered has-text-light" style="font-weight: 700; letter-spacing: 0.1rem">{{ category.name }}</h2>
      </div>
      <ProductBox
        v-for="product in category.products"
        :key="product.id"
        :product="product" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ProductBox from "@/components/ProductBox";

export default {
  name: 'Category',
  data() {
    return {
      category: {
        products: []
      }
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getCategory()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'category') {
        this.getCategory()
      }
    }
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug

      this.$store.commit('setIsLoading', true)

      await axios
          .get(`/api/v1/products/${categorySlug}/`)
          .then(response => {
            this.category = response.data

            document.title = this.category.name + ' | TeaShop'
          })
          .catch(error => {
            console.log(error)
            toast({
                message: 'Something went wrong. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'top-center'
            })
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style lang="scss">
$primary-color: #3EB489;
$secondary-color: #92ddc8;

.category-name {
  background:$primary-color;
}

.page-category {
  min-height: 25vw;
}

</style>