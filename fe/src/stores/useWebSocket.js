import { defineStore } from "pinia";
import { useAuthStore } from "./useAuth";

export const useWebSocketStore = defineStore("websocket", {
  state: () => ({
    socket: null,
    notifications: {}, 
    isConnected: false, 
  }),
  actions: {
    connect() {
      if (!this.socket) {
        const authStore = useAuthStore();
        this.socket = new WebSocket(`ws://${import.meta.env.VITE_SOCKET}/ws?token=${authStore.accessToken}`);

        this.socket.onopen = () => {
          this.isConnected = true;
          console.log("WebSocket connected");
        };

        this.socket.onmessage = (event) => {
          console.log("Received message:", event.data);
          const data = JSON.parse(event.data);
          this.addNotification(data);
        };

        this.socket.onclose = () => {
          this.isConnected = false;
          console.log("WebSocket disconnected");
          this.socket = null;
        };

        this.socket.onerror = (error) => {
          console.error("WebSocket error:", error);
        };
      }
    },
    disconnect() {
      if (this.socket) {
        this.socket.close();
        this.socket = null;
        this.isConnected = false;
      }
    },
    addNotification(notification) {
      this.notifications = notification;
      console.log(this.notifications)
    },
    clearNotifications() {
      this.notifications = {};
    },
  },
});
