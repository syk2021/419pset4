/* -----Functions for API requests----- */

function getDateTime() {
	let dateTime = new Date();
	$("#dateTime").html(dateTime.toLocaleString()); //Set the html to the current time
}

function setup() {
	getDateTime();
}

$("document").ready(setup); //start at setup
