<template>
  <div class="popup">
    <h3>Errors:</h3>
    <div v-for="(values, key, index) in errors" :key="index">
      {{ key }}:
      <div v-for="value in values" :key="value">{{ value }}</div>
    </div>
    <input type="button" value="Close" @click="$emit('closeErrors')" />
  </div>
</template>

<script>
export default {
  props: ["errors"],
};
</script>

<style>
.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
  z-index: 1;
  background-color: #fff;
  padding: 50px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}
</style>
