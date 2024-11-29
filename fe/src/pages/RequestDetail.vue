<script setup>
  import { useAuthStore } from '@/stores/useAuth';
  
  import ApproveDetail from '@/components/decentralization/ApproveDetail.vue'
  import RequestDetail from '@/components/decentralization/RequestDetail.vue'

  import { isApprove } from '@/utils'

  const authStore = useAuthStore() 
</script>

<template>
  <RequestDetail v-if="authStore?.user?.skylight === 'req'"/>
  <ApproveDetail :user="authStore?.user" v-if="isApprove(authStore?.user?.skylight)"/>
</template>