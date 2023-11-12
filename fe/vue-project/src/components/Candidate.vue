<template>
  <div>
    <div>
      <span class="name-heading">{{ candidate.name }}</span>
      <span v-if="candidate.linkedin"
        >- <a href="candidate.linkedin">"{{ candidate.linkedin }}"</a></span
      >
    </div>
    <br />
    <Experience :experience="candidate.experience" />
  </div>
</template>

<script>
import Experience from "../components/Experience.vue";
export default {
  components: { Experience },
  props: ["candidate"],
};
</script>

<style>
.name-heading {
  font-size: 1.2rem;
}
</style>
