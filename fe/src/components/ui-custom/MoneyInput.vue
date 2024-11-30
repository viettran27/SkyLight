<template>
	<input
		type="text"
		:value="formattedValue"
		@input="onInput"
		:class="
			cn(
				'flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed',
				props.class,
			)
		"
	/>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { cn } from '@/lib/utils';

const props = defineProps({
	value: {
		type: [Number, String],
		default: '0',
	},
	class: { type: null, required: false },
});

const emit = defineEmits(['update:props.value']);

const rawValue = ref(Number(props.value));

const formattedValue = computed(() => {
	const value = rawValue.value || 0;
	return value.toLocaleString('vi-VN');
});

function onInput(event) {
	const input = event.target.value;
	const numericValue = input.replace(/[^\d]/g, '');
	rawValue.value = numericValue ? Number(numericValue) : 0;
	emit('update:value', rawValue.value);
}

watch(
	() => props.value,
	(newValue) => {
		rawValue.value = Number(newValue || 0);
	},
);
</script>
