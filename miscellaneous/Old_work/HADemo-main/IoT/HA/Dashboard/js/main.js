document.addEventListener("swiped", function (e) {
  console.log(e.target); // element that was swiped
  console.log(e.detail.dir); // swipe direction
  window.getComputedStyle(document.querySelector(".navbar"), ":hover");
});

function showResponse(response) {
  var container = document.getElementById("response-container");
}

// ============ Date & Time =================

function startTime() {
  var today = new Date(),
    h = today.getHours(),
    m = today.getMinutes(),
    da = today.getDate();
  mo = today.getMonth();
  yr = today.getFullYear();
  mo = monthName(mo);
  //var s = today.getSeconds();
  var mer = checkMeridian(h);
  h = make12hr(h);
  m = checkTime(m);
  //s = checkTime(s);
  txt.innerHTML = "<big>" + h + ":" + m + "</big>" + "<small>" + mer + "</small>"; //":" + s +
  var t = setTimeout(startTime, 500);
  mon.innerHTML = mo + " " + da + "," + " " + yr;
}
function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  } // add zero in front of numbers < 10
  return i;
}

function monthName(mo) {
  //Function to return month Name
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  return months[mo];
}

function make12hr(i) {
  //Converts time to 12hr format
  if (i > 12) {
    i = i - 12;
  }
  return i;
}

function checkMeridian(i) {
  //Checks Meridian
  if (i > 12) {
    i = " PM";
  } else {
    i = " AM";
  }
  return i;
}

// ===================================



// const themeMap = {
//   dark: "light",
//   light: "solar",
//   solar: "dark"
// };

// const theme = localStorage.getItem('theme')
//   || (tmp = Object.keys(themeMap)[0],
//       localStorage.setItem('theme', tmp),
//       tmp);
// const bodyClass = document.body.classList;
// bodyClass.add(theme);

// function toggleTheme() {
//   const current = localStorage.getItem('theme');
//   const next = themeMap[current];

//   bodyClass.replace(current, next);
//   localStorage.setItem('theme', next);
// }

// document.getElementById('themeButton').onclick = toggleTheme;

// const gaugeElement = document.querySelector(".gauge");

function setGaugeValue(value) {
  if (value < 0 || value > 1) {
    return;
  }

  document.querySelector(".gauge__fill").style.transform = `rotate(${value / 2}turn)`;
  document.querySelector(".gauge__cover").innerHTML = `${Math.round(value * 100)}°C`;
}

// function setGVrand() {
//   let value = Math.random();
//   document.querySelector(".gauge__fill").style.transform = `rotate(${value / 2}turn)`;
//   document.querySelector(".gauge__cover").innerHTML = `${Math.round(value * 100)}°C`;
// }

// setInterval(() => {
//   setGVrand();
// }, 500);

function movePageRight() {
  document.querySelector(".page").classList.add("page-slide");
}

function movePageBack() {
  document.querySelector(".page").classList.remove("page-slide");
}

// ================= Buttons ===================

let house = {
  rooms: [
    {
      name: "Master Bedroom",
      appliances: ["fan", "socket", "light", "night bulb"],
      sensors: [],
    },
    {
      name: "Drawing Room",
			appliances: ["fan", "socket", "show lights", "light", "night bulb", "concealed lights 1", "concealed lights 2"],
			sensors: [],
    },
    {
      name: "Jatin's Room",
      appliances: ["socket", "light", "night bulb", "concealed lights 1", "concealed lights 2"],
      sensors: [],
    },
    {
      name: "Megha's Room",
      appliances: ["fan", "socket", "light", "tubelight", "night bulb"],
      sensors: [],
    },
  ],
};

const allbutton = Array.from(document.querySelector(".buttongrid").childNodes);

const count = 7;
console.log(allbutton);

allbutton.forEach((element) => {
  console.log(element.classList);
});


// ================ Switch ================

let currentRoom = document.querySelector(".drawing-room");



// ==================IDLE COUNT ===============

function idleReset() {
	var t;
	window.onload = resetTimer;
	window.onmousemove = resetTimer;
	window.onmousedown = resetTimer;  // catches touchscreen presses as well      
	window.ontouchstart = resetTimer; // catches touchscreen swipes as well 
	window.onclick = resetTimer;      // catches touchpad clicks as well
	window.onkeydown = resetTimer;   
	window.addEventListener('scroll', resetTimer, true); // improved; see comments

	function yourFunction() {
		showRooms();
	}

	function resetTimer() {
			clearTimeout(t);
			t = setTimeout(yourFunction, 30000);  // time is in milliseconds
	}
}
idleReset();