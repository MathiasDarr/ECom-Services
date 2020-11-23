<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
            <v-card  tile flat>
            
            <v-card-title>Event Driven Microservices Kafka & Spring Boot Project</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            
            <h3>Project Discription</h3>
            <p class="title font-weight-light">

                In this project I play around with an envent driven microservices architecture, using Kafka as a message broker
                for communicating between microservices.  
      

            </p>
              <h3> Motivation </h3>
            <p class="title font-weight-light">
                It seems as though Ecommerce systems often utilize an event driven archtiecture.   
            </p>
            <h3> Technologies Used </h3>
            
            <ul class="title font-weight-light">
              <li>
                Kafka Streams & Avro Serialization
              </li>

              <li>
                Spring Boot & String Kafka Streams Binder
              </li>
              <li>
                DynamoDB
              </li>
            </ul>

            <v-divider></v-divider>     
            <span>
 
            </span>
            <v-layout>
                <v-flex md1>
                    <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/github.png'" height="60px" width="60"></v-img>
                </v-flex>
                <v-flex md8>
                    <p class="title font-weight-medium">
                    Github Links
                    </p>
                    <p class="title font-weight-light">   
                        <a href="https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-events">Event Driven Microservices </a> 
          
                    </p>
                </v-flex>
            </v-layout>

            



            </v-card-text>
          </v-card>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>

import BaseNavBar from  '../BaseNavBar'

export default {
    components:{
        BaseNavBar
    },
    data(){

        return {
            items: [
                { title: 'Microservices Project', icon: 'mdi-view-dashboard', route:'/ecommerce' },
                { title: 'Ecommerce Store', icon: 'mdi-image', route:'/storefront' },
                { title: 'Shopping Cart', icon: 'mdi-image', route:'/cart' },
          ],
        }
    }



}
</script>