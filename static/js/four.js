window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
      title:{
        text: "All clients statistics"
      },
      animationEnabled: true,
      toolTip: {
        shared: true,
        content: function(e){
          var body ;
          var head ;
          head = "<span style = 'color:DodgerBlue; '><strong>"+ (e.entries[0].dataPoint.x)  + " sec</strong></span><br/>";

          body = "<span style= 'color:"+e.entries[0].dataSeries.color + "'> " + e.entries[0].dataSeries.name + "</span>: <strong>"+  e.entries[0].dataPoint.y + "</strong>  m/s<br/> <span style= 'color:"+e.entries[1].dataSeries.color + "'> " + e.entries[1].dataSeries.name + "</span>: <strong>"+  e.entries[1].dataPoint.y + "</strong>  m";

          return (head.concat(body));
        }
      },
      axisY:{
        title: "Time in shop",
        includeZero: false,
        suffix : " min",
        lineColor: "#369EAD"
      },
      axisY2:{
        title: "Amount of viewed product",
        includeZero: false,
        suffix : "",
        lineColor: "#C24642"
      },
      axisX: {
        title: "Client name",
        suffix : ""
      },
      data: [
      {
        type: "spline",
        name: "amount of products",
        dataPoints: arr
      },
      {
        type: "spline",
        axisYType: "secondary"  ,
        name: "time in minutes",
        dataPoints: arr2
      }
      ]
    });

chart.render();
}