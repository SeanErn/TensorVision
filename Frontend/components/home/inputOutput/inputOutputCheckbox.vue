<template>
    <div class="form-control bg-base-100 rounded-md mb-2">
        <label class="label cursor-pointer flex items-center">
            <span class="label-text text-lg">{{ title }}</span>
            <div class="bg-base-300 p-1 mr-1 rounded-md aspect-square justify-center flex items-center">
                <input type="checkbox" class="checkbox checkbox-lg checkbox-primary border-2" />
            </div>
        </label>
    </div>
</template>

<script setup lang="ts">

const props = defineProps({
    title: String,
})

</script>