import { useAuthStore } from "@/stores/useAuth";

export const canEdit = (status) => {
  const authStore = useAuthStore();

  return authStore.user?.skylight && 
  ( 
    (
      status === 'Đang đợi trưởng bộ phận duyệt' ||
      status === 'Đang đợi kế toán duyệt'
    ) &&
    authStore.user?.skylight === 'req'
  )
  ||
  (
    status === 'Đang đợi kế toán trưởng duyệt' &&
    authStore.user?.skylight === 'acct'
  )
}

export const isApprove = (auth) => {
  return auth === "hod" ||
  auth === "ca" ||
  auth === "dir"
}

export const statusFit = (auth) => {
  const status = {
    "hod": "Đang đợi trưởng bộ phận duyệt",
    "acct": "Đang đợi kế toán duyệt",
    "ca": "Đang đợi kế toán trưởng duyệt",
    "dir": "Đang đợi duyệt cuối cùng"
  }

  return status[auth]
}