export const viewMoney = (money) => {
	if (!money) return '';
	return money?.toLocaleString('vi-VN', {
		style: 'currency',
		currency: 'VND',
	});
};