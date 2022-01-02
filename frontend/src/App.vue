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

        <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
                <v-btn text dark v-bind="attrs" v-on="on">
            <v-icon class="mr-1">mdi-magnify</v-icon>
            <span class="mr-2">Buscar por</span>
                </v-btn>
            </template>
            <v-list>
                <v-list-item >
                    <v-list-item-title>País</v-list-item-title>
                </v-list-item>
                <v-list-item>
                    <v-list-item-title>Fecha</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>

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
