const API_URL = "https://your-backend-url.com";  // Zmień na właściwy adres backendu

async function fetchComments() {
    const username = document.getElementById("username").value || "elonmusk";
    const response = await fetch(`${API_URL}/comments?username=${username}`);
    const comments = await response.json();

    const list = document.getElementById("comments-list");
    list.innerHTML = "";

    comments.forEach(comment => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `${comment.text} <button onclick="blockUser('${comment.user_id}')">🚫 Blokuj</button>`;
        list.appendChild(listItem);
    });
}

async function blockUser(userId) {
    await fetch(`${API_URL}/block-user`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId })
    });
    alert("Użytkownik zablokowany!");
}
