function setup() {
	var submit = document.getElementById("rank");
	submit.addEventListener("keypress", (e) => {
		if (e.key === "Enter") getDeps();
	} );
}

function addOptionToResults(option) {
	option[0] = option[0].replace("Indian Institute of Technology", "IIT");
	option[1] = option[1].replace("(4 Years Bachelor of Technology)", "(4y)");
	option[1] = option[1].replace("(5 Years Bachelor and Master of Technology (Dual Degree))", "(5y Dual)");

	var result = 
	`<div class="result">
		<div class="resultTable">
			<div class="resultHeader">
				<div class="resultHeaderFiller"></div>
				<div class="resultHeaderPrompt">OR</div>
				<div class="resultHeaderPrompt">CR</div>
			</div>
			<div class="resultMainData">
				<div class="resultInstitute">${option[0]}</div>
				<div class="resultRank">${option[5]}%P%</div>
				<div class="resultRank">${option[7]}%P%</div>
			</div>
		</div>
		<div class="resultFooter">
			<div class="resultDepartment">${option[1]}</div>
			<div class="resultQuota">${option[3]}</div>
		</div>
	</div>`

	if (option[4] == "Female-only") {
		result = result.replaceAll("resultRank", "resultRank female");
	}
	if (option[6] == 1) result = result.replace("%P%", "P");
	else result = result.replace("%P%", "");
	if (option[8] == 1) result = result.replace("%P%", "P");
	else result = result.replace("%P%", "");
	document.getElementById("results").insertAdjacentHTML("beforeend", result);
}

function updateResults(jsonResults) {
	list = JSON.parse(jsonResults);
	list.forEach( (result, index) => {
		addOptionToResults(result);
	} );
}

function getDeps() {
	document.getElementById("resultsLabel").hidden = false;
	document.getElementById("results").hidden = false;
	document.getElementById("results").innerHTML = "";
	data = { 
		advRank: document.getElementById("rank").value,
		category: document.getElementById("category").value,
		gender: document.getElementById("gender").value,
		prepRL: document.getElementById("prepRL").checked ? 1 : 0
	}

	xhttp = new XMLHttpRequest();
	xhttp.open("POST", "../api/getdeps", true);
	xhttp.setRequestHeader("Content-Type", "application/json");
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == XMLHttpRequest.DONE) {
			updateResults(xhttp.responseText);
		}
	}

	xhttp.send(JSON.stringify(data));
}

function getInstiDeps() {
	document.getElementById("resultsLabel").hidden = false;
	document.getElementById("results").hidden = false;
	document.getElementById("results").innerHTML = "";
	var rank = document.getElementById("rank").value;
	data = { 
		institute: document.getElementById("institute").value.replace("IIT", "Indian Institute of Technology"),
		category: document.getElementById("category").value,
		advRank: rank == "" ? "1" : rank,
		gender: document.getElementById("gender").value,
		prepRL: document.getElementById("prepRL").checked ? 1 : 0
	}
	
	xhttp = new XMLHttpRequest();
	xhttp.open("POST", "../api/institute", true);
	xhttp.setRequestHeader("Content-Type", "application/json");
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == XMLHttpRequest.DONE) {
			updateResults(xhttp.responseText);
		}
	}

	xhttp.send(JSON.stringify(data));
}

function showAdvOptions() {
	var advOptions = document.getElementById("advOptions");
	var arrow = document.getElementById("advOptionsButtonArrow")
	if (advOptions.style.maxHeight == 0) {
		// expand
		arrow.classList.remove("right");
		arrow.classList.add("down");
		advOptions.style.maxHeight = advOptions.scrollHeight + "px";
	}
	else {
		// collapse
		arrow.classList.remove("down");
		arrow.classList.add("right");
		advOptions.style.maxHeight = null;
	}
}

function showInstituteSearch() {
	var advOptions = document.getElementById("instiSearch");
	var arrow = document.getElementById("instiSearchButtonArrow")
	if (advOptions.style.maxHeight == 0) {
		// expand
		arrow.classList.remove("right");
		arrow.classList.add("down");
		advOptions.style.maxHeight = advOptions.scrollHeight + "px";
	}
	else {
		// collapse
		arrow.classList.remove("down");
		arrow.classList.add("right");
		advOptions.style.maxHeight = null;
	}
}
