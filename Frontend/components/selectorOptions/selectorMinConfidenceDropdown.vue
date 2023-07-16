<template>
<div class="relative">
  <button id="selectorMinConfidenceDropdownBtn" ref="selectorMinConfidenceDropdownBtn" data-dropdown-toggle="selectorMinConfidenceDropdownMenu" data-dropdown-trigger="click" data-dropdown-delay="750" class=" w-full text-white focus:ring-zinc-400 focus:ring-2 focus:outline-none font-medium rounded-lg text-sm px-4 py-2.5 flex justify-between items-center bg-zinc-800 hover:bg-zinc-900" type="button">Minimum Model Confidence <svg class="w-4 h-4 ml-2" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></button>
  <!-- Dropdown menu -->
  <div id="selectorMinConfidenceDropdownMenu" ref="selectorMinConfidenceDropdownMenu" class="z-10 hidden divide-y divide-gray-100 rounded-lg shadow bg-zinc-900 w-full">
    <ul class="h-44 py-2 text-sm text-gray-200 overflow-y-auto transition-opacity overflow-x-clip" aria-labelledby="dropdownDefaultButton">
      <li v-for="(value, index) in pipelineNames" :key="index">
        <a href="#" class="block px-4 py-2  hover:bg-gray-600 hover:text-white text-ellipsis" @click="updateButton(value)">{{ value }}</a>
      </li>
    </ul>
  </div>
</div>

</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { initFlowbite } from 'flowbite';

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
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
