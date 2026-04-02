// Автоматическое обновление года в футере
const date = new Date();
const yearSpan = document.querySelector(".year");
if (yearSpan) {
    yearSpan.innerHTML = date.getFullYear();
}

// Автоматическое скрытие сообщений через 3 секунды
setTimeout(function() {
    const message = document.getElementById("message");
    if (message) {
        message.style.display = "none";
    }
}, 3000);
