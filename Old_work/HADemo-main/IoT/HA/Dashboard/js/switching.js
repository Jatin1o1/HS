
// ============ ON/OFF States =============

function addoned(element) {
  element.classList.add("oned");
  let led = element.firstElementChild.firstElementChild;
  led.style.backgroundColor = "#21c900";
}

function removeoned(element) {
  element.classList.remove("oned");
  let led = element.firstElementChild.firstElementChild;
  led.style.backgroundColor = "#c90000";
}


function lock() {
	var x = document.querySelector("#lock > span> status");
	let led = document.querySelector("#lock").firstElementChild.firstElementChild;
  if (x.innerHTML === "Locked") {
      x.innerHTML = "Unlocked";
      document.getElementById("unlockico").style.display = "block";
      document.getElementById("lockico").style.display = "none";
			led.style.backgroundColor = "#c90000";
			pywebview.api.lock("0:0");
  } else {
      x.innerHTML = "Locked";
      document.getElementById("unlockico").style.display = "none";
			document.getElementById("lockico").style.display = "block";
			led.style.backgroundColor = "#21c900";
			pywebview.api.lock("0:1");
			
  }
}

// ===============Master BedRoom================

function mbFan() {
  var x = document.querySelector("#mb-fan > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
			removeoned(document.querySelector("#mb-fan"));
			document.getElementById("mbfanico").style.animation = "";
      pywebview.api.mb("1:0");
  } else {
      x.innerHTML = "ON";
			addoned(document.querySelector("#mb-fan"));
			document.getElementById("mbfanico").style.animation = "fan-animation 1s linear infinite";
      pywebview.api.mb("1:1");
  }
}

function mbSocket() {
  var x = document.querySelector("#mb-socket > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mb-socket"));
      pywebview.api.mb("2:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mb-socket"));
      pywebview.api.mb("2:1");
  }
}

function mbBulb() {
  var x = document.querySelector("#mb-bulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mb-bulb"));
      pywebview.api.mb("3:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mb-bulb"));
      pywebview.api.mb("3:1");
  }
}

function mbNbulb() {
  var x = document.querySelector("#mb-nbulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mb-nbulb"));
      pywebview.api.mb("4:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mb-nbulb"));
      pywebview.api.mb("4:1");
  }
}


// =================Drawing Room================

function drFan() {
  var x = document.querySelector("#dr-fan > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
			removeoned(document.querySelector("#dr-fan"));
			document.getElementById("drfanico").style.animation = "";
      pywebview.api.dr("1:0");
  } else {
      x.innerHTML = "ON";
			addoned(document.querySelector("#dr-fan"));
			document.getElementById("drfanico").style.animation = "fan-animation 1s linear infinite";
      pywebview.api.dr("1:1");
  }
}

function drSocket() {
  var x = document.querySelector("#dr-socket > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#dr-socket"));
      pywebview.api.dr("2:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#dr-socket"));
      pywebview.api.dr("2:1");
  }
}

function drBulb() {
  var x = document.querySelector("#dr-bulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#dr-bulb"));
      pywebview.api.dr("3:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#dr-bulb"));
      pywebview.api.dr("3:1");
  }
}

function drShowLights() {
  var x = document.querySelector("#dr-showlights > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#dr-showlights"));
      pywebview.api.dr("4:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#dr-showlights"));
      pywebview.api.dr("4:1");
  }
}

function drClset1() {
  var x = document.querySelector("#dr-clset1 > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#dr-clset1"));
      pywebview.api.dr("5:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#dr-clset1"));
      pywebview.api.dr("5:1");
  }
}

function drClset2() {
  var x = document.querySelector("#dr-clset2 > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#dr-clset2"));
      pywebview.api.dr("6:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#dr-clset2"));
      pywebview.api.dr("6:1");
  }
}

function drNbulb() {
  var x = document.querySelector("#dr-nbulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#dr-nbulb"));
      pywebview.api.dr("7:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#dr-nbulb"));
      pywebview.api.dr("7:1");
  }
}

// ============ Jatin's Room==============

function jrSocket() {
  var x = document.querySelector("#jr-socket > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#jr-socket"));
      pywebview.api.jr("1:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#jr-socket"));
      pywebview.api.jr("1:1");
  }
}

function jrBulb() {
  var x = document.querySelector("#jr-bulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#jr-bulb"));
      pywebview.api.jr("2:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#jr-bulb"));
      pywebview.api.jr("2:1");
  }
}

function jrClset1() {
  var x = document.querySelector("#jr-clset1 > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#jr-clset1"));
      pywebview.api.jr("3:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#jr-clset1"));
      pywebview.api.jr("3:1");
  }
}

function jrClset2() {
  var x = document.querySelector("#jr-clset2 > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#jr-clset2"));
      pywebview.api.jr("4:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#jr-clset2"));
      pywebview.api.jr("4:1");
  }
}

function jrNbulb() {
  var x = document.querySelector("#jr-nbulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#jr-nbulb"));
      pywebview.api.jr("5:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#jr-nbulb"));
      pywebview.api.jr("5:1");
  }
}



// =================== Megha's Room ===================

function mrFan() {
  var x = document.querySelector("#mr-fan > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
			removeoned(document.querySelector("#mr-fan"));
			document.getElementById("mrfanico").style.animation = "";
      pywebview.api.mr("1:0");
  } else {
      x.innerHTML = "ON";
			addoned(document.querySelector("#mr-fan"));
			document.getElementById("mrfanico").style.animation = "fan-animation 1s linear infinite";
      pywebview.api.mr("1:1");
  }
}

function mrSocket() {
  var x = document.querySelector("#mr-socket > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mr-socket"));
      pywebview.api.mr("2:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mr-socket"));
      pywebview.api.mr("2:1");
  }
}

function mrTubeLight() {
  var x = document.querySelector("#mr-tubelight > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mr-tubelight"));
      pywebview.api.mr("3:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mr-tubelight"));
      pywebview.api.mr("3:1");
  }
}

function mrBulb() {
  var x = document.querySelector("#mr-bulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mr-bulb"));
      pywebview.api.mr("4:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mr-bulb"));
      pywebview.api.mr("4:1");
  }
}

function mrNbulb() {
  var x = document.querySelector("#mr-nbulb > span > status");
  if (x.innerHTML === "ON") {
      x.innerHTML = "OFF";
      removeoned(document.querySelector("#mr-nbulb"));
      pywebview.api.mr("5:0");
  } else {
      x.innerHTML = "ON";
      addoned(document.querySelector("#mr-nbulb"));
      pywebview.api.mr("5:1");
  }
}