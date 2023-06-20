// script.js

function sendMessage() {
    var input = document.getElementById('input-text');
    var message = input.value.trim();
  
    if (message !== '') {
      displayMessage(message, 'sent');
      input.value = '';
  
      // Lógica del chatbot
      // Puedes personalizar la lógica de respuesta del chatbot aquí
      var response = '¡Hola! Soy el chatbot ciberpunk. ¿En qué puedo ayudarte?';
      displayMessage(response, 'received');
    }
  }
  
  function displayMessage(message, type) {
    var chatMessages = document.getElementById('chat-messages');
    var messageElement = document.createElement('div');
    messageElement.classList.add('message', type);
    messageElement.innerHTML = '<p>' + message + '</p>';
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
    