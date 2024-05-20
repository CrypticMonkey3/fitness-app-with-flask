// Email regex is from: https://stackoverflow.com/questions/46155/how-can-i-validate-an-email-address-in-javascript
const email_regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const special_chars = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

function validate_input(email, password) {
    // Validate email
    let valid_email = (email) => { return email_regex.test(email); };
    let valid_password = (password) => { return (password.length > 10) && /[A-Z]/.test(password) && /[a-z]/.test(password) && special_chars.test(password); };
    console.log(valid_email ? "Valid email": "Invalid email");
    console.log(email);
    console.log(valid_password ? "Valid password": "Invalid password");
    console.log(password);

    return [valid_email, valid_password];
}

function validate_registration() {
    var email = document.getElementById("register-email").value;
    console.log(email);
    var password = document.getElementById("register-password1").value;
    console.log(password);
    let password2 = document.getElementById("register-password2").value;

    let valid_inputs = validate_input(email, password);
    let valid_registration = valid_inputs.every(element => element === true) && password2 == password;

    if (!valid_inputs[0]) {  // if email is invalid
        // change border colour of email box
        document.getElementById("register-email").style.border = "1px solid red";
    }

    if (!valid_inputs[1]) {  // if password is not at a secure enough level
        // change border colour of password boxes
        document.getElementById("register-password1").style.border = "1px solid red";
        document.getElementById("register-password2").style.border = "1px solid red";

        // make password requirements appear with the auto-generate button
        document.getElementByClassName("password_hint").style.display = "block";
    }

    if (password != password2) {
        // change border colour of re-enter password box
        document.getElementById("register-password2").style.border = "1px solid red";
    }

    if (valid_registration) {
        console.log("Valid registration");
        // POST to Python
    }
    return;
}

function validate_login() {
    // POST to Python

    // GET from Python
}