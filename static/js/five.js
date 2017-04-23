window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer",
	{
		title:{
			text: "Time per product",
			verticalAlign: 'top',
			horizontalAlign: 'left'
		},
                animationEnabled: true,
		data: [
		{
			type: "doughnut",
			startAngle:100,
			toolTipContent: "{label}: {y} - <strong>#percent%</strong>",
			indexLabel: "{label} #percent%",
			dataPoints: [
				{  label: "Fiat126", y: 123 },
				{  y: 205, label: "Ferrari" },
				{  y: 198, label: "Audi" }

			]
		}
		]
	});

	var chart2 = new CanvasJS.Chart("chartContainer2",
	{
		title:{
			text: "Clients per product",
			verticalAlign: 'top',
			horizontalAlign: 'left'
		},
                animationEnabled: true,
		data: [
		{
			type: "doughnut",
			startAngle:20,
			toolTipContent: "{label}: {y} - <strong>#percent%</strong>",
			indexLabel: "{label} #percent%",
			dataPoints: [
				{  label: "Fiat126", y: 6 },
				{  y: 3, label: "Ferrari" },
				{  y: 1, label: "Audi" }

			]
		}
		]
	});
	chart.render();
    chart2.render();


}