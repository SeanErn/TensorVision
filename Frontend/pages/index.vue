<template>
  <html class="bg-zinc-900 max-w-full overflow-y-scroll" data-theme="alotobots">
    <head>
        <meta charset="utf-8">
        <meta name="color-scheme" content="dark" />
        <title>Home | Tensorflow Custom</title>
    </head>
    <ClientOnly>
    <div class="p-4 gap-4 grid grid-cols-4 grid-rows-2 max-w-full">
    <CameraWrapper class="xl:col-span-3  col-span-4 max-w-full"/>
    <SelectorOptionsQuickSettings class="col-span-2 xl:col-span-1"/>
    <InputOutput class="col-span-2 xl:col-span-1"/>
    </div> 
    </ClientOnly>
  </html>
  </template>