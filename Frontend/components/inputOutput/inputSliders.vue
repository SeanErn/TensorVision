<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <InputOutputInputSlider title="Exposure:" :min="0" :max="100" :step="1" :value="0"/>
            <InputOutputInputSlider title="Brightness:" :min="0" :max="100" :step="1" :value="0"/>
            <InputOutputInputSlider title="Gain:" :min="0" :max="100" :step="1" :value="0"/>
        </ClientOnly>
    </div>
</template>
