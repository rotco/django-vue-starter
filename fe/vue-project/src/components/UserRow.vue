<template>
  <tr>
    <td v-if="!filters?.date">{{ formatDate(user.date) }}</td>
    <td v-if="!filters?.name">{{ user.name }}</td>
    <td v-if="!filters?.address">{{ user.address }}</td>
    <td v-if="locationId == 'tableWithActions'" @click="omitDeleteUser">
      <img
        src="../assets/3844460_can_trash_icon.png"
        alt="TrashIcon"
        style="width: 24px; height: 24px"
      />
    </td>
  </tr>
</template>

<script>
import moment from "moment";

export default {
  props: ["user", "filters", "locationId", "deleteUser"],
  methods: {
    omitDeleteUser() {
      this.$emit("deleteUser", this.user);
      console.log("omitDeleteUser", this.user);
    },
    formatDate(date) {
      return moment(date).format("YYYY-MM-DD");
    },
  },
};
</script>

<style></style>
