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
    <div class="actions">
      <div class="search">
        <input placeholder="Search" />
      </div>
      <button>Add User</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["name"],
  data() {
    return {
      dateFilter: false,
      nameFilter: false,
      addressFilter: false,
    };
  },
  methods: {
    handleFilter() {
      console.log(
        "handleFilters",
        this.dateFilter,
        this.nameFilter,
        this.addressFilter
      );
    },
  },
};
</script>

<style></style>
