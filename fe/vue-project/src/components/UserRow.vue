<template>
  <tr>
    <td v-if="!filters?.date">{{ user.date }}</td>
    <td v-if="!filters?.name">{{ user.name }}</td>
    <td v-if="!filters?.address">{{ user.address }}</td>
    <td v-if="locationId == 'tableWithActions'" @click="deleteUser">
      <img src="../assets/trash32x32.png" alt="TrashIcon" style="width: 20px" />
    </td>
  </tr>
</template>

<script>
import TrashIcon from "../assets/trash32x32.png";

export default {
  props: ["user", "filters", "locationId"],
  methods: {
    deleteUser() {
      console.log("this.user.id", this.user.id);
      this.$store.commit("deleteUser", this.user.id);
    },
  },
};
</script>

<style></style>
