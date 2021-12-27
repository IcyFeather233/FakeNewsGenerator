<template>
  <div id="app">
    <img src="./assets/scumaker_logo.png" style="width: 10%; height: auto">
    <h1 style="text-align: center">SCU Maker新闻稿生成器</h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
