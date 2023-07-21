<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <HomeInputOutputDropdown title="Orientation:" placeholder="Select Orientation" :options="['90 Clockwise', '180', '90 Counter Clockwise']"/>
            <HomeInputOutputDropdown title="Resolution:" placeholder="Select Resolution"/>
            <HomeInputOutputDropdown title="Stream Resolution:" placeholder="Select Stream Resolution"/>
        </ClientOnly>
    </div>
</template>
