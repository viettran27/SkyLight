import { defineStore } from 'pinia';
import { FILTER } from '../constants';

export const useFilterStore = defineStore('filter', {
	state: () => ({
    filter: FILTER.ALL
  }),
  actions: {
    setFilter(value) {
      this.filter = value;
    },

    reset() {
      this.filter = FILTER.ALL
    }
  }
});
