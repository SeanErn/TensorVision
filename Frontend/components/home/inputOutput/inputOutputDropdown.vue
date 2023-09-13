<template>
  <div class="relative flex items-center gap-2 min-w-full bg-base-100 px-2 mb-2 rounded-lg">
    <h1>
      {{ title }}
    </h1>
    <!-- Dropdown menu -->
    <select class="select select-bordered bg-base-300 my-2 w-full">
      <option disabled selected>{{ placeholder }}</option>
      <option v-for="(value, index) in options" :key="index">{{ value }}</option>
    </select>
  </div>
</template>
<!-- TODO: Fix this to do models instead of pipelines -->
<script setup lang="ts">
import { ref, onMounted } from 'vue';

defineProps({
  title: String,
  options: Array,
  placeholder: String,
})

// initialize components based on data attribute selectors
onMounted(() => {
})

</script>
