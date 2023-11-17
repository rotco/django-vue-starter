<template>
  <div>
    <table>
      <thead>
        <tr>
          <th v-if="!filters[locationId]?.date">Date</th>
          <th v-if="!filters[locationId]?.name">Name</th>
          <th v-if="!filters[locationId]?.address">Address</th>
          <th v-if="locationId == 'tableWithActions'">Actions</th>
        </tr>
      </thead>

      <tbody v-for="user in users" :key="user.id">
        <UserRow
          :user="user"
          :filters="filters[locationId]"
          :locationId="locationId"
          v-if="
            locationId == 'tableWithActions' ||
            filteredUserIds == null ||
            (filteredUserIds && filteredUserIds.has(user.id))
          "
        />
      </tbody>
    </table>
  </div>
</template>

<script>
import UserRow from "./UserRow.vue";

export default {
  components: { UserRow },
  props: ["locationId"],
  data() {
    return {
      filters: {},
      users: [],
      filteredUserIds: null,
    };
  },
  methods: {},
  computed: {
    usersFromStore() {
      return this.$store.getters.users;
    },
    filtersFromStore() {
      return this.$store.getters.filters;
    },
    filteredUserIdsFromStore() {
      return this.$store.getters.filteredUserIds;
    },
  },
  watch: {
    filtersFromStore(newVal, oldVal) {
      this.filters = newVal;
    },
    usersFromStore(newVal, oldVal) {
      this.users = newVal;
    },
    filteredUserIdsFromStore(newVal, oldVal) {
      this.filteredUserIds = newVal;
    },
  },
};
</script>

<style></style>
