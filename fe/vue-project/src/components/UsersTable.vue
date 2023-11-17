<template>
  <div>
    <div v-if="showDeleteDialog" class="popup">
      <div>
        <div class="popup-header">Delete User</div>
        <div class="popup-text">
          Are you sure you want to delete {{ selectedUser.name }} ?
        </div>
        <div class="popup-buttons">
          <input
            @click="showDeleteDialog = false"
            value="Cancel"
            type="button"
          />
          <input @click="deleteUser()" value="Confirm" type="button" />
        </div>
      </div>
    </div>
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
          @deleteUser="handleDeleteUserButton"
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
