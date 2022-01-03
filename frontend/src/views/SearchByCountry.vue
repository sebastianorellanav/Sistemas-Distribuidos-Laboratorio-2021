<template>
<v-container>
    <v-row class="my-2">
        <div class="text-h2">Buscar por País</div>
    </v-row>

    <v-row>
        <v-col cols="12" sm="6" md="4">
            <v-autocomplete clearable :items="countries" placeholder="Selecciona o escribe un país" v-model="inputCountry"></v-autocomplete>
        </v-col>
        <v-col cols="12" sm="6" md="1" offset-md="7">
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
            <v-data-table :headers="headers" :items="earthquakes" :loading="isLoading" :items-per-page="8" class="elevation-1"></v-data-table>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: "SearchByCountry",
    data: () => {
        return {
            inputCountry: "",
            countries: ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"],
            rules: [
                value => !!value || 'Requerido',
            ],
            earthquakes: [],
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
            isLoading: false,
            statistics: []
        }
    },

    methods: {
        search() {
            this.isLoading = true;
            let url_backend = "http://localhost:5000";
            let endpoint = "/terremotos/";
            console.log("searching...");
            console.log(url_backend + endpoint + this.inputCountry);
            axios.get(url_backend + endpoint + this.inputCountry)
                .then(response => {
                    this.earthquakes = response.data.terremotos;
                    this.statistics = response.data.estadisticas;
                    this.isLoading = false;
                })
                .catch(error => {
                    console.log(error);
                    this.isLoading = false;
                })
        }
    }
}
</script>
