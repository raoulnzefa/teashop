<template>

  <div class="home">
    <div class="parallax mb-6">
      <div class="caption">
        <span class="caption-span">
          Quality of Tea
        </span>
      </div>
    </div>

    <div class="our-products box box-green-prm columns is-multiline">
      <div class="title-box box column is-12">
        <h1 class="is-size-2-desktop is-size-4-mobile has-text-centered">
           Thessa<i class="fa-solid fa-trademark"></i>
        </h1>
      </div>

      <div class="column is-6">
          <Delivery style="width: 100%; height: 80%" />
      </div>

      <div class="column is-6">
        <dl class="content is-flex is-flex-direction-column">

          <div class="info-item">
            <dt><i class="fa-solid fa-mortar-pestle"></i> The perfect mix</dt>
            <dd>We use the recipes of ancient natives, thanks to which our products not only taste delicious,
              but also provide many valuable ingredients and vitamins for the proper functioning of the body.
            </dd>
          </div>

          <div class="info-item mt-4">
            <dt><i class="fa-solid fa-earth-americas"></i> Straight from origin</dt>
            <dd>Our Thessa<i class="fa-solid fa-trademark"></i> is produced on plantations in many South American countries.
              They are confirmed with the eco certificate. Always fresh with beautifully smell.
            </dd>
          </div>

          <div class="info-item">
            <dt><i class="fa-solid fa-spa"></i> Special varieties</dt>
            <dd>We offer some special herbs and teas with remarkable healing, calming and energizing properties.
              Try it out and leave a review for others to know what to expect!
            </dd>
          </div>

          <div class="info-item">
            <dt><i class="fa-solid fa-clock"></i> 48h</dt>
            <dd>Always on the time. Delivery to your house or delivery point is maximum 48h.
            </dd>
          </div>

        </dl>
      </div>

    </div>

    <div class="box new-products">
      <div class="columns is-multiline">
        
        <div class="box title-box column is-12">
          <h2 class="is-size-2-desktop is-size-4-mobile has-text-centered" style="color: white">
            <i class="fa-solid fa-ranking-star"></i> New assortment for you!</h2>
        </div>
  
        <ProductBox v-for="product in latestProducts" :key="product.id" :product="product" />
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

import Delivery from "@/components/Delivery";
import ProductBox from "@/components/ProductBox";


export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox,
    Delivery
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home ' + '| TeaShop'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/latest-products/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style lang="scss" scoped>
$primary-color: #3EB489;
$secondary-color: #92ddc8;
$third: #059461;


.info-item {
  margin-bottom: 3rem;

  dt {
    font-size: 2rem;
    font-weight: 600;
  }

  dd {
    font-size: 1.25rem;
  }
}

.title-box {
  text-align: center;
  background: $third;

  h1 {
    color: white!important;
  }
}

.new-products {
  background: $primary-color;
}


.parallax {
  background-image: url('~@/assets/tea-plantation.jpg');

  min-height: 50vh;

  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.caption {
  position: absolute;
  left: 0;
  top: 35%;
  width: 100%;
  text-align: center;
  color: #000;
}
.caption span.caption-span {
  background-color: rgba(152,152,156,0.6);
  color: #fff;
  padding: 18px;
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: 10px;
}
</style>