<template>
  <div class="relative flex-grow">

    <!-- Dropdown menu -->
    <select class="select select-bordered bg-base-300 my-2 min-w-full">
      <option disabled selected>Select Pipeline</option>
      <option v-for="(value, index) in pipelineNames" :key="index">{{ value }}</option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

// initialize components based on data attribute selectors
onMounted(() => {
})

const socket = new WebSocket("ws://127.0.0.1:5000");
const pipelineNames = ref<string[]>([]);

socket.addEventListener("open", (event) => {
  console.log("WebSocket connection opened:", event);
  let payload = JSON.stringify({
    type: "getAllPipelineNames",
    data: {}
  });
  socket.send(payload);
});

socket.addEventListener("message", (event) => {
  console.log("WebSocket message received:", event.data);
  let parsed = JSON.parse(event.data)

  switch (parsed.type) {
    case "getAllPipelineNames":
      pipelineNames.value = parsed.data.pipelines;
      console.log(`Models: ${pipelineNames.value}`);
      break;
    default:
      console.error(`Unknown message type: ${parsed.type} with data: ${parsed.data}`)
      break;
  }

});

socket.addEventListener("close", (event) => {
  console.log("WebSocket connection closed:", event);
});

// Handle dropdown name of pipeline, send to backend and save for next restart
function updateButton(pipeline: string) {
  const dropdownButton = document.getElementById('selectorPipelineDropdownBtn');
  if (dropdownButton) {
    dropdownButton.childNodes[0].textContent = pipeline;
    let payload = JSON.stringify({
      type: "updatePipelineName",
      command: "updatePipelineName",
      data: {
        pipelineName: pipeline
      }
    });
    socket.send(payload);
  }
}


</script>
