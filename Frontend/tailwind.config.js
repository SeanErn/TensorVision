/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./node_modules/flowbite.{js,ts}"
  ],
  theme: {
    extend: {
      gridTemplateColumns: {
        'dropdownGrid': '25% 1fr'
      },
    }
  },
  daisyui: {
    themes: [
      {
        alotobots : {
            "primary": "#dc2626",          
            "secondary": "#fee2e2",          
            "accent": "#e11d48",         
            "neutral": "#2a323c",         
            "base-100": "#3f3f46", 
            "base-200": "#27272a",
            "base-300": "#18181b",          
            "info": "#3abff8",          
            "success": "#36d399",              
            "warning": "#fbbd23",           
            "error": "#f87272",
                     }
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
}
