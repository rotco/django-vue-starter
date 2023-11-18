import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      filters: {},
      users: [],
      filteredUserIds: null,
    };
  },
  mutations: {
    updateFilters(state, data) {
      state.filters = data;
      console.log("updateFilters:", data);
    },
    updateUsers(state, data) {
      state.users = data;
      console.log("updateState:", data);
    },
    updateFilteredUserIds(state, data) {
      state.filteredUserIds = new Set(data);
      console.log("updateFilteredUserIds:", data);
    },
    deleteUser(state, id) {
      state.users = state.users.filter((user) => user.id != id);
    },
    pushUserToStore(state, user) {
      state.users.push(user);
    },
  },
  getters: {
    users(state) {
      return state.users;
    },
    filters(state) {
      return state.filters;
    },
    filteredUserIds(state) {
      return state.filteredUserIds;
    },
  },
});
