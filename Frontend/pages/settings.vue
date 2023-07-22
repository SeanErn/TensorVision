<template>
  <html class="bg-zinc-900 min-h-full" data-theme="alotobots">

  <head>
    <meta charset="utf-8">
    <meta name="color-scheme" content="dark" />
    <title>Tensor Vision - Home</title>
  </head>
  <ClientOnly>
    <div class="m-4 gap-4 flex flex-col justify-center items-center">
      <div class="container place-content-center rounded-md bg-base-200 p-3 xl:h-full w-full mb-auto">
        <h1 class="font-bold text-2xl pb-2">General</h1>
        <Button title="Export Settings" type="bg-base-300" />
        <Button title="Import Settings" type="bg-base-300" />
      </div>
      <div class="container place-content-center rounded-md bg-base-200 p-3 xl:h-full w-full mb-auto">
        <h1 class="font-bold text-2xl pb-2">Networking</h1>
        <hr>
        <br>
        <h2 class="font-bold text-xl pb-2">IP Address</h2>
        <div class="flex items-center gap-3">
          <input id='dhcp' type="radio" name="radio-1" class="radio" checked v-on:change="isDHCPSelected = true" />
          <label for="dhcp">DHCP</label>
          <input id="static" type="radio" name="radio-1" class="radio" v-on:change="isDHCPSelected = false"/>
          <label for="static">Static</label>
        </div>
        <div v-if="!isDHCPSelected" class="flex items-center gap-3 mt-4">
          <label for="ip">IP Address</label>
          <input id="ip" type="text" placeholder="Ex: 192.16.2.1" class="input input-bordered w-full max-w-xs" />
        </div>
        <div class="flex items-center gap-3 mt-4">
          <label for="ip">Hostname</label>
          <input id="ip" type="text" placeholder="tensorvision" value="tensorvision" class="input input-bordered w-full max-w-xs" />
        </div>
        <div class="flex items-center gap-3 mt-4">
          <label for="ip">Team Number</label>
          <input id="ip" type="number" value="0" class="input input-bordered w-full max-w-xs" />
        </div>
      </div>
    </div>
  </ClientOnly>

  </html>
</template>

<script>
export default {
  data() {
    return {
      isDHCPSelected: true
    }
  }
}
</script>
  