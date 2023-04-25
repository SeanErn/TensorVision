<template>
    <div id="nav" class="bg-zinc-800 shadow-xl shadow-zinc-850">
      <div class="mx-auto px-6 py-6 flex gap-10 text-slate-50 text-4xl font-ubuntu font-bold">
        <NuxtLink to="/" class="hover:text-zinc-200">Home</NuxtLink>
        <NuxtLink to="/about" class="hover:text-zinc-200">About</NuxtLink>
        <NuxtLink to="/contact" class="hover:text-zinc-200">Contact</NuxtLink>
      </div>
    </div>
<div class="container p-4 text">
    <slot />
</div>
</template>