<template>
  <div class="filters-actions-bar">
    <Errors :errors="errors" @closeErrors="closeErrors" v-if="showErrors" />
    <PopupDialog
      v-if="showAddUserDialog"
      @handleConfirm="addUser"
      @closeDialog="closeDialog"
      header="Add User"
      :form="userForm"
    />
    <div class="filters">
      <div class="filter">
        <input
          @change="handleFilter"
          v-model="dateFilter"
          type="checkbox"
          id="date"
          name="date"
        />
        <label for="date">Date</label>
      </div>
      <div class="filter">
        <input
          @change="handleFilter"
          v-model="nameFilter"
          type="checkbox"
          id="name"
          name="name"
        />
        <label for="name">Name</label>
      </div>
      <div class="filter">
        <input
          @change="handleFilter"
          v-model="addressFilter"
          type="checkbox"
          id="address"
          name="address"
        />
        <label for="address">Address</label>
      </div>
    </div>
    <div v-if="locationId == 'tableWithActions'" class="actions">
      <div class="search">
        <input
          placeholder="Search"
          @change="handleSearch"
          v-model="searchQuery"
          class="search-box"
        />
      </div>
      <input
        class="submit-button"
        type="button"
        value="Add User"
        @click="showAddUserDialog = true"
      />
    </div>
  </div>
</template>

<script>
import PopupDialog from "../components/PopupDialog.vue";
import Errors from "../components/Errors.vue";
export default {
  components: { PopupDialog, Errors },
  props: ["locationId"],
  data() {
    return {
      dateFilter: false,
      nameFilter: false,
      addressFilter: false,
      searchTimeout: null,
      searchQuery: "",
      showAddUserDialog: false,
      userForm: {
        name: "",
        address: "",
      },
      errors: {},
      showErrors: false,
    };
  },
  watch: {
    searchQuery(newVal, oldVal) {
      this.handleSearch();
    },
  },
  methods: {
    handleFilter() {
      let filters = {};
      filters[this.locationId] = {
        date: this.dateFilter,
        name: this.nameFilter,
        address: this.addressFilter,
      };
      console.log("handleFilter", filters);

      this.$store.commit("updateFilters", filters);
    },
    handleSearch() {
      console.log("handleSearch", this.searchQuery);

      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.runSearch();
      }, 1000);
    },
    async runSearch() {
      console.log("runSearch", this.searchQuery);
      const response = await (
        await fetch(
          `http://localhost:8000/api/filtered-users?search=${this.searchQuery}`
        )
      ).json();
      console.log("search response:", response);
      if (response && response.results) {
        this.$store.commit("updateFilteredUserIds", response.results);
      }
    },
    async addUser() {
      console.log("addUser", this.userForm);
      const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.userForm),
      };
      const response = await (
        await fetch("http://localhost:8000/api/users", options)
      ).json();
      console.log("addUser response:", response);
      if (response && response.results) {
        this.$store.commit("pushUserToStore", response.results);
        this.initUserForm();
      } else if (response.errors) {
        console.log("errors:", response.errors);
        this.errors = response.errors;
        this.initUserForm();
        this.showErrors = true;
      }
      this.showAddUserDialog = false;
    },
    initUserForm() {
      this.userForm = {
        name: "",
        address: "",
      };
    },
    closeDialog() {
      this.initUserForm();
      this.showAddUserDialog = false;
    },
    closeErrors() {
      this.showErrors = false;
    },
  },
};
</script>

<style>
.search-box {
  width: 300px;
}
.filter {
  margin-right: 24px;
}
.filters {
  margin-top: auto;
  margin-bottom: auto;
}
label {
  margin-left: 10px;
}
</style>
