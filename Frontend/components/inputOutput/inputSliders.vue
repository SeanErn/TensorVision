<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <InputSlider title="Exposure:" :min="0" :max="100" :step="1" :value="0"/>
            <InputSlider title="Brightness:" :min="0" :max="100" :step="1" :value="0"/>
            <InputSlider title="Contrast:" :min="0" :max="100" :step="1" :value="0"/>
        </ClientOnly>
    </div>
</template>
