<template>
    <div class="flex gap-2 w-full bg-base-100 px-3 text-lg rounded-md shadow-md">
        <span class="flex items-center">Pipeline: </span>
        <ClientOnly>
            <SelectorPipelineDropdown/>
        </ClientOnly>
    </div>
</template>
