<template>
    <div class="rounded-md overflow-hidden relative w-1/2 shadow-md">
        <img src="~assets/img/ex1.jpg"/>
        <div class="absolute bottom-0 w-full opacity-60 bg-base-200 px-3 py-2 text-lg">
            <h1>Raw</h1>
            <h1 class="align-right">FPS: {{ data.camera.fps }}</h1>
        </div>
    </div>
</template>

<script setup>
// var {data : fps} = await useFetch('')
// Example before backend is set up
var data = {
    "camera":{
        "fps":60
    }
}
</script>
