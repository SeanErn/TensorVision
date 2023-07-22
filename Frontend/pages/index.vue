<template>
  <html class="bg-zinc-900 min-h-full" data-theme="alotobots">

  <head>
    <meta charset="utf-8">
    <meta name="color-scheme" content="dark" />
    <title>Tensor Vision - Home</title>
  </head>
  <ClientOnly>
    <div class="m-4 gap-4 lg:grid grid-cols-4 flex flex-col justify-center items-center">
      <HomeCameraStreamsCameraWrapper class="xl:col-span-3 col-span-4 w-full max-lg:my-2" />
      <HomeSelectorOptionsQuickSettings class="col-span-2 xl:col-span-1 max-lg:my-2" />
      <HomeInputOutput class="col-span-2 row-span-2  max-lg:my-2" />
      <HomeTargetInfo class="col-span-2  max-lg:my-2 h-full " />
    </div>
  </ClientOnly>

  </html>
</template>

<script setup lang="ts">
onMounted(() => {
})

const socket = new WebSocket("ws://127.0.0.1:5000");

socket.addEventListener("open", (event) => {
  console.log("WebSocket connection opened:", event);
  let payload = JSON.stringify({
    type: "getAll",
    data: {}
  });
  socket.send(payload);
});

socket.addEventListener("message", (event) => {
  console.log(event);
});

// export default {
//   setup() {
//     provide('providedData', 'Hello from parent component')
//   }
// }
</script>