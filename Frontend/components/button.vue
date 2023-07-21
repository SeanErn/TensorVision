<template>
    <button class='btn mr-2' :class="type">{{ title }}</button>
</template>

<script setup lang="ts">

const props = defineProps({
    title: String,
    type: String,
})

</script>