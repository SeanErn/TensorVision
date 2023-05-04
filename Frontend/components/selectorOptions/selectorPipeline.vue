<template>
    <div class="grid grid-cols-dropdownGrid content-between w-full bg-zinc-700 px-3 py-2 text-zinc-200 text-lg rounded-md shadow-md">
        <span class="flex items-center">Pipeline: </span>
        <ClientOnly>
            <SelectorPipelineDropdown/>
        </ClientOnly>
    </div>
</template>
