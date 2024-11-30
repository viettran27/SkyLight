export const formatISODate = (isoDate) => {
	if (!isoDate) return '';

	const date = new Date(isoDate);

	const day = String(date.getDate()).padStart(2, '0');
	const month = String(date.getMonth() + 1).padStart(2, '0');
	const year = date.getFullYear();
	const hours = String(date.getHours()).padStart(2, '0');
	const minutes = String(date.getMinutes()).padStart(2, '0');

	return `${day}/${month}/${year} ${hours}:${minutes}`;
};

export const formatDate = (i_date) => {
	if (!i_date) return '';

	const date = new Date(i_date);

	const day = String(date.getDate()).padStart(2, '0');
	const month = String(date.getMonth() + 1).padStart(2, '0');
	const year = date.getFullYear();

	return `${day}/${month}/${year}`;
};
