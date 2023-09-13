import { pipeline } from "stream";


export default defineNuxtPlugin((nuxtApp) => {
    if (!process.client) return;
    
    const socket = new WebSocket("ws://127.0.0.1:5803");

    var receivedPipelineConfig = 'hello';
      socket.addEventListener("open", (event) => {
        console.log("WebSocket connection opened:", event);
        let payload = JSON.stringify({
          type: "getCurrentPipeline",
          data: {}
        });
        socket.send(payload);
      });
  
      socket.addEventListener("message", function (event) {
        const receivedData = JSON.parse(event.data);
  
        switch (receivedData.type) {
          case "getCurrentPipeline":
            socket.send(
              JSON.stringify({
                type: "getPipelineConfig",
                data: { pipelineName: receivedData.data.pipelineName },
              })
            );
            break;
          case "getPipelineConfig":
            receivedPipelineConfig = JSON.parse(receivedData.data.pipelineConfig);

          default:
            console.log("Unknown message type:", receivedData.type);
            break;
        }
      });
  
      // Add the socket object to the app context
    return {
        provide: {
            socket: socket,
            pipelineConfig: receivedPipelineConfig
        }
    }
  });
  
