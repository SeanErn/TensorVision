<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <InputOutputDropdown title="Orientation:" placeholder="Select Orientation" :options="['90 Clockwise', '180', '90 Counter Clockwise']"/>
            <InputOutputDropdown title="Resolution:" placeholder="Select Resolution"/>
            <InputOutputDropdown title="Stream Resolution:" placeholder="Select Stream Resolution"/>
        </ClientOnly>
    </div>
</template>
