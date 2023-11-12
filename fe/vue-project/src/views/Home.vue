<template>
  <div>
    <div v-if="error">{{ error }}</div>
    <Candidates :candidates="candidates" />
  </div>
</template>

<script>
import Candidates from "../components/Candidates.vue";
export default {
  components: { Candidates },

  data() {
    return {
      items: [],
      error: null,
      candidates: [],
    };
  },
  methods: {
    async fetchCandidates() {
      const response = await fetch(
        "http://localhost:8000/api/resume/allcands-full-api_hub_b1f6-acde48001122.json"
      );
      if (response && response.ok) {
        const candidateRaw = await response.json();
        this.candidates = candidateRaw.results;
        console.log("candidates:", this.candidates);
      } else {
        console.log("error:", response);
        this.error = `${response.statusText} ${response.status}`;
      }
    },
    async getItems() {
      console.log("getItems");
      const response = await (
        await fetch("http://localhost:8000/api/items")
      ).json();
      this.items = response.results;
    },
  },
  mounted() {
    this.fetchCandidates();
  },
};
</script>

<style></style>
