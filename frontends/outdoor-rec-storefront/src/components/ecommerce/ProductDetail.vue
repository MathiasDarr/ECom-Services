<template>
  <v-container>
    <v-layout row>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md10>
        <v-card flat>
          <v-card tile flat >
          
          <v-card-text> <h1>{{ productName }} </h1> </v-card-text>
          
  
          <v-card-text>
            <h3> $ {{ price }} </h3>
          </v-card-text>
        </v-card>           
                  
        <v-btn rounded class="error mt4" @click="addToCart()" > Add to Cart </v-btn>
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>


<script>



      // <v-flex md10>




      // </v-flex>

import BaseNavBar from '../BaseNavBar'

import { mapActions } from "vuex";
import router from '../../router'
export default {
    components:{
      BaseNavBar
    },
    created(){
        this.id = this.$route.params.id
        console.log('The id is: ' + this.$route.params.id);
        this.addDeleteItem({id:this.id,quantity: 1})
    },

    data () {
     return {
       
       productName: "Atmos 65",
       price:"180.00",
       id: this.$route.params.id,
       quantity:1,
       
       items: [
          { title: 'Microservices Project Description', icon: 'mdi-view-dashboard', route:'/ecommerce' }, 
          { title: 'Ecommerce Store', icon: 'mdi-image', route:'/storefront' },
          { title: 'Shopping Cart', icon: 'mdi-image', route:'/cart' },
        ],
       
     }
  },
  methods:{
    ...mapActions(["addDeleteItem"]),
    addToCart(){
      this.addDeleteItem(this.id, this.quantity)
    },
    selectRoute(route){ // eslint-disable-line no-unused-vars
          router.push(route).catch(err => err)
    }
    
  }


}
</script>