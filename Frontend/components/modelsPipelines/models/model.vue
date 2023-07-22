<template>
    <div class="place-content-center rounded-md bg-base-200 p-3 w-full">
        <div class="py-2">
            <h1 class="font-bold text-2xl">Models</h1>
        </div>
        <Button title="Add Model" type="bg-base-300" onclick="addModel.showModal()" />
        <Button title="Edit Model" type="bg-base-300" :disabled="!selectedModel" />
        <Button title="Delete Model" type="btn-primary" :disabled="!selectedModel" />

        <table class="table table-zebra bg-base-100 rounded-md mt-4">
            <!-- head -->
            <thead class="">
                <tr class=" text-base">
                    <th>#</th>
                    <th>Name</th>
                    <th>detect.tflite</th>
                    <th>label.pbtxt</th>
                </tr>
            </thead>
            <tbody v-if="models">
                <tr v-for="(model, index) in models" :key="index" @click="selectedModel === model.name ? selectedModel = '' : selectedModel = model.name"
                    :class="{ 'bg-base-300': selectedModel === model.name }">
                    <th>{{ index }}</th>
                    <td>{{ model.name }}</td>
                    <td>{{ model.detect }}</td>
                    <td>{{ model.label }}</td>
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
    <dialog id="addModel" class="modal">
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
                <input type="file" accept=".tflite" class="file-input file-input-bordered file-input-primary w-full max-w-xs" />
            </div>
            <div class="form-control w-full max-w-xs">
                <label class="label">
                    <span class="label-text">Model - label.pbtxt</span>
                </label>
                <input type="file" accept=".pbtxt" class="file-input file-input-bordered file-input-secondary w-full max-w-xs" />
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

const models = ref<{ name: string, detect: string, label: string }[] | undefined>(
    [
        {
            name: 'hello',
            detect: 'detect.tflite',
            label: 'label.pbtxt'
        }
    ]
);
const selectedModel = ref<string | undefined>();

</script>