import { createRouter, createWebHistory } from 'vue-router';
import Auth from '@/pages/Auth.vue';
import { ProtectedRoute } from '@/components/protected-route';
import { Layout } from '@/components/layout';

const routesConfig = [
	{ path: '/requests', component: () => import('@/pages/Request.vue') },
	{ path: '/requests/:id', component: () => import('@/pages/RequestDetail.vue') },
	{ path: '/responses', component: () => import('@/pages/Response.vue') },
	{
		path: '/automatic_salary',
		component: () => import('@/pages/AutomaticSalary.vue'),
	},
	{
		path: '/manage_wallet',
		component: () => import('@/pages/ManageWallet.vue'),
	},
];

const routes = [
	{
		path: '/login',
		component: Auth,
	},
	{
		redirect: '/requests'
	},
	{
		path: '/',
		component: ProtectedRoute,
		children: [
			{
				path: '',
				component: Layout,
				children: routesConfig.map((route) => ({
					path: route.path,
					component: route.component,
				})),
			},
		],
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
