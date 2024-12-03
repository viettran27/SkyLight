import { createApp } from 'vue';
import './assets/index.css';
import App from './App.vue';
import { Input } from '@/components/ui/input';
import MoneyInput from '@/components/ui-custom/MoneyInput.vue';
import { Button } from '@/components/ui/button';
import {
	Select,
	SelectContent,
	SelectGroup,
	SelectItem,
	SelectLabel,
	SelectTrigger,
	SelectValue,
} from '@/components/ui/select';
import {
	Collapsible,
	CollapsibleContent,
	CollapsibleTrigger,
} from '@/components/ui/collapsible';
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import {
	Table,
	TableBody,
	TableCaption,
	TableCell,
	TableHead,
	TableHeader,
	TableRow,
} from '@/components/ui/table';
import {
	Dialog,
	DialogContent,
	DialogDescription,
	DialogFooter,
	DialogHeader,
	DialogTitle,
	DialogClose,
	DialogTrigger,
} from '@/components/ui/dialog';
import { Textarea } from '@/components/ui/textarea';
import {
  Pagination,
  PaginationEllipsis,
  PaginationFirst,
  PaginationLast,
  PaginationList,
  PaginationListItem,
  PaginationNext,
  PaginationPrev,
} from '@/components/ui/pagination'

import router from './router';
import { createPinia } from 'pinia';

const app = createApp(App);
const pinia = createPinia();

app.component('Input', Input);
app.component('MoneyInput', MoneyInput);
app.component('Button', Button);
app.component('Select', Select);
app.component('SelectContent', SelectContent);
app.component('SelectGroup', SelectGroup);
app.component('SelectItem', SelectItem);
app.component('SelectLabel', SelectLabel);
app.component('SelectTrigger', SelectTrigger);
app.component('SelectValue', SelectValue);
app.component('Collapsible', Collapsible);
app.component('CollapsibleContent', CollapsibleContent);
app.component('CollapsibleTrigger', CollapsibleTrigger);
app.component('DropdownMenu', DropdownMenu);
app.component('DropdownMenuContent', DropdownMenuContent);
app.component('DropdownMenuItem', DropdownMenuItem);
app.component('DropdownMenuTrigger', DropdownMenuTrigger);
app.component('Table', Table);
app.component('TableBody', TableBody);
app.component('TableCaption', TableCaption);
app.component('TableCell', TableCell);
app.component('TableHead', TableHead);
app.component('TableHeader', TableHeader);
app.component('TableRow', TableRow);
app.component('Dialog', Dialog);
app.component('DialogContent', DialogContent);
app.component('DialogDescription', DialogDescription);
app.component('DialogFooter', DialogFooter);
app.component('DialogHeader', DialogHeader);
app.component('DialogTitle', DialogTitle);
app.component('DialogTrigger', DialogTrigger);
app.component('DialogClose', DialogClose);
app.component('Textarea', Textarea);
app.component('Pagination', Pagination);
app.component('PaginationEllipsis', PaginationEllipsis);
app.component('PaginationFirst', PaginationFirst);
app.component('PaginationLast', PaginationLast);
app.component('PaginationList', PaginationList);
app.component('PaginationListItem', PaginationListItem);
app.component('PaginationNext', PaginationNext);
app.component('PaginationPrev', PaginationPrev);

app.use(router);
app.use(pinia);
app.mount('#app');
