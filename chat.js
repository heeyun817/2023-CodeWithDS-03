function sendMessage() {
    var messageInput = document.getElementById("messageInput");
    var messageText = messageInput.value;
    
    if (messageText.trim() === "") {
        return; // 빈 메시지는 전송하지 않음
    }
    
    var chatContent = document.querySelector(".chat-content");
    
    var messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    
    var profileDiv = document.createElement("div");
    profileDiv.classList.add("profile");
    var profileImg = document.createElement("img");
    profileImg.src = "img/dukxi_logo.png"; // 프로필 이미지 주소
    profileDiv.appendChild(profileImg);
    
    var textDiv = document.createElement("div");
    textDiv.classList.add("text");
    var textParagraph = document.createElement("p");
    textParagraph.innerHTML = "<strong>나:</strong> " + messageText;
    textDiv.appendChild(textParagraph);
    
    messageDiv.appendChild(profileDiv);
    messageDiv.appendChild(textDiv);
    
    chatContent.appendChild(messageDiv);
    
    messageInput.value = ""; // 메시지 입력란 초기화
    
    // 채팅 내용이 너무 많아지지 않도록 스크롤을 아래로 이동
    chatContent.scrollTop = chatContent.scrollHeight;
}