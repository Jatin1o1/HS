const showRooms = () => {
	document.querySelector(".rooms").style.display = "block";
	hideAllButtons();
	currentDispHide();	
}

const hideRooms = () => {
	document.querySelector(".rooms").style.display = "none";
}

const currentDispHide = () => {
	document.querySelector(".current-disp").style.display = "none";
}

const currentDispShow = (room) => {
	document.querySelector(".current-disp").innerHTML = room;
	document.querySelector(".current-disp").style.display = "block";
}

const hideAllButtons = () => {
	document.querySelector(".master-bedroom").style.display = "none";
	document.querySelector(".drawing-room").style.display = "none";
	document.querySelector(".jatins-room").style.display = "none";
	document.querySelector(".meghas-room").style.display = "none";
}


const showMB = () => {
	currentRoom = document.querySelector(".master-bedroom");
	hideRooms();
	hideAllButtons();
	currentDispShow("Master Bedroom");
	document.querySelector(".master-bedroom").style.display = "grid";
	
}

const showDR = () => {
	currentRoom = document.querySelector(".drawing-room");
	hideRooms();
	hideAllButtons();
	currentDispShow("Drawing Room");
	document.querySelector(".drawing-room").style.display = "grid";
	
}

const showJR = () => {
	currentRoom = document.querySelector(".jatins-room");
	hideRooms();
	hideAllButtons();
	currentDispShow("Jatin's Room");
	document.querySelector(".jatins-room").style.display = "grid";
	
}

const showMR = () => {
	currentRoom = document.querySelector(".meghas-room");
	hideRooms();
	hideAllButtons();
	currentDispShow("Megha's Room");
	document.querySelector(".meghas-room").style.display = "grid";
	
}

const showlights = () => {
	currentRoom.display = "grid";
	Array.from(currentRoom.childNodes).forEach(button => {
		if(button.classList != undefined) {
			if(button.classList.contains("switchLight")) {
				button.style.display = "block";
			} else  {
				button.style.display = "none";
			}
		}
	})
};

const showall = () => {
	Array.from(currentRoom.childNodes).forEach(button => {
    if(button.classList != undefined) {
      if(button.classList.contains("button")) {
        button.style.display = "block";
      }
    }
  });
};

const showlock = () => {
	hideAllButtons();
	document.querySelector(".current-disp").style.display = "none";
};

const showsensor = () => {
  allbutton.forEach (button => {
    if(button.classList != undefined) {
      if(button.classList.contains("sensor")) {
        button.style.display = "block";
      } else {
        button.style.display = "none";
      }
    }
  });
};

