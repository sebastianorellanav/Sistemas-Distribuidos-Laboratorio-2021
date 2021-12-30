<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/terremoto.png" style="height:400px">
    <HelloWorld msg="Bienvenido a la App de Terremotos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
