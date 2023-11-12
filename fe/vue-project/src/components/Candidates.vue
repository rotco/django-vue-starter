<template>
  <div>
    <div v-for="cand in candidates" :key="cand.name" class="candidate-card">
      <Candidate :candidate="cand" />
    </div>
  </div>
</template>

<script>
import Candidate from "../components/Candidate.vue";
export default {
  components: { Candidate },

  props: ["candidates"],
};
</script>

<style>
.candidate-card {
  margin: 20px;
}
</style>
