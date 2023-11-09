<template>
  <div>
    <h1>
      <Greetings message="Home Page" />
    </h1>
    <div>
      {{ items }}
    </div>
  </div>
</template>

<script>
import Greetings from "../components/Greetings.vue";
export default {
  components: { Greetings },

  data() {
    return {
      items: [],
    };
  },
  methods: {
    async getItems() {
      console.log("getItems");
      const response = await (
        await fetch("http://localhost:8000/api/items")
      ).json();
      this.items = response.results;
    },
  },
  mounted() {
    this.getItems();
  },
};
</script>

<style></style>
