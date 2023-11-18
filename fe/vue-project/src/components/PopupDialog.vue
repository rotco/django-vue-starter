<template>
  <div class="popup">
    <div>
      <div class="popup-header">
        <div>{{ header }}</div>
        <img
          src="../assets/close_icon.png"
          alt="TrashIcon"
          style="width: 10px; height: 10px"
          @click="$emit('closeDialog')"
        />
      </div>
      <div class="popup-body">
        {{ text }}
        <div>
          <div
            class="popup-inputs"
            v-for="(value, key, index) in form"
            :key="index"
          >
            <label style="text-transform: capitalize">{{ key }}</label>
            <input class="text-input" type="text" v-model="form[key]" />
          </div>
        </div>
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
  z-index: 1;
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  min-width: 60%;
}

.popup-header {
  display: flex;
  justify-content: space-between;
  font-size: larger;
  color: grey;
}
.popup-body {
  text-align: center;
  display: flex;
  justify-content: center;
}
.popup-buttons {
  display: flex;
  justify-content: right;
}
.popup-inputs {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px;
}
.text-input {
  width: 400px;
}
</style>
