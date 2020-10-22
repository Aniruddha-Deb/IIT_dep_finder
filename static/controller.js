function addOptionToResults(option) {
	option[0] = option[0].replace("Indian Institute of Technology", "IIT");
	option[1] = option[1].replace("(4 Years Bachelor of Technology)", "(4y)");
	option[1] = option[1].replace("(5 Years Bachelor and Master of Technology (Dual Degree))", "(5y Dual)");

	var result = 
	`<div class="result">
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
		<div class="resultDepartment">${option[1]}</div>
	</div>`
	document.getElementById("results").insertAdjacentHTML("beforeend", result);
}

function updateResults(jsonResults) {
	list = JSON.parse(jsonResults);
	list.forEach( (result, index) => {
		console.log(index);
		addOptionToResults(result);
	} );
}

function getDeps() {
	data = { 
		advRank: document.getElementById("rank").value,
		category: "OPEN",
		gender: "Gender-Neutral",
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
