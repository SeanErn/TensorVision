<template>
<button id="selectorPipelineDropdownButton" data-dropdown-toggle="dropdown" class="text-white focus:ring-zinc-400 focus:ring-2 focus:outline-none font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center bg-zinc-800 hover:bg-zinc-900" type="button">Dropdown button <svg class="w-4 h-4 ml-2" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></button>
<!-- Dropdown menu -->
<div id="selectorPipelineDropdownMenu" class="z-10 hidden divide-y divide-gray-100 rounded-lg shadow w-44 bg-zinc-900">
  <ul class="py-2 text-sm text-gray-200" aria-labelledby="dropdownDefaultButton">
    <li v-for="(value, index) in modelsArray" :key="index">
      <a href="#" class="block px-4 py-2  hover:bg-gray-600 hover:text-white" @click="updateButton(value)">{{ value }}</a>
    </li>
  </ul>
</div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
import { Dropdown } from 'flowbite';

// set the dropdown menu element
const $targetEl = document.getElementById('selectorPipelineDropdownMenu');

// set the element that trigger the dropdown menu on click
const $triggerEl = document.getElementById('selectorPipelineDropdownButton');

// options with default values
const options = {
  placement: 'bottom',
  triggerType: 'click',
  offsetSkidding: 0,
  offsetDistance: 10,
  delay: 300,
  onHide: () => {
      console.log('dropdown has been hidden');
  },
  onShow: () => {
      console.log('dropdown has been shown');
  },
  onToggle: () => {
      console.log('dropdown has been toggled');
  }
};

// initialize the dropdown
const dropdown = new Dropdown($targetEl, $triggerEl, options);
const socket = new WebSocket("ws://127.0.0.1:5000");
const modelsArray = ref<string[]>([]);

socket.addEventListener("open", (event) => {
  console.log("WebSocket connection opened:", event);
  socket.send("getAllModelNames");
});

socket.addEventListener("message", (event) => {
  console.log("WebSocket message received:", event.data);
  let parsed = JSON.parse(event.data)

  switch (parsed.type) {
    case "getAllModelNames":
      modelsArray.value = parsed.data.models;
      console.log(`Models: ${modelsArray.value}`);
      break;
    default:
      console.error(`Unknown message type: \${parsed.type} with data: \${parsed.data}`)
      break;
  }

});

socket.addEventListener("close", (event) => {
  console.log("WebSocket connection closed:", event);
});

// Handle dropdown name of pipeline
function updateButton(pipeline: string) {
  const dropdownButton = document.getElementById('dropdownDefaultButton');
  if (dropdownButton) {
    dropdownButton.childNodes[0].textContent = pipeline;
  }
}
</script>
