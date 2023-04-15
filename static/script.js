/* -----Functions for handling responses----- */

function handleSetTable(response) {
	$("#results").html(response);
}

function handleError(err) {
	console.log("Error:", err);
}

/* -----Functions for API requests----- */

function getDateTime() {
	let dateTime = new Date();
	$("#dateTime").html(dateTime.toLocaleString()); //Set the html to the current time
}

let request_results = null;

function getTableResults() {
	let label = $("#label-input").val();
	let agent = $("#agent-input").val();
	let classifier = $("#classifier-input").val();
	let dep = $("#dep-input").val();

	label = encodeURIComponent(label);
	classifier = encodeURIComponent(classifier);
	agent = encodeURIComponent(agent);
	dep = encodeURIComponent(dep);

	let url = `/searchresults?l=${label}&c=${classifier}&a=${agent}&d=${dep}`;

	if (request_results != null) {
		request_results.abort();
	}

	request = $.ajax({
		type: "GET",
		url: url,
		success: handleSetTable,
		error: handleError,
	});
}

function setup() {
	getDateTime();
	$("#label-input").on("input", getTableResults);
	$("#agent-input").on("input", getTableResults);
	$("#classifier-input").on("input", getTableResults);
	$("#dep-input").on("input", getTableResults);
}

$("document").ready(setup); //start at setup
