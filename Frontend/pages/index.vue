<template>
  <html class="bg-zinc-900 min-h-full" data-theme="alotobots">
    <head>
        <meta charset="utf-8">
        <meta name="color-scheme" content="dark" />
        <title>Home | Tensorflow Custom</title>
    </head>
    <ClientOnly>
    <div class="m-4 gap-4 lg:grid grid-cols-4 grid-rows-2 flex flex-col justify-center items-center">
    <CameraStreamsCameraWrapper class="xl:col-span-3 col-span-4 w-full max-lg:my-2"/>
    <SelectorOptionsQuickSettings class="col-span-2 xl:col-span-1 max-lg:my-2"/>
    <InputOutput class="col-span-2  max-lg:my-2"/>
    </div> 
    </ClientOnly>
  </html>
  </template>