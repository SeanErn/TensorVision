const io = require("sails.io.js")(require("socket.io-client"));

io.sails.url = "ws://127.0.0.1:5000";

export default (context, inject) => {
  // You can listen to WebSocket events here
    console.log("INIT SOCKET")
  inject("io", io);
};