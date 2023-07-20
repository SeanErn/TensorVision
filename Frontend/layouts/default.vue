<template>
<div class="flex max-h-screen max-w-screen" data-theme="alotobots">
   <aside id="default-sidebar sticky"
      class="z-40 h-screen overflow-visible"
      aria-label="Sidebar">
      <div class="h-full px-3 py-4 bg-zinc-800 shadow-xl flex flex-col">
         <!-- <img class="py-4" src="~assets/img/tensorVisionLogo.png"/> -->
         <div class="lg:tooltip-right lg:tooltip z-50 my-1" data-tip="Camera Stream">
            <NuxtLink to="/" class="btn btn-primary btn-square">
               <svg aria-hidden="true"
                  class="w-6 h-6 text-gray-300 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white "
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path
                     d="M3.25 4A2.25 2.25 0 001 6.25v7.5A2.25 2.25 0 003.25 16h7.5A2.25 2.25 0 0013 13.75v-7.5A2.25 2.25 0 0010.75 4h-7.5zM19 4.75a.75.75 0 00-1.28-.53l-3 3a.75.75 0 00-.22.53v4.5c0 .199.079.39.22.53l3 3a.75.75 0 001.28-.53V4.75z">
                  </path>
               </svg>
            </NuxtLink>
         </div>
         <div class="lg:tooltip-right lg:tooltip z-50 my-1" data-tip="Models + Pipelines">
            <NuxtLink to="/models_pipelines" class="btn btn-ghost btn-square">
               <svg aria-hidden="true"
                  class="flex-shrink-0 w-6 h-6 text-gray-300 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2 3a1 1 0 00-1 1v1a1 1 0 001 1h16a1 1 0 001-1V4a1 1 0 00-1-1H2z"></path>
                  <path clip-rule="evenodd"
                     d="M2 7.5h16l-.811 7.71a2 2 0 01-1.99 1.79H4.802a2 2 0 01-1.99-1.79L2 7.5zM7 11a1 1 0 011-1h4a1 1 0 110 2H8a1 1 0 01-1-1z"
                     fill-rule="evenodd"></path>
               </svg>
               <!-- NOTIFICATION ICON <span class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-200 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
            </NuxtLink>
         </div>
         <div class="lg:tooltip-right lg:tooltip z-50 my-1" data-tip="Device Settings">
            <NuxtLink to="/settings" class="btn btn-ghost btn-square">
               <svg aria-hidden="true"
                  class="flex-shrink-0 w-6 h-6 text-gray-300 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path
                     d="M10 3.75a2 2 0 10-4 0 2 2 0 004 0zM17.25 4.5a.75.75 0 000-1.5h-5.5a.75.75 0 000 1.5h5.5zM5 3.75a.75.75 0 01-.75.75h-1.5a.75.75 0 010-1.5h1.5a.75.75 0 01.75.75zM4.25 17a.75.75 0 000-1.5h-1.5a.75.75 0 000 1.5h1.5zM17.25 17a.75.75 0 000-1.5h-5.5a.75.75 0 000 1.5h5.5zM9 10a.75.75 0 01-.75.75h-5.5a.75.75 0 010-1.5h5.5A.75.75 0 019 10zM17.25 10.75a.75.75 0 000-1.5h-1.5a.75.75 0 000 1.5h1.5zM14 10a2 2 0 10-4 0 2 2 0 004 0zM10 16.25a2 2 0 10-4 0 2 2 0 004 0z">
                  </path>
               </svg>
            </NuxtLink>
         </div>
         <div class="lg:tooltip-right lg:tooltip z-50 my-1" data-tip="Docs">
            <!--<span class="inline-flex items-center justify-center w-3 h-3 p-3 ml-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">3</span>-->
            <NuxtLink to="/docs" class="btn btn-ghost btn-square">
               <svg aria-hidden="true"
                  class="flex-shrink-0 w-6 h-6 text-gray-300 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path
                     d="M10.75 16.82A7.462 7.462 0 0115 15.5c.71 0 1.396.098 2.046.282A.75.75 0 0018 15.06v-11a.75.75 0 00-.546-.721A9.006 9.006 0 0015 3a8.963 8.963 0 00-4.25 1.065V16.82zM9.25 4.065A8.963 8.963 0 005 3c-.85 0-1.673.118-2.454.339A.75.75 0 002 4.06v11a.75.75 0 00.954.721A7.506 7.506 0 015 15.5c1.579 0 3.042.487 4.25 1.32V4.065z">
                  </path>
               </svg>
            </NuxtLink>
         </div>

      </div>
   </aside>
   <div class="overflow-x-scroll bg-zinc-900 ">
   <slot/>
</div>
</div>
</template>
