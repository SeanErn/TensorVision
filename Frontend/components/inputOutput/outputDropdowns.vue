<template>
    <div class="content-between w-full text-lg rounded-md shadow-md">
        <ClientOnly>
            <InputOutputDropdown title="Target Offset Point:" placeholder="Select Offset Point" :options="['Center', 'Top', 'Bottom', 'Left', 'Right']"/>
            <InputOutputDropdown title="Target Sort:" placeholder="Select Sort Mode" :options="['Highest Confidence', 'Lowest confidence', 'Largest', 'Smallest', 'Highest', 'Lowest', 'Rightmost', 'Leftmost', 'Centermost']"/>
            <InputOutputDropdown title="Robot Offset Mode:" placeholder="Select Offset Mode" :options="['None', 'Single Point']"/>
        </ClientOnly>
    </div>
</template>