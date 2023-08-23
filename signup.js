// 가입부분 체크

/*function signUpCheck(){

    let email = document.getElementById("email").value
    let name = document.getElementById("name").value
    let password = document.getElementById("password").value
    let passwordCheck = document.getElementById("passwordCheck").value
    let check = true;
    
      // 이메일확인
      if(email.includes('@')){
        let emailId = email.split('@')[0]
        let emailServer = email.split('@')[1]
        if(emailId === "" || emailServer === ""){
          document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
          check = false
        }
        else{
          document.getElementById("emailError").innerHTML=""
        }
      }else{
        document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
        check = false
      }
    
    
      // 이름확인
      if(name===""){
        document.getElementById("nameError").innerHTML="이름이 올바르지 않습니다."
        check = false
      }else{
        document.getElementById("nameError").innerHTML=""
      }
    
    
      // 비밀번호 확인
      if(password !== passwordCheck){
        document.getElementById("passwordError").innerHTML=""
        document.getElementById("passwordCheckError").innerHTML="비밀번호가 동일하지 않습니다."
        check = false
      }else{
        document.getElementById("passwordError").innerHTML=""
        document.getElementById("passwordCheckError").innerHTML=""
      }
    
      if(password===""){
        document.getElementById("passwordError").innerHTML="비밀번호를 입력해주세요."
        check = false
      }else{
        //document.getElementById("passwordError").innerHTML=""
      }
      if(passwordCheck===""){
        document.getElementById("passwordCheckError").innerHTML="비밀번호를 다시 입력해주세요."
        check = false
      }else{
        //document.getElementById("passwordCheckError").innerHTML=""
      }
    
      if(check){
        document.getElementById("emailError").innerHTML=""
        document.getElementById("nameError").innerHTML=""
        document.getElementById("passwordError").innerHTML=""
        document.getElementById("passwordCheckError").innerHTML=""
        
        //비동기 처리이벤트
        setTimeout(function() {
          alert("가입이 완료되었습니다.")
      },0);
      }
    }*/

// signup.js

// 이메일 인증 버튼 클릭 시 이벤트
function sendVerificationCode() {
    alert("인증코드를 보냈습니다. 메일을 확인해주세요!");
    window.location.href = "email.html"; // email.html로 이동
}

function verifyEmailCode() {
    alert("이메일이 인증되었습니다.");
    window.location.href = "signup.html"; // signup.html로 이동
}

// 회원가입 버튼 클릭 시 이벤트
function completeSignUp() {
    alert("가입되셨습니다!");
    window.location.href = "login.html"; // login.html로 이동
}

// 회원가입 버튼 활성화 여부 업데이트
function updateSignUpButtonStatus() {
    const nameInput = document.getElementById("nameInput");
    const emailInput = document.getElementById("emailInput");
    const passwordInput = document.getElementById("passwordInput");
    const confirmPasswordInput = document.getElementById("confirmPasswordInput");
    const signUpButton = document.getElementById("signUpButton");

    if (nameInput.value && emailInput.value && passwordInput.value && confirmPasswordInput.value) {
        signUpButton.disabled = false;
    } else {
        signUpButton.disabled = true;
    }
}

document.addEventListener("input", updateSignUpButtonStatus);

function completeSignUp() {
    alert("가입되셨습니다!");
    window.location.href = "login.html"; // login.html로 이동
}


window.addEventListener("load", function() {
    updateSignUpButtonStatus(); // 페이지 로딩 시 초기 상태 반영
});
