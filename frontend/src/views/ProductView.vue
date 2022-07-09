<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-4">
        <figure class="image mb-3">
          <img alt="product image" style="width: 100%" :src="product.get_image">
        </figure>
      </div>
      <div class="column is-8 is-flex is-justify-content-flex-start is-flex-direction-column">
        <h1 class="box title is-size-1 product-name">{{ product.name }}</h1>

        <p class="is-size-4 mb-3"> {{ product.description }} </p>

        <p class="is-size-3"><strong>{{ product.price }}€</strong></p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>

          <div class="control">
            <a class="button button-green-prm" @click="addToCart">Add to cart</a>
          </div>
        </div>

      </div>
    </div>

    <div class="review mb-3 review-box box box-green-prm">

      <div class="review-box box box-green-prm is-flex is-justify-content-space-between is-align-items-baseline">
        Reviews
        <a class="add-review-button" aria-expanded="false" data-target="add-review" @click="showAddComment = !showAddComment">
          <i class="fa-solid fa-plus fa-xl"></i>
        </a>
      </div>

      <div id="add-review" class="add-review" v-if="showAddComment">
        <form @submit.prevent="submitForm">
          <div class="field has-addons">

            <div class="control" style="width: 80%">
              <textarea class="textarea" v-model="commentBody"></textarea>
            </div>

            <div class="control">
              <button  style="height: 100%" class="button button-add-comment"><i class="fa-solid fa-paper-plane fa-2x"></i></button>
            </div>

          </div>
        </form>
      </div>
    </div>
     <CommentBox
         v-for="comment in product.comments"
         :key="comment.id"
         :comment="comment"
     />

  </div>

</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast'
import CommentBox from "@/components/CommentBox";

export default {
  name: 'Product',
  data() {
    return {
      product: {
        comments: []
      },
      quantity: 1,

      commentBody: '',
      showAddComment: false
    }
  },
  components: {
    CommentBox
  },
  mounted() {
    this.getProduct()
  },
  methods: {
    submitForm() {
      const product_slug = this.$route.params.product_slug

      const formData = {
        body: this.commentBody
      }

      axios
          .post(`/api/v1/comments/${product_slug}/`, formData)
          .then(response => {
            toast({
              message: 'Comment added',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'top-center'
            })
            window.location.reload()
          })
          .catch(error => {
            console.log(error)
          })
    },

    async getProduct() {
      this.$store.commit('setIsLoading', true)

      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug

      await axios
          .get(`/api/v1/products/${category_slug}/${product_slug}`)
          .then(response => {
            this.product = response.data

            document.title = this.product.name + ' | TeaShop'
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }

      const item = {
        product: this.product,
        quantity: this.quantity
      }

      this.$store.commit('addToCart', item)

      toast({
        message: 'The product was added to the cart',
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'top-center'
      })
    }
  }
}
</script>

<style lang="scss" scoped>

$primary-color: #3EB489;
$secondary-color: #92ddc8;
$third: #059461;

.add-review-button {
  color: white!important;
  background: $third;
  padding: 1rem;
  border-radius: 50%;
}

.button-add-comment {
  background: $secondary-color;
  color: white;
}

.product-name {
  background: $primary-color;
  color: white;
}

.image img {
  width: 50%;
  height: 30%
}


.review-box {
  font-size: 1.5rem;
  font-weight: 700;
}

</style>
