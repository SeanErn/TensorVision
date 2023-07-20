<template>
    <div class="container place-content-center rounded-md h-fit mb-auto flex max-2xl:flex-col gap-4">
        <div class="container place-content-center rounded-md bg-base-200 p-3 h-fit mb-auto">
            <div class="py-2">
                <h1 class="font-bold text-2xl">Input</h1>
            </div>
            <div class="">
                <InputOutputInputSliders />
                <InputOutputInputDropdowns />
            </div>
        </div>
        <div class="container place-content-center rounded-md bg-base-200 p-3 h-fit mb-auto">
            <div class="py-2">
                <h1 class="font-bold text-2xl">Output</h1>
            </div>
            <div class="">
                <InputOutputDropdowns />
                <InputOutputCheckbox title="Show Multiple Targets"/>
                <InputOutputButtons />
            </div>
        </div>
    </div>
</template>