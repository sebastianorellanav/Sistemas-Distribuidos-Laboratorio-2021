<template>
<v-app>
    <v-app-bar app class="green darken-4" dark>
        <div class="d-flex align-center">
            <v-img alt="terremoto-app Logo" class="shrink mr-2" contain src="./assets/terremoto.png" transition="scale-transition" width="40" />

            <h2>TERREMOTO-APP</h2>
        </div>

        <v-spacer></v-spacer>

        <v-btn href="/" text>
            <v-icon class="mr-1">mdi-home</v-icon>
            <span class="mr-2">Inicio</span>
        </v-btn>
        <v-btn href="/#/latest" text>
            <v-icon class="mr-1">mdi-alarm</v-icon>
            <span class="mr-2">Últimos terremotos</span>
        </v-btn>

    </v-app-bar>

    <v-main>
        <router-view />
    </v-main>
</v-app>
</template>

<script>
export default {
    name: 'App',

    data: () => ({
        //
    }),
};
</script>
