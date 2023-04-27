<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})
</script>

<template>
  <html class="bg-zinc-900">
    <head>
        <meta charset="utf-8">
        <meta name="color-scheme" content="dark" />
        <title>Home | Tensorflow Custom</title>
    </head>
    <ClientOnly>
    <div class="flex flex-row gap-5">
    <CameraWrapper/>
    <SelectorWrapper/>
    </div> 
    </ClientOnly>
  </html>
  </template>