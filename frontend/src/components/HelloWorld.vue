<template>
<v-container>
    <v-row class="text-center">
        <v-col cols="12">
            <v-img :src="require('../assets/terremoto.png')" class="my-3" contain height="200" />
        </v-col>

        <v-col cols="12" class="mb-4">
            <h1 class="display-2 font-weight-bold mb-3">
                Bienvenido a la App de Terremotos
            </h1>

            <p class="subheading font-weight-regular">
                En esta aplicación encontrarás información y datos de terremotos
                <br>ocurridos al rededor de todo el mundo.
            </p>
        </v-col>

        <v-col cols="4">
            <v-btn block class="mx-3 green lighten-1" @click="redirectToLatestEarthquakes()">
                Ver ultimos terremotos
            </v-btn>
        </v-col>
        <v-col cols="4">
            <v-btn block class="mx-3 green lighten-1" @click="redirectToSearchByCountry()">
                Buscar terremotos en un país
            </v-btn>
        </v-col>
        <v-col cols="4">
            <v-btn block class="mx-3 green lighten-1" @click="redirectToSearchByDate()">
                Buscar terremotos por fecha
            </v-btn>
        </v-col>

    </v-row>
</v-container>
</template>

<script>
export default {
    name: 'HelloWorld',

    data: () => ({

    }),

    methods: {
        redirectToSearchByCountry() {
            console.log("redirecting to search by country...");
            window.location.href = "/#/search-by-country";
        },

        redirectToLatestEarthquakes() {
            console.log("redirecting to latest earthquakes...");
            window.location.href = "/#/latest";
        },

        redirectToSearchByDate() {
            console.log("redirecting to search by date...");
            window.location.href = "/#/search-by-dates";
        }
    }
}
</script>
