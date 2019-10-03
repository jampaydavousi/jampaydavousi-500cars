/* data route */
var url = "/chart";


function buildPlot() {
  d3.json(url).then((data) => {
    
    // console.log(data.Price);
    // console.log(data.Mileage);
    var chart = c3.generate({
      bindto: '#scatter',
      point: {
        r: 5
    },
        data: {
          x: "Mileage",
            columns: [
              data.Depreciation,
              data.Mileage,
            ],
            type: 'scatter',
          point: {
            focus: {
                expand: {
                    enabled: true
                }
            }
          },
        },
        axis: {
            x: {
                label: 'Mileage',
                tick: {
                  fit: false
              }
                },
            y: {
              label: 'Depreciation'
            }
        },

      });
  d3.selectAll(".c3-circle").style("fill", function(d, i) {
         
    abc = (d.x+d.value);
        
function numberSum(N) {
 var total = 0;
   for(var i = 1; i <= N; i++){
     total += i;
   }
   return total;
}        
        console.log("total " +numberSum(abc));
        console.log("i -" +i);
 return i % 2 ? "#ff0000" : "#ff0000";
     });
});

}

buildPlot();







