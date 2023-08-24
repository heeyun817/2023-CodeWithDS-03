/*function login() {
    // 로그인 처리 로직을 여기에 작성할 수 있습니다.
    // 예시: 로그인 로직이 성공했다고 가정하고 main.html로 이동합니다.
    window.location.href = "main.html";
}

function goToMain() {
    // 바로 main.html로 이동합니다.
    window.location.href = "main.html";
}*/

function updateButtonStatus() {
    const idInput = document.getElementById("idInput");
    const passwordInput = document.getElementById("passwordInput");
    const loginButton = document.getElementById("loginButton");

    if (idInput.value && passwordInput.value) {
        loginButton.disabled = false;
    } else {
        loginButton.disabled = true;
    }
}

// 아이디와 비밀번호 입력 시 확인 버튼 상태 업데이트
document.addEventListener("input", updateButtonStatus);

// 로그인 처리 및 main.html로 이동
function welcome() {
    // 로그인 처리 로직을 여기에 작성할 수 있습니다.
    // 예시: 로그인 로직이 성공했다고 가정하고 알림을 띄우고 main.html로 이동합니다.
    alert("덕씨님 어서오세요!");
    window.location.href = "home.html";
}