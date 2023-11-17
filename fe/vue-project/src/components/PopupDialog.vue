<template>
  <div class="popup">
    <div>
      <div class="popup-header">{{ header }}</div>
      <div class="popup-text">{{ text }}</div>
      <div v-for="(value, key, index) in form" :key="index">
        <label>{{ key }}</label>
        <input type="text" v-model="form[key]" />
      </div>
      <div class="popup-buttons">
        <input
          class="cancel-button"
          @click="$emit('closeDialog')"
          value="Cancel"
          type="button"
        />
        <input
          class="submit-button"
          @click="$emit('handleConfirm')"
          value="Confirm"
          type="button"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["header", "text", "form"],
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
