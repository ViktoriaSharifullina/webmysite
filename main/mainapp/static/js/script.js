const email = document.getElementById("mail");
const password = document.getElementById("password");

email.addEventListener("input", function (event) {
    if (email.validity.typeMismatch) {
      email.setCustomValidity("Введите e-mail адрес в формате name@gmail.ru");
      email.style.backgroundColor = "rgba(168, 53, 53, 0.295)";
    } else {
      email.style.backgroundColor = "#e6e6e6";
      email.setCustomValidity("");
    }
  });

  password.addEventListener("input", function (event) {
    if (password.validity.patternMismatch) {
        password.setCustomValidity("Пароль должен содержать не менее восьми символов, минимум одно число, буквы нижнего и верхнего регистра и специальные символы.");
        password.style.backgroundColor = "rgba(168, 53, 53, 0.295)";
      } else {
        password.style.backgroundColor = "#e6e6e6";
        password.setCustomValidity("");
    }
  });