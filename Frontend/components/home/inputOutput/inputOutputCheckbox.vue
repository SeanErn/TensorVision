<template>
    <div class="form-control">
        <label class="label cursor-pointer flex items-center">
            <span class="label-text text-lg">{{ title }}</span>
            <input type="checkbox" class="checkbox checkbox-lg" />
        </label>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
    title: String,
})

</script>