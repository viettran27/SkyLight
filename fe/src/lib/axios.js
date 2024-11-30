import axios from 'axios';
import { useAuthStore } from '@/stores/useAuth';

export const axiosClient = axios.create({
	baseURL: `${import.meta.env.VITE_API}/v1`,
	headers: {
		'Content-Type': 'application/json',
	},
});

axiosClient.interceptors.request.use(
	(config) => {
		const authStore = useAuthStore();
		if (authStore.accessToken) {
			config.headers.Authorization = `Bearer ${authStore.accessToken}`;
		}
		return config;
	},
	(error) => {
		return Promise.reject(error);
	},
);

axiosClient.interceptors.response.use(
	(response) => response.data,
	async (error) => {
		const authStore = useAuthStore();
		if (
			error.response?.status === 401 &&
			error.response?.data?.detail === 'access_token hết hạn'
		) {
			try {
				const refreshToken = localStorage.getItem('refresh_token');
				if (refreshToken) {
					const refreshResponse = await axiosClient.post(
						'/auth/refresh',
						{ refresh_token: refreshToken },
					);
					authStore.setAccessToken(refreshResponse.access_token);
					error.config.headers.Authorization = `Bearer ${refreshResponse.access_token}`;
					return axiosClient.request(error.config);
				} else {
					authStore.logout();
					window.location.href = '/login';
				}
			} catch (refreshError) {
				authStore.logout();
				window.location.href = '/login';
				return Promise.reject(refreshError);
			}
		}
	},
);
