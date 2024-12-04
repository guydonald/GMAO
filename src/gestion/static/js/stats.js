const renderChart = (data, labels) => {

	const ctx = document.getElementById('myChart');

	new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: labels,
			datasets: [{
				label: 'Last 6 months expenses',
				data: data,
				borderWidth: 1
			}]
		},
		options: {
			plugins: {
				title: {
					display: true,
					text: 'Expenses per category',
					font: {
						size: 20
					},
					padding: {
						top: 30,
						bottom: 30
					}
				}
			}
		}
	});
};
const getChartData = () => {
	console.log('fetching');
	fetch('expense_category_summary').then(res => res.json()).then(results => {
		console.log("results", results);
		const category_data = results.expense_category_data;
		const [labels, data] = [Object.keys(category_data), Object.values(category_data)];
		renderChart(data, labels);
	});
};

document.onload = getChartData();