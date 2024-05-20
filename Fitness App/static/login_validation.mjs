// Email regex is from: https://stackoverflow.com/questions/46155/how-can-i-validate-an-email-address-in-javascript
const email_regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const special_chars = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;


function validate_input(email, password) {
    // Validate email
    let valid_email = email_regex.test(email);
    // Validate password
    let valid_password = (password.length > 10) && /[A-Z]/.test(password) && /[a-z]/.test(password) && special_chars.test(password);

    return [valid_email, valid_password];
}


function validate_registration() {
    var email_tag = document.getElementById("register-email");
    // console.log(email_tag.value);

    var password_tag = document.getElementById("register-password1");
    // console.log(password_tag.value);

    let password2_tag = document.getElementById("register-password2");
    // console.log(password2_tag.value);

    let incorrect_email_txt = document.getElementById("invalid_email");
    let incorrect_pass_txt = document.getElementById("password_hint");
    let incorrect_reentry = document.getElementById("password_match");

    let form_tags = [[email_tag, incorrect_email_txt], [password_tag, incorrect_pass_txt, password2_tag]];
    let valid_inputs = validate_input(email_tag.value, password_tag.value);
    let valid_registration = valid_inputs.every(element => element === true) && password2_tag.value == password_tag.value;

    // ((!valid_inputs[0] && !email_tag.classList.contains("invalid")) || (valid_inputs[0] && email_tag.classList.contains("invalid")))
    // The above is an expanded version of the below for email_tag.
    let toggle_tag = (validity, tag) => ((!validity && !tag.classList.contains("change")) || (validity && tag.classList.contains("change")));

    for (let i = 0; i < form_tags.length; i++) {
        // if the tag is invalid and doesn't have a invalid class attached to it- then toggle on the invalid class
        // OR
        // if the tag is valid and had an invalid class is attached to the tag- then toggle the invalid class off.
        if (toggle_tag(valid_inputs[i], form_tags[i][0])) {
            for (let j = 0; j < form_tags[i].length; j++) {
                form_tags[i][j].classList.toggle("change");
                console.log(form_tags[i][j].id, "was toggled!");
            }
        }
    }

    // Set up CSS for tags with the 'invalid' class- similar to how the red borders and additional text to show up

    if (password != password2) {
        // change border colour of re-enter password box
        document.getElementById("register-password2").style.border = "1px solid red";
    }

    if (valid_registration) {
        console.log("Valid registration");
        // POST to Python

        return true;
    }

    return false;
}

function validate_login() {
    // POST to Python

    // GET from Python
}