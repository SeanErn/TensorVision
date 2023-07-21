<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <HomeInputOutputSlider title="Exposure:" :min="0" :max="100" :step="1" :value="0"/>
            <HomeInputOutputSlider title="Brightness:" :min="0" :max="100" :step="1" :value="0"/>
            <HomeInputOutputSlider title="Gain:" :min="0" :max="100" :step="1" :value="0"/>
        </ClientOnly>
    </div>
</template>
