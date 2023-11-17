<template>
  <div>
    <div>
      <ActionsBar locationId="tableWithActions" />
      <div>
        <UsersTable locationId="tableWithActions" />
      </div>
    </div>
    <div>
      <ActionsBar locationId="tableNoActions" />
      <div>
        <UsersTable locationId="tableNoActions" />
      </div>
    </div>
  </div>
</template>

<script>
import ActionsBar from "../components/ActionsBar.vue";
import UsersTable from "../components/UsersTable.vue";
export default {
  components: { ActionsBar, UsersTable },

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
      this.$store.commit("updateUsers", this.users);
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

  border-radius: 2px;
}
.cancel-button {
  background-color: #ffffff;
  color: rgb(116, 111, 111);
  padding: 10px 20px;
  border: 1px solid rgba(128, 128, 128, 0.485);
  border-radius: 2px;
}
input {
  padding: 10px 20px;
  margin-left: 10px;
  border: 1px solid rgba(128, 128, 128, 0.485);
  border-radius: 2px;
}
body {
  width: 95%;
  margin-left: auto;
  margin-right: auto;
}
</style>
