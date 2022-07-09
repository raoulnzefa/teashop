<template>
  <div id="wrapper">
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong style="font-family: 'Titillium Web', sans-serif; color: white">
            Tea Shop
          </strong>
          <span style="color: white">
            <i class="fa-solid fa-leaf"></i>
          </span>
        </router-link>

        <a class="navbar-burger" aria-label="menu" style="color: white" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">

        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Tea?" name="query">
                </div>

                <div class="control">
                  <button class="button" style="background: inherit; border: none; color: white">
                    <span class="icon">
                      <i class="fas fa-search fa-xl"></i>
                    </span>
                  </button>
                </div>

              </div>
            </form>
          </div>
        </div>


        <div class="navbar-end">


          <div class="dropdown is-hoverable mr-5">
            <div class="dropdown-trigger">
              <button id="categoriesDropdown" class="button" aria-haspopup="true" aria-controls="dropdown-menu4">
                <span>Categories</span>
                <span class="icon is-small">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu4" role="menu">
              <div class="dropdown-content">
                <div v-for="category in categories" class="dropdown-item">
                  <router-link :to="`${category.get_absolute_url}`">
                    <p style="color: white!important; font-size: 1.1rem; font-weight: 600">{{ category.name }}</p>
                  </router-link>
                </div>
              </div>
            </div>
          </div>



          <div class="navbar-item mr-5">
            <template v-if="$store.state.isAuthenticated">
              <router-link to="/my-account">
                <p><i class="fa-solid fa-user fa-lg" style="color: white"></i></p>
              </router-link>
            </template>

            <template v-else>
              <router-link to="/log-in">
                <i class="fa-solid fa-user fa-lg" style="color: white"></i>
              </router-link>
            </template>
          </div>

          <div id="shoppingCart" class="navbar-item">
            <router-link to="/cart">
              <span class="icon"><i class="fas fa-solid fa-basket-shopping mr-3 fa-xl" style="color: white;"></i></span>
              <span style="text-decoration: none; color: white; font-weight: 600">{{ cartTotalPrice }}€</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <div class="empty-container"></div>

    <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading }">
      <div class="loading-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <div class="columns is-multiline">

        <div class="footer-field column is-6 has-text-centered is-flex is-flex-direction-column">
          <a href="#"><i class="fa-solid fa-circle-question"></i> Questions and answers</a>
          <a href="#"><i class="fa-solid fa-truck"></i> Delivery details</a>
          <a href="#"><i class="fa-solid fa-phone"></i> Contact</a>

        </div>

        <div class="footer-field column is-6 has-text-centered is-flex is-flex-direction-column">
          <a href="#"><i class="fa-solid fa-building"></i> For enterprises</a>
          <a href="#"><i class="fa-solid fa-truck-ramp-box"></i> Returns</a>
          <a href="#"><i class="fa-solid fa-bell"></i> Newsletter</a>
        </div>

        <div class="copyright column is-12 has-text-centered">
          <strong style="font-family: 'Titillium Web', sans-serif; color: white">
            Tea Shop
          </strong>
          <span style="color: white">
            <i class="fa-solid fa-leaf"></i>
          </span>
        </div>

        <div class="copyright column is-12 has-text-centered">
          <p>Copyright (c) 2022 Kacper Krasnodebski</p>
        </div>

      </div>

    </footer>

  </div>
</template>

<script>
import axios from "axios";


export default {
  components: {},

  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
      categories: []
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    this.getCategories()
  },
  methods: {
    async getCategories() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/categories/')
          .then(response => {
            this.categories = (response.data)
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    }
  },
  computed: {

    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    },

    cartTotalPrice() {
      let totalPrice = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalPrice += this.cart.items[i].quantity * this.cart.items[i].product.price
      }
      return totalPrice
    }
  },
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

$primary-color: #3EB489;
$secondary-color: #92ddc8;

.button-green-prm {
  background: $primary-color;
  border: none;
  color: white!important;
  font-weight: 600;
}

.box-green-prm {
  background: $primary-color;
  color: white;
}

.footer {
  background: #3EB489!important;
  margin-top: 3rem;

  .copyright {
  font-size: 1rem;
  font-weight: 600;
  color: white!important;
  }

  .footer-field {
    a {
      font-size: clamp(0.5rem, 10vw, 1.3rem);
      font-weight: 600;
      color: white!important;
      text-decoration: none!important;
    }
  }
}

body {
  background: $secondary-color ;
}


.dropdown-menu {
  background: $primary-color;
}

.dropdown-content {
  background: $primary-color;
}

.navbar-end {
   .navbar-item {
    margin-right:0.75rem;
  }
}

.empty-container {
  min-height: 5vh;
}

.is-active {
  .navbar-end {
    .navbar-item {
      display: inline-block;
    }
  }
}

@media (min-width: 800px) {
  .dropdown {
    padding-top: 0.28rem;
  }
}

.navbar-menu {
  background: $primary-color;
}

.navbar-brand {
  font-size: 1.5rem;
  letter-spacing: 0.1em;
}

.navbar {
  background: $primary-color; //#36F57F
  position: fixed;
  width: 100%;
}

#categoriesDropdown {
  border: none;
  background: $primary-color;
  color: white;
  font-size: 1.25rem;
  font-weight: 600;
}


.loading-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.loading-dual-ring:after {
  content: "";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: loading-dual-ring 1.2s linear infinite;
}

@keyframes loading-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}


</style>
