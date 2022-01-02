<template>
<v-container>
    <v-row class="my-2">
        <v-col>
            <div class="text-h2">Buscar por Fechas</div>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="12" sm="6" md="4">
            <v-menu v-model="menu1" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
                <template v-slot:activator="{ on, attrs }">
                    <v-text-field v-model="dateSince" label="Desde" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="dateSince" @input="menu1 = false"></v-date-picker>
            </v-menu>
        </v-col>

        <v-col cols="12" sm="6" md="4">
            <v-menu v-model="menu2" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
                <template v-slot:activator="{ on, attrs }">
                    <v-text-field v-model="dateUntil" label="Hasta" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="dateUntil" @input="menu2 = false"></v-date-picker>
            </v-menu>
        </v-col>

        <v-col cols="12" sm="6" md="1" offset-md="3">
            <v-btn class="green lighten-2" @click="search()">Buscar</v-btn>
        </v-col>
    </v-row>

    <v-row v-if="isLoading">
        <v-col v-for="i in 4" cols="12" sm="6" md="3" :key="i">
            <v-skeleton-loader class="mx-auto" max-width="300" type="card"></v-skeleton-loader>
        </v-col>
    </v-row>

    <v-row v-if="earthquakes.length > 0">
        <v-col cols="12" md="3">
            <v-card elevation="1">
                <v-card-title>Magnitud</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item>
                            Promedio:
                            <v-chip class="mx-2" color="primary">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">%</v-chip>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>

        </v-col>

        <v-col cols="12" md="3">
            <v-card elevation="1">
                <v-card-title>GAP</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item>
                            Promedio:
                            <v-chip class="mx-2" color="primary">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">%</v-chip>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>

        </v-col>

        <v-col cols="12" md="3">
            <v-card elevation="1">
                <v-card-title>RMS</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item>
                            Promedio:
                            <v-chip class="mx-2" color="primary">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">%</v-chip>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>

        </v-col>

        <v-col cols="12" md="3">
            <v-card elevation="1">
                <v-card-title>SIG</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item>
                            Promedio:
                            <v-chip class="mx-2" color="primary">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">%</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">%</v-chip>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>

        </v-col>
    </v-row>

    <v-row>
        <v-col cols="12">
            <v-data-table :headers="headers" :items="earthquakes" :items-per-page="8" class="elevation-1"></v-data-table>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: "SearchByDates",
    data: () => {
        return {
            earthquakes: [],
            isLoading: false,
            dateUntil: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            dateSince: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            menu1: false,
            menu2: false,
            headers: [{
                    text: 'Dessert (100g serving)',
                    align: 'start',
                    sortable: false,
                    value: 'name',
                },
                {
                    text: 'Calories',
                    value: 'calories'
                },
                {
                    text: 'Fat (g)',
                    value: 'fat'
                },
                {
                    text: 'Carbs (g)',
                    value: 'carbs'
                },
                {
                    text: 'Protein (g)',
                    value: 'protein'
                },
                {
                    text: 'Iron (%)',
                    value: 'iron'
                },
            ],
            desserts: [{
                    name: 'Frozen Yogurt',
                    calories: 159,
                    fat: 6.0,
                    carbs: 24,
                    protein: 4.0,
                    iron: '1%',
                },
                {
                    name: 'Ice cream sandwich',
                    calories: 237,
                    fat: 9.0,
                    carbs: 37,
                    protein: 4.3,
                    iron: '1%',
                },
                {
                    name: 'Eclair',
                    calories: 262,
                    fat: 16.0,
                    carbs: 23,
                    protein: 6.0,
                    iron: '7%',
                },
                {
                    name: 'Cupcake',
                    calories: 305,
                    fat: 3.7,
                    carbs: 67,
                    protein: 4.3,
                    iron: '8%',
                },
                {
                    name: 'Gingerbread',
                    calories: 356,
                    fat: 16.0,
                    carbs: 49,
                    protein: 3.9,
                    iron: '16%',
                },
                {
                    name: 'Jelly bean',
                    calories: 375,
                    fat: 0.0,
                    carbs: 94,
                    protein: 0.0,
                    iron: '0%',
                },
                {
                    name: 'Lollipop',
                    calories: 392,
                    fat: 0.2,
                    carbs: 98,
                    protein: 0,
                    iron: '2%',
                },
                {
                    name: 'Honeycomb',
                    calories: 408,
                    fat: 3.2,
                    carbs: 87,
                    protein: 6.5,
                    iron: '45%',
                },
                {
                    name: 'Donut',
                    calories: 452,
                    fat: 25.0,
                    carbs: 51,
                    protein: 4.9,
                    iron: '22%',
                },
                {
                    name: 'KitKat',
                    calories: 518,
                    fat: 26.0,
                    carbs: 65,
                    protein: 7,
                    iron: '6%',
                },
            ],
        }
    },

    methods: {

        search() {
            console.log("searching...");
            this.isLoading = true;
            let url_backend = "http://localhost:5000";
            let endpoint = "/terremotos/";
            axios.get(url_backend + endpoint, {
                    params: {
                        since: this.dateSince,
                        until: this.dateUntil
                    }
                })
                .then(response => {
                    this.earthquakes = response.data;
                    this.isLoading = false;
                })
                .catch(error => {
                    console.log(error);
                    this.isLoading = false;
                })
        },

        formatDate(date) {
            if (!date) return null

            const [year, month, day] = date.split('-')
            return `${month}/${day}/${year}`
        },
        parseDate(date) {
            if (!date) return null

            const [month, day, year] = date.split('/')
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        },
    },
}
</script>
