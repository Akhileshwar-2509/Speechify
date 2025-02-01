// app/static/js/scripts.js

// Example function to show alert after file is uploaded
function showAlert(message) {
    alert(message);
}

// Example function to update content dynamically (like showing a success message after text-to-speech conversion)
function updateMessage(message) {
    const messageDiv = document.getElementById('message');
    messageDiv.innerText = message;
}
