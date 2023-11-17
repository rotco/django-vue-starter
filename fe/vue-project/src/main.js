import "./assets/main.css";

import { createApp } from "vue";
import { createStore } from "vuex";

import App from "./App.vue";
import router from "./router";

const app = createApp(App);

const store = createStore({
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

app.use(router);
app.use(store);

app.mount("#app");
