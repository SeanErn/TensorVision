<template>
    <div class="relative flex-grow rounded-md p-3 bg-base-200 max-w-full mb-auto max-2xl:h-1/2 ">
        <h1 class="p-2 font-bold text-2xl">Target Info</h1>
        <div class="overflow-x-auto">
            <table class="table table-zebra bg-base-100 rounded-md">
                <!-- head -->
                <thead class="">
                    <tr class=" text-base">
                        <th>Target Number</th>
                        <th>Class</th>
                        <th>Confidence</th>
                        <th>Pitch</th>
                        <th>Yaw</th>
                        <th>Area</th>
                    </tr>
                </thead>
                <tbody v-for="(target, index) in targets">
                    <tr>
                        <th>{{ index }}</th>
                        <td>{{ target.class }}</td>
                        <td>{{ target.confidence }}</td>
                        <td>{{ target.pitch }}</td>
                        <td>{{ target.yaw }}</td>
                        <td>{{ target.area }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue';

// initialize components based on data attribute selectors
onMounted(() => {
})

const socket = new WebSocket("ws://127.0.0.1:5000");
const targets = ref<{ targetNumber: number, class: string, confidence: number, pitch: number, yaw: number, area: number }[]>([{ targetNumber: 0, class: 'N/A', confidence: 0, pitch: 0, yaw: 0, area: 0 }]);

socket.addEventListener("message", (event) => {
    console.log("WebSocket message received:", event.data);
    let parsed = JSON.parse(event.data)

    switch (parsed.type) {
        case "targetInfo":
            targets.value = parsed.data;
            console.log(`Models: ${targets.value}`);
            break;
        default:
            console.error(`Unknown message type: ${parsed.type} with data: ${parsed.data}`)
            break;
    }

});

socket.addEventListener("close", (event) => {
    console.log("WebSocket connection closed:", event);
});
</script>
  