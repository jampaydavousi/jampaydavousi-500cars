
function buildCharts(sample) {
  d3.json(`/samples/${sample}`).then((data) => {
    console.log(data);
    const Price = data.Price;
    const Year = data.Year;
    const MSRP = data.MSRP;
    const Latitude = data.Latitude;
    const Longitude = data.Longitude;
    const Mileage = data.Mileage;
    const City = data.City;
    const Depreciation = data.Depreciation;


    // Build a Bubble Chart
    var chartLayout = {
      margin: { t: 0 },
      hovermode: "closest",
      xaxis: {
        showticklabels: true,
        title: {
          text: 'Mileage'}
    },
    yaxis: {
      title: {
        text: 'Depreciation (%)'}
      }
    };
    var chartData = [
      {
        x: Mileage,
        y: Depreciation,
        text: City,
        mode: "markers",
        marker: {
          size: 20,
          color: Mileage,
          colorscale: "Viridis"
        }
      }
    ];


    Plotly.newPlot("chart", chartData, chartLayout);



  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDatasetNew");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
  });
}


function optionChangedDep(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
}

// Initialize the dashboard
init();
