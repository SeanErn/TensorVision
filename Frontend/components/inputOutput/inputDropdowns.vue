<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <InputOutputInputDropdown title="Orientation:" placeholder="Select Orientation" :options="['90 Clockwise', '180', '90 Counter Clockwise']"/>
            <InputOutputInputDropdown title="Resolution:" placeholder="Select Resolution"/>
            <InputOutputInputDropdown title="Stream Resolution:" placeholder="Select Stream Resolution"/>
        </ClientOnly>
    </div>
</template>
