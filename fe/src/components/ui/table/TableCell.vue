<script setup>
import { cn } from '@/lib/utils';

const props = defineProps({
	class: { type: null, required: false },
});
</script>

<template>
	<td
		:class="
			cn(
				'h-14 px-4 group-hover:bg-gray-100 align-middle [&:has([role=checkbox])]:pr-0',
				props.class,
			)
		"
	>
		<slot />
	</td>
</template>
