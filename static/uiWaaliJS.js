var range = document.getElementById('range');

noUiSlider.create(range, {
		start: 0,
		connect: 'lower',
		orientation: "vertical",
		step: 5,
		behaviour: 'tap-drag',
		range: {
			'min': 0,
			'max': 100
		},
		pips: { // Show a scale with the slider
			mode: 'steps',
			density: 2
		}
});
var prev = range.noUiSlider.get();
prev = Math.round(prev);
document.getElementById("thresh_"+prev.toString()).style.display = "block";

range.noUiSlider.on('update', function( values, handle ) {
	document.getElementById("thresh_"+prev.toString()).style.display = "none";
	prev = Math.round(values[handle]);
	document.getElementById("thresh_"+prev.toString()).style.display = "block";
});
