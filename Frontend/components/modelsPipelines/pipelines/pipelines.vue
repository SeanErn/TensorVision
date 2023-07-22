<template>
    <div class="place-content-center rounded-md bg-base-200 p-3 w-full">
        <div class="py-2">
            <h1 class="font-bold text-2xl">Pipelines</h1>
        </div>
        <Button title="Add Pipeline" type="bg-base-300" onclick="addPipeline.showModal()" />
        <Button title="Edit Pipeline" type="bg-base-300" :disabled="!selectedPipeline" />
        <Button title="Delete Pipeline" type="btn-primary" :disabled="!selectedPipeline" />

        <table class="table table-zebra bg-base-100 rounded-md mt-4">
            <!-- head -->
            <thead class="">
                <tr class=" text-base">
                    <th>#</th>
                    <th>Name</th>
                    <th>Model</th>
                    <th>Settings</th>
                </tr>
            </thead>
            <tbody v-if="pipelines">
                <tr v-for="(pipeline, index) in pipelines" :key="index"
                    @click="selectedPipeline === pipeline.pipelineName ? selectedPipeline = '' : selectedPipeline = pipeline.pipelineName"
                    :class="{ 'bg-base-300': selectedPipeline === pipeline.pipelineName }">
                    <th>{{ index }}</th>
                    <td>{{ pipeline.pipelineName }}</td>
                    <td>{{ pipeline.pipelineSettings.model }}</td>
                </tr>
            </tbody>
            <tbody v-else>
                <tr>
                    <td colspan="3">No models found... add a new one to get started. If you think this is wrong check your
                        connection. </td>
                </tr>
            </tbody>
        </table>

    </div>
    <dialog id="addPipeline" class="modal">
        <form method="dialog" class="modal-box">
            <h3 class="font-bold text-lg">Add Module</h3>
            <hr class="my-2">
            <div class="form-control w-full max-w-xs">
                <label class="label">
                    <span class="label-text">Model Name</span>
                </label>
                <input type="text" placeholder="Type here" class="input input-bordered w-full max-w-xs" />
                <label class="label">
                </label>
            </div>
            <div class="form-control w-full max-w-xs">
                <label class="label">
                    <span class="label-text">Model - detect.tflite</span>
                </label>
                <input type="file" accept=".tflite"
                    class="file-input file-input-bordered file-input-primary w-full max-w-xs" />
            </div>
            <div class="form-control w-full max-w-xs">
                <label class="label">
                    <span class="label-text">Model - label.pbtxt</span>
                </label>
                <input type="file" accept=".pbtxt"
                    class="file-input file-input-bordered file-input-secondary w-full max-w-xs" />
            </div>
            <div class="modal-action">
                <!-- if there is a button in form, it will close the modal -->
                <button class="btn btn-primary">Add Module</button>
                <button class="btn">
                    <svg class="w-[14px] h-[14px] text-gray-800 dark:text-white" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                    </svg>
                </button>
            </div>
        </form>
    </dialog>
</template>

<script setup lang="ts">

const pipelines = ref < {
    _id: {
        $oid: String;
    }, 
    pipelineName: String,
    cameraSettings: {
        device: Number,
        exposure: Number,
        brightness: Number,
        autoExposure: Boolean,
        inputImageRotationMode: Number,
    },
    pipelineSettings : {
        model: String,
        minimumConfidence: Number,
        targetingOffsets : {
            yaw: Number,
            pitch: Number,
        }
    }
}[] | undefined > ();
const selectedPipeline = ref<String | undefined>();

</script>