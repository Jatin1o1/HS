openSocket = () => {

    socket = new WebSocket("ws://127.0.0.1:9997/");
    let msg = document.getElementById("msg");
    socket.addEventListener('open', (e) => {
        document.getElementById("status").innerHTML = "Opened";
        console.log("opened");
    });
    socket.addEventListener('message', (e) => {
        console.log("got message");
        let ctx = msg.getContext("2d");
        let image = new Image();
        image.src = URL.createObjectURL(e.data);
        image.addEventListener("load", (e) => {
            ctx.drawImage(image, 0, 0, msg.width, msg.height);
        });
    });
}
