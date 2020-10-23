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
				<div class="resultRank">${option[5]}</div>
				<div class="resultRank">${option[7]}</div>
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
	document.getElementById("results").insertAdjacentHTML("beforeend", result);
	document.getElementById
}

function updateResults(jsonResults) {
	list = JSON.parse(jsonResults);
	list.forEach( (result, index) => {
		console.log(index);
		addOptionToResults(result);
	} );
}

function getDeps() {
	document.getElementById("resultsLabel").hidden = false;
	document.getElementById("results").hidden = false;
	document.getElementById("results").innerHTML = "";
	data = { 
		advRank: document.getElementById("rank").value,
		category: "OPEN",
		gender: "Female-only",
		prepRL: 0
	}

	xhttp = new XMLHttpRequest();
	xhttp.open("POST", "api/getdeps", true);
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
	console.log("adv options clicked");
}
