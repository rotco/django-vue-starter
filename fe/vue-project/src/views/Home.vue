<template>
  <div>
    <h1>Hello World</h1>
    <div>
      {{ items }}
    </div>
  </div>
</template>

<script>
export default {
  components: {},

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
