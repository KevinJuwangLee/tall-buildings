var mainChart = document.getElementsByClassName("amcharts-graph-g1")[1];
var gElements = mainChart.querySelectorAll('circle');

var GDPs = [];
for(let i = 35; i < gElements.length; i++) {
    GDPs.push(parseFloat(gElements[i].getAttribute('aria-label').substring(6).replace(',','')));
}