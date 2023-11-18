<template>
  <div class="container">
    <ActionsBar locationId="tableWithActions" />
    <UsersTable locationId="tableWithActions" />
    <ActionsBar locationId="tableNoActions" />
    <UsersTable locationId="tableNoActions" />
  </div>
</template>

<script>
import ActionsBar from "../components/ActionsBar.vue";
import UsersTable from "../components/UsersTable.vue";
export default {
  components: { ActionsBar, UsersTable },

  methods: {
    async getUsers() {
      console.log("getUsers");
      const response = await (
        await fetch("http://localhost:8000/api/users")
      ).json();
      this.$store.commit("updateUsers", response.results);
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
.submit-button {
  background-color: #127bea;
  color: white;
  padding: 10px 20px;
  border: 1px solid rgba(128, 128, 128, 0.485);
  border-radius: 5px;
}
.cancel-button {
  background-color: #ffffff;
  color: rgb(116, 111, 111);
  padding: 10px 20px;
  border: 1px solid rgba(128, 128, 128, 0.485);
  border-radius: 5px;
}
input {
  padding: 10px 20px;
  margin-left: 8px;
  border: 1px solid rgba(128, 128, 128, 0.485);
  border-radius: 5px;
}
.container {
  width: 95%;
  margin-left: auto;
  margin-right: auto;
  font-family: sans-serif;
}
</style>
