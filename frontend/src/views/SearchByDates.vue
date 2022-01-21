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
    <v-row>
        <v-col cols="6">
            <v-alert v-if="errorDates" dense type="error"> La fecha de inicio debe ser menor que la fecha de término.
    </v-alert>
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
                            <v-chip class="mx-2" color="primary"> {{statistics.mag[0]}} </v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success"> {{statistics.mag[1] }}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange"> {{statistics.mag[2] }}</v-chip>
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
                            <v-chip class="mx-2" color="primary">{{statistics.gap[0]}}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">{{statistics.gap[1]}}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">{{statistics.gap[2]}}</v-chip>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>

        </v-col>

        <v-col cols="12" md="3">
            <v-card elevation="1">
                <v-card-title>Aceleración Sísmica</v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item>
                            Promedio:
                            <v-chip class="mx-2" color="primary">{{statistics.rms[0]}}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">{{statistics.rms[1]}}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">{{statistics.rms[2]}}</v-chip>
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
                            <v-chip class="mx-2" color="primary">{{statistics.sig[0]}}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Mediana:
                            <v-chip class="mx-2" color="success">{{statistics.sig[1]}}</v-chip>
                        </v-list-item>
                        <v-list-item>
                            Moda:
                            <v-chip class="mx-2" color="orange">{{statistics.sig[2]}}</v-chip>
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
                    text: "Código",
                    value: "code"
                },
                {
                    text: "Magnitud",
                    value: "mag"
                },
                {
                    text: "Lugar",
                    value: "place"
                },
                {
                    text: "Dmin",
                    value: "dmin"
                },
                {
                    text: "Gap",
                    value: "gap"
                },
                {
                    text: "RMS",
                    value: "rms"
                },
                {
                    text: "SIG",
                    value: "sig"
                },

                {
                    text: "Fecha",
                    value: "time"
                },
            ],
            statistics: [],
            errorDates: false,
        }
    },

    methods: {

        search() {
            if (this.dateSince >= this.dateUntil) {
                console.log("date since es mayor que until")
                this.errorDates = true;
            } else {
                console.log("estan bien")
                this.errorDates = false;
            }
            console.log("searching...");
            this.isLoading = true;
            let url_backend = "http://localhost:5000";
            let endpoint = "/terremotos";
            axios.get(url_backend + endpoint, {
                    params: {
                        starttime: this.dateSince,
                        endtime: this.dateUntil
                    }
                })
                .then(response => {
                    this.earthquakes = response.data.terremotos;
                    this.earthquakes.forEach(e => {
                        let date = new Date(e.time);
                        var dateStr =
                            ("00" + (date.getMonth() + 1)).slice(-2) + "/" +
                            ("00" + date.getDate()).slice(-2) + "/" +
                            date.getFullYear() + " " +
                            ("00" + date.getHours()).slice(-2) + ":" +
                            ("00" + date.getMinutes()).slice(-2) + ":" +
                            ("00" + date.getSeconds()).slice(-2);
                        e.time = dateStr;
                    })
                    this.statistics = response.data.estadisticas;
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
