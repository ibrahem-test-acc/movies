// ___login form___
let userName = document.getElementById("name");
let email = document.getElementById("email");
let password = document.getElementById("password");
let btnLogin = document.getElementById("btnLogin");
let users = [];

btnLogin.addEventListener("click", function () {
  if (
    validationName() == true &&
    validationEmail() == true &&
    validationPassword() == true
  ) {
    let userData = {
      userName: userName.value,
      email: email.value,
      password: password.value,
    };
    users.push(({ userName, email, password } = userData));
    localStorage.setItem("data", JSON.stringify(users));
    window.open("home.html", "_self");
    document.getElementById("error").innerHTML = ``;
  }
});

function validationName() {
  let regx = /^\w{3,8}$/;
  if (regx.test(userName.value) == true) {
    return true;
  } else {
    document.getElementById(
      "error"
    ).innerHTML = `<div class="alert alert-danger">Name Invalid...!</div>`;
  }
}
function validationEmail() {
  let regx = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  if (regx.test(email.value) == true) {
    return true;
  } else {
    document.getElementById(
      "error"
    ).innerHTML = `<div class="alert alert-danger">Email Invalid...!</div>`;
  }
}
function validationPassword() {
  let regx = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  if (regx.test(password.value) == true) {
    return true;
  } else {
    document.getElementById(
      "error"
    ).innerHTML = `<div class="alert alert-danger">Password Invalid...!</div>`;
  }
}

// ------------------------
// Alert

let alert = document.getElementById("alert");

alert.addEventListener("click", function () {
  swal({
    title: "مــــعــــلــــــش هه",
    timer: 4000,
  });
});
