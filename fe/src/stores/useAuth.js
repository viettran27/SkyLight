import { defineStore } from "pinia";
import { axiosClient } from "@/lib/axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    accessToken: localStorage.getItem("access_token") || null,
    user: null
  }),
  actions: {
    setAccessToken(token) {
      this.accessToken = token;
      localStorage.setItem("access_token", token);
    },
    setUser(userInfo) {
      this.user = userInfo;
    },
    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      this.accessToken = null;
      this.user = null;
    },
    async getMe() {
      if (!this.accessToken) {
        return null;
      }
      try {
        const response = await axiosClient.get("/auth/me");
        this.setUser(response.data);
        return response.data;
      } catch (error) {
        return null;
      }
    },
  },
});
