function sendMessage() {
    let msgInput = document.getElementById("msg");
    let msg = msgInput.value;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += "<p><b>You:</b> " + msg + "</p>";

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += "<p><b>Bot:</b> " + data.response + "</p>";
    });

    msgInput.value = "";
}