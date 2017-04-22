/**
 * Created by pati on 22.04.17.
 */
window.onload = function () {

		var chart = new CanvasJS.Chart("chartContainer",
		{
			theme: "theme3",
                        animationEnabled: true,
			title:{
				text: "Global statistics by day",
				fontSize: 30
			},
			toolTip: {
				shared: true
			},
			axisY: {
				title: "Amount of client in one day"
			},
			axisY2: {
				title: "Time spend in shop by all clients"
			},
			data: [
			{
				type: "column",
				name: "Amount of client in one day",
				legendText: "Clients",
				showInLegend: true,
				dataPoints: arr
			},
			{
				type: "column",
				name: "Time spend in shop by all clients in minutes",
				legendText: "Time",
				axisYType: "secondary",
				showInLegend: true,
				dataPoints: arr2
			}

			],
          legend:{
            cursor:"pointer",
            itemclick: function(e){
              if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
              	e.dataSeries.visible = false;
              }
              else {
                e.dataSeries.visible = true;
              }
            	chart.render();
            }
          },
        });

chart.render();
}