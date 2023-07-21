// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules : [
        '@nuxtjs/tailwindcss'
    ],
    css : [
        '~/assets/scss/default.scss'
    ],
    app : {
        head : {
            link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }],
        }
    },
}
)
