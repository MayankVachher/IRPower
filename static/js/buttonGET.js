addEventListener("DOMContentLoaded", function() {
	var button = document.getElementById('anotherButton');
	button.addEventListener("click", function(e) {
		e.preventDefault();
		console.log("Hello!");
		var request = new XMLHttpRequest();
		request.open("GET", "/", true);
		request.send();
		console.log(request);
	});
}, true);