<template>
  <div>
    <h4>Experience:</h4>
    <div v-for="exp in experience" :key="exp">{{ exp }}</div>
  </div>
</template>

<script>
export default {
  props: ["experience"],
};
</script>

<style></style>
