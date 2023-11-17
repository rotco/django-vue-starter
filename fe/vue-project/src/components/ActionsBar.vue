<template>
  <div class="filters-actions-bar">
    <div class="filters">
      <div class="filter">
        <input
          @change="handleFilter"
          v-model="dateFilter"
          type="checkbox"
          id="date"
          name="date"
        />
        <label for="date">date</label>
      </div>
      <div class="filter">
        <input
          @change="handleFilter"
          v-model="nameFilter"
          type="checkbox"
          id="name"
          name="name"
        />
        <label for="name">name</label>
      </div>
      <div class="filter">
        <input
          @change="handleFilter"
          v-model="addressFilter"
          type="checkbox"
          id="address"
          name="address"
        />
        <label for="address">address</label>
      </div>
    </div>
    <div v-if="locationId == 'tableWithActions'" class="actions">
      <div class="search">
        <input
          placeholder="Search"
          @change="handleSearch"
          v-model="searchQuery"
        />
      </div>
      <button>Add User</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["locationId"],
  data() {
    return {
      dateFilter: false,
      nameFilter: false,
      addressFilter: false,
      searchTimeout: null,
      searchQuery: "",
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
  },
};
</script>

<style></style>
