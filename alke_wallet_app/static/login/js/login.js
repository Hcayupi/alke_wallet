
/**
 * Mostrar / ocultar contraseña
 */
function togglePassword(button) {
  const pass = document.getElementById("idPass");
  const icon = button.querySelector("i");

  if (pass.type === "password") {
    pass.type = "text";
    icon.classList.replace("bi-eye", "bi-eye-slash");
  } else {
    pass.type = "password";
    icon.classList.replace("bi-eye-slash", "bi-eye");
  }
}

function limpiarInputsLogin() {
  setTimeout(() => {
    txtEmail.value = "";
    txtPass.value = "";
    feedback.classList.add("invisible");
    txtEmail.classList.remove("is-invalid");
    txtPass.classList.remove("is-invalid");
  }, 2000);
}
