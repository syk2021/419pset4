/* -----Functions for handling responses----- */

/**
 * Take in the response from the GET request and set the #results field in the page as the response.
 * @param  response - response from GET request
 * @return [None]
 */
function handleSetTable(response) {
	$("#results").html(response);
}

/**
 * Take in the error from the GET request and prints out the error in the console.
 * @param  error - error from GET request
 * @return [None]
 */
function handleError(err) {
	console.log("Error:", err);
}

/* -----Functions for backend requests----- */

let request_results = null;

/**
 * Change the #dateTime field to be the current date and time of when the user opened the page.
 * @param  [None]
 * @return [None]
 */
function getDateTime() {
	let dateTime = new Date();
	$("#dateTime").html(dateTime.toLocaleString()); //Set the html to the current time
}

/**
 * Get user input and make a GET request to the backend to query the databse with the specified input.
 * @param  [None]
 * @return [None]
 */
function getTableResults() {
	// Get the user input from the input field
	let label = $("#label-input").val();
	let agent = $("#agent-input").val();
	let classifier = $("#classifier-input").val();
	let dep = $("#dep-input").val();

	//Encode each input as a URI components
	label = encodeURIComponent(label);
	classifier = encodeURIComponent(classifier);
	agent = encodeURIComponent(agent);
	dep = encodeURIComponent(dep);

	let url = `/search?l=${label}&c=${classifier}&a=${agent}&d=${dep}`;

	if (request_results != null) {
		request_results.abort();
	}

	//Get request to get the table information from the backend
	request = $.ajax({
		type: "GET",
		url: url,
		success: handleSetTable,
		error: handleError,
	});
}

/**
 * Have each input field called getTableResults() upon user input, and initially set the day and time.
 * @param  [None]
 * @return [None]
 */
function setup() {
	getDateTime();
	$("#label-input").on("input", getTableResults);
	$("#agent-input").on("input", getTableResults);
	$("#classifier-input").on("input", getTableResults);
	$("#dep-input").on("input", getTableResults);
}

$("document").ready(setup); //start at setup
