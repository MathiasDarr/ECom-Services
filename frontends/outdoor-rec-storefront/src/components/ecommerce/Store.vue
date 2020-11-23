<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md10>
        <v-card flat>
          <ProductList />
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>

import BaseNavBar from '../BaseNavBar'
import { mapGetters, mapActions } from "vuex";
import ProductList from './ProductList'

export default {
    components:{
        BaseNavBar,
        ProductList
    },

    methods:{
        ...mapActions(["fetchProducts"]),
    },
    computed: {
        ...mapGetters(["allProducts"]),
    },
    created(){
      this.fetchProducts();
    },

    data(){

        return {
            items: [
                { title: 'Ecommerce Store', icon: 'mdi-image', route:'/storefront' },
                { title: 'Shopping Cart', icon: 'mdi-image', route:'/cart' },

          ],
        }
    }
}
</script>