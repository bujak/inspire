window.onload = function () {
          var chart = new CanvasJS.Chart("chartContainer", {
              data: [
              {
                  type: "column",
                  dataPoints: [
                  { y: 10, label: "aaa" },
                  { y: 15, label: "bbb" },
                  { y: 25, label: "ccc" },
                  { y: 30, label: "ddd" },
                  { y: 28, label: "fff" }
                  ]
              }
              ]
          });

          chart.render();
      }