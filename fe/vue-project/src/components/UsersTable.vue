<template>
  <div>
    <PopupDialog
      v-if="showDeleteDialog"
      @handleConfirm="deleteUser"
      @closeDialog="showDeleteDialog = false"
      header="Delete User"
      text="Are you sure you want to delete the user ?"
    />
    <table>
      <thead>
        <tr class="table-head">
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
            locationId == 'tableNoActions' ||
            filteredUserIds == null ||
            (filteredUserIds && filteredUserIds.has(user.id))
          "
          @deleteUser="handleDeleteUserButton"
        />
      </tbody>
    </table>
  </div>
</template>

<script>
import PopupDialog from "./PopupDialog.vue";
import UserRow from "./UserRow.vue";
export default {
  components: { UserRow, PopupDialog },
  props: ["locationId"],
  data() {
    return {
      filters: {},
      users: [],
      filteredUserIds: null,
      showDeleteDialog: false,
      selectedUser: null,
    };
  },
  methods: {
    handleDeleteUserButton(user) {
      this.selectedUser = user;
      this.showDeleteDialog = true;
    },
    deleteUser() {
      this.$store.commit("deleteUser", this.selectedUser.id);
      this.showDeleteDialog = false;
    },
  },
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

<style>
table {
  border-collapse: collapse;
  width: 100%;
  margin-top: 20px;
  margin-bottom: 60px;
}
th,
td {
  text-align: left;
}
thead tr {
  border-bottom: 1px solid #00000022;
}
tbody tr {
  border-bottom: 1px solid #0000000d;
}
</style>
