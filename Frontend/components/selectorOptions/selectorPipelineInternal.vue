<template>
    <div>
      <p v-for="message in messages" :key="message.id">{{ message?.content }}</p>
    </div>
  </template>
  
  <script lang="ts">
  export default {
    data() {
      return {
        socket: null as WebSocket | null, // make sure to initialize socket as null
        messages: [],
      };
    },
    mounted() {
      this.socket = new WebSocket('wss://example.com');
  
      this.socket?.addEventListener('open', () => {
        console.log('WebSocket connection established');
      });
  
      this.socket?.addEventListener('message', (event) => {
        const message = JSON.parse(event.data);
        this.messages.push(message);
      });
  
      this.socket?.addEventListener('close', (event) => {
        console.log(`WebSocket connection closed with code ${event?.code}`);
      });
  
      this.socket?.addEventListener('error', (event) => {
        console.error(`WebSocket error: ${event}`);
      });
    },
  };
  </script>
  