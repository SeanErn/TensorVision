<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <InputOutputSlider title="Exposure:" :min="0" :max="100" :step="1" :value="0"/>
            <InputOutputSlider title="Brightness:" :min="0" :max="100" :step="1" :value="0"/>
            <InputOutputSlider title="Gain:" :min="0" :max="100" :step="1" :value="0"/>
        </ClientOnly>
    </div>
</template>
