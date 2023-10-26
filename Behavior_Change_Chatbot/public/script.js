document.addEventListener('DOMContentLoaded', function () {
    const chatLog = document.getElementById('chat-log');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage !== '') {
            appendUserMessage(userMessage);
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_input: userMessage }),
            })
                .then((response) => response.json())
                .then((data) => {
                    appendBotMessage(data.response);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            userInput.value = '';
        }
    });

    function appendUserMessage(message) {
        const userMessage = document.createElement('div');
        userMessage.classList.add('chat-msg');
        userMessage.textContent = message;
        chatLog.appendChild(userMessage);
    }

    function appendBotMessage(message) {
        const botMessage = document.createElement('div');
        botMessage.classList.add('chat-msg', 'bot');
        botMessage.textContent = message;
        chatLog.appendChild(botMessage);
    }
});
