export const getDaysOFMonth = () => new Date(0, new Date().getMonth() + 1, 0).getDate();

export const getYear = () => new Date().getFullYear()
export const getMonthName = () => new Date(0, new Date().getMonth()).toLocaleString('default', { month: 'long' });

export const listNumberBefore = (number) => [...Array(number).keys()];

export const gettwentyfourHours = () => Array.from(Array(24).keys());