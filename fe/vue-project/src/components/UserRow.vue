<template>
  <tr>
    <td v-if="!filters?.date">{{ user.date }}</td>
    <td v-if="!filters?.name">{{ user.name }}</td>
    <td v-if="!filters?.address">{{ user.address }}</td>
    <td v-if="locationId == 'tableWithActions'">delete</td>
  </tr>
</template>

<script>
export default {
  props: ["user", "filters", "locationId"],
};
</script>

<style></style>
