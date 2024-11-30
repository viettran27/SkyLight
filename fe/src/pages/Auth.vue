<script setup>
import { axiosClient } from '@/lib/axios';
import { useRouter } from 'vue-router';
import { reactive } from 'vue';
import { cn } from '@/lib/utils';
import { buttonVariants } from '@/components/ui/button';
import { useAuthStore } from '@/stores/useAuth';

const loginValue = reactive({
	macongty: 'NT1',
	masothe: '',
	matkhau: '',
});
const router = useRouter();
const authStore = useAuthStore();

const handleLogin = () => {
	axiosClient
		.post('auth/login', loginValue, { withCredentials: true })
		.then((response) => {
			localStorage.setItem('refresh_token', response.refresh_token);
			authStore.setAccessToken(response.access_token);
			authStore.setUser(response.user);
			router.push('/requests');
		});
};
</script>

<template>
	<div
		class="fixed top-0 bottom-0 left-0 right-0 bg-black bg-opacity-40 flex justify-center items-center"
	>
		<div class="bg-white min-w-[600px] rounded-2xl pt-5 pb-16 px-16">
			<form @submit.prevent="handleLogin" class="flex flex-col gap-7">
				<h1 class="text-center font-bold">Đăng nhập</h1>
				<div>
					<label>Nhà máy</label>
					<Select
						:defaultValue="loginValue.macongty"
						v-model="loginValue.macongty"
					>
						<SelectTrigger class="mt-1">
							<SelectValue placeholder="Chọn nhà máy" />
						</SelectTrigger>
						<SelectContent>
							<SelectGroup>
								<SelectItem value="NT1">NT1</SelectItem>
								<SelectItem value="NT2">NT2</SelectItem>
							</SelectGroup>
						</SelectContent>
					</Select>
				</div>

				<div>
					<label>Mã số thẻ</label>
					<Input
						class="mt-1"
						v-model="loginValue.masothe"
						placeholder="Mã số thẻ"
					/>
				</div>

				<div>
					<label>Mật khẩu</label>
					<Input
						class="mt-1"
						v-model="loginValue.matkhau"
						placeholder="Nhập mật khẩu"
						type="password"
					/>
				</div>

				<input
					type="submit"
					value="Đăng nhập"
					:class="cn(buttonVariants({ variant: 'default' }), 'mt-3')"
				/>
			</form>
		</div>
	</div>
</template>
