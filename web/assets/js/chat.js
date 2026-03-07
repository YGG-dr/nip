async function sendMessage()
{
	let input = document.getElementById("message");
	let chat = document.getElementById("chat-window");

	let message = input.value;

	if(!message) return;

	chat.innerHTML += "<p>Você: </b>" + message + "</p>";
	
	let form = new FormData();
	form.append("message", message);
	
	let response = await fetch("chat.php", {
		method: "POST",
		body: form
	});
	
	let data = await response.json();
	
	chat.innerHTML += "<p><b>nip: " + data.response + "</p>";
	
	input.value = "";
}