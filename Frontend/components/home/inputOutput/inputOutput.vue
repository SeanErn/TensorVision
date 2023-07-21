<template>
    <div class="container place-content-center rounded-md h-fit mb-auto flex max-2xl:flex-col gap-4">
        <div class="container place-content-center rounded-md bg-base-200 p-3 h-fit mb-auto">
            <div class="py-2">
                <h1 class="font-bold text-2xl">Input</h1>
            </div>
            <div class="">
                <HomeInputOutputInputSliders />
                <HomeInputOutputInputDropdowns />
            </div>
        </div>
        <div class="container place-content-center rounded-md bg-base-200 p-3 h-fit mb-auto">
            <div class="py-2">
                <h1 class="font-bold text-2xl">Output</h1>
            </div>
            <div class="">
                <HomeInputOutputDropdowns />
                <!-- <HomeInputOutputCheckbox title="Show Multiple Targets"/> -->
                <HomeInputOutputButtons />
            </div>
        </div>
    </div>
</template>