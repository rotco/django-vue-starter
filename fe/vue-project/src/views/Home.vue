<template>
  <div>
    <ActionsBar name="top" />
    <div>
      {{ users }}
    </div>
  </div>
</template>

<script>
import ActionsBar from "../components/ActionsBar.vue";
export default {
  components: { ActionsBar },

  data() {
    return {
      users: [],
    };
  },
  methods: {
    async getUsers() {
      console.log("getUsers");
      const response = await (
        await fetch("http://localhost:8000/api/users")
      ).json();
      this.users = response.results;
    },
  },
  mounted() {
    this.getUsers();
  },
};
</script>

<style>
.filters-actions-bar,
.filters,
.actions {
  display: flex;
  justify-content: space-between;
}
</style>
