<template>
  <div id="app">
    <StopWatch />
  </div>
</template>

<script>
import StopWatch from './components/StopWatch.vue'

export default {
  name: 'App',
  components: {
    StopWatch
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
