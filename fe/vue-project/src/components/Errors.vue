<template>
  <div class="popup">
    <div class="popup-header" style="color: red">Errors:</div>
    <div class="errors-container">
      <div class="errors-text">
        <div
          style="margin-bottom: 20px"
          v-for="(values, key, index) in errors"
          :key="index"
        >
          <span style="font-size: large">{{ key }}:</span>
          <li v-for="value in values" :key="value">{{ value }}</li>
        </div>
      </div>
    </div>

    <div class="popup-buttons">
      <input
        class="submit-button"
        type="button"
        value="Close"
        @click="$emit('closeErrors')"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: ["errors"],
};
</script>

<style scoped>
.errors-container {
  display: table;
  margin-left: auto;
  margin-right: auto;
}
.errors-text {
  display: flex;
  flex-direction: column;
}
</style>
