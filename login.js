import { auth } from "./firebase.js";
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Toggle Signup form
function showSignup() {
  document.querySelector('.login-container').style.display = 'none';
  document.querySelector('.signup-container').style.display = 'block';
}

// Toggle Login form
function showLogin() {
  document.querySelector('.signup-container').style.display = 'none';
  document.querySelector('.login-container').style.display = 'block';
}

window.showSignup = showSignup;
window.showLogin = showLogin;

// LOGIN
document.getElementById('loginForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const email = document.getElementById('username').value;   // using email as username
  const password = document.getElementById('password').value;

  signInWithEmailAndPassword(auth, email, password)
    .then(() => {
      Swal.fire({
        icon: 'success',
        title: 'Login Successful',
        text: 'Welcome back!'
      }).then(() => {
        window.location.href = "dashboard.html";
      });
    })
    .catch(error => {
      Swal.fire("Error", error.message, "error");
    });
});

// SIGNUP
document.getElementById('signupForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const email = document.getElementById('email').value;
  const password = document.getElementById('newPassword').value;

  createUserWithEmailAndPassword(auth, email, password)
    .then(() => {
      Swal.fire({
        icon: 'success',
        title: 'Registration Successful',
        text: 'You can now login'
      });
      showLogin();
    })
    .catch(error => {
      Swal.fire("Error", error.message, "error");
    });
});
