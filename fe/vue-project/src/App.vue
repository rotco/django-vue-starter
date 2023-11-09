<script setup>
import { RouterLink, RouterView } from "vue-router";
import Home from "./views/Home.vue";
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav>
  <div>
    <RouterView />
  </div>
</template>

<style scoped>
nav {
  display: flex;
  gap: 10px;
}
</style>
