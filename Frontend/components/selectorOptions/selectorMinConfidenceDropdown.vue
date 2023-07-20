<template>
<div class="relative ">

  <!-- Dropdown menu -->
  <!-- Min confidence 0.0-1.0 Float  -->

  <div class="p-2 bg-base-300 justify-center flex rounded-md min-w-full my-2">
    <input type="range" min="0.0" max="1.0" step="0.01" v-model="confidence" class="range range-primary p-0" />
    <input type="text" class="ml-2 w-16 text-center" v-model="confidence" />
    
  </div>  
</div>

</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';


const confidence = ref(0.5);

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
  const dropdownButton = document.getElementById('selectorMinConfidenceDropdownBtn');
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
