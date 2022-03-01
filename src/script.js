
// ~~~database~~~
const db = `[
                {
                    "email": "test1@test.test",
                    "phone": "",
                    "password": "test1"
                },
                {
                    "email": "panda@pan.da",
                    "phone": "",
                    "password": "PANDA"
                },
                {
                    "email": "kali@kus.com",
                    "phone": "123456789",
                    "password": "kralcık"
                }
            ]`

// email/phone errors
validations = {
    email: [/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/],
    phone: [/^\d{5,50}$/]
};
emailVal = new RegExp(validations['email'][0]);
phoneVal = new RegExp(validations['phone'][0]);

function textInput() {
    text = document.getElementById('id-email-phone').value;
    text = text.replace(/\s/g,'');
    field = document.getElementById('text-input');
    err = document.getElementById('text-error');
    signin = document.getElementById('signin-button');
    
    if( !emailVal.test( text ) & !phoneVal.test( text ) ){
        if( text == "" )
            err.innerHTML = "Please enter a valid email or phone number.";
        else if( !isNaN( text ) & !phoneVal.test( text ) ) 
            err.innerHTML = "Please enter a valid phone number.";
        else if( text.length < 5 | text.length > 50 )
            err.innerHTML = "Your email must contain between 5 and 50 characters.";
        else if( !emailVal.test( text ) & isNaN( text ) )
            err.innerHTML = "Please enter a valid email.";
        else
            err.innerHTML = "Unknown Error.";
        
        signin.disabled = true;
        field.style.borderBottom = "2px solid #e87c03";
        return false;
    } else {
        signin.disabled = false;
        document.getElementById('text-error').innerHTML = '';
        field.style.borderBottom = "0px";
    }
}

function textCheckCorrection() {
    text = document.getElementById('id-email-phone').value;
    field = document.getElementById('text-input');
    signin = document.getElementById('signin-button');

    if( ( !emailVal.test( text ) & !phoneVal.test( text ) ) | text == "" | ( !isNaN( text ) & !phoneVal.test( text ) ) | ( text.length < 5 | text.length > 50 ) | ( !emailVal.test( text ) & isNaN( text ) ) ){
        return false;
    } else {
        signin.disabled = false;
        document.getElementById('text-error').innerHTML = '';
        field.style.borderBottom = "0px";
    }
}

// password errors
function passInput() {
    pass = document.getElementById('id-password').value;
    pass = pass.replace(/\s/g,'');
    field = document.getElementById('pass-input');
    signin = document.getElementById('signin-button');

    if( pass.length < 4 | pass.length > 60 ) {
        document.getElementById('pass-error').innerHTML = "Your password must contain between 4 and 60 characters.";
        field.style.borderBottom = "2px solid #e87c03";
        signin.disabled = true;
        return false;
    }
    else {
        signin.disabled = false;
        document.getElementById('pass-error').innerHTML = "";
        field.style.borderBottom = "0px";
    }
}

function passCheckCorrection() {
    pass = document.getElementById('id-password').value;
    pass = pass.replace(/\s/g,'');
    field = document.getElementById('pass-input');
    signin = document.getElementById('signin-button');

    if( pass.length < 4 | pass.length > 60 ) {
        return false;
    }
    else {
        signin.disabled = false;
        document.getElementById('pass-error').innerHTML = "";
        field.style.borderBottom = "0px";
    }
}

// show/hide focus helper 
document.getElementsByTagName("button")[0].addEventListener("mousedown",function(e){
        e.preventDefault();
    });

// form resend popup remover
if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}

// remember me functionality
checkCheck = document.getElementById("id-remember-me");
userInput = document.getElementById("id-email-phone");

if( localStorage.checkbox && localStorage.checkbox !== "" ) {
    checkCheck.setAttribute("checked", "checked");
    userInput.value = localStorage.username;
} else {
    checkCheck.removeAttribute("checked");
    userInput.value = "";
}

function rememberMe() {
    if( checkCheck.checked && userInput.value !== "" ) {
        localStorage.username = userInput.value;
        localStorage.checkbox = checkCheck.value;
    } else {
        localStorage.username = "";
        localStorage.checkbox = "";
    }
}

// sign in checks
function checks() {
    rememberMe();
    textInput();
    passInput();

    error = document.getElementById("db-error");
    errorMsg = document.getElementById("db-error-text");

    text = document.getElementById('id-email-phone').value;
    fieldText = document.getElementById('text-error');
    pass = document.getElementById('id-password').value;
    pass = pass.replace(/\s/g,'');
    fieldPass = document.getElementById('pass-error');

    if( fieldText.innerHTML == "" & fieldPass.innerHTML == "" ) {
        data = JSON.parse(db);

        emailFlag = false;
        phoneFlag = false;

        for( let i = 0; i < data.length; i++ ) {
            if( text == data[i].email | text == data[i].phone ) {
                if( text == data[i].email )
                    emailFlag = true;
                else
                    phoneFlag = true;
                    
                if( pass == data[i].password ) {
                    errorMsg.innerHTML = "";
                    error.style.height = "0";
                    errorMsg.style.padding = "0";
                    return true;
                }
                else {
                    errorMsg.innerHTML = "<b>Incorrect password.</b> Please try again or you can reset your password.";
                    error.style.height = "48px";
                    errorMsg.style.padding = "10px 20px";
                    return false;
                }
            }
        }

        if( !emailFlag & !phoneFlag ) {
            if( isNaN( text ) ) {
                errorMsg.innerHTML = "Sorry, we can't find an account with this email address. Please try again or create a new account.";
                error.style.height = "48px";
                errorMsg.style.padding = "10px 20px";
            }
            else {
                errorMsg.innerHTML = "Sorry, we can't find an account with this number. Please make sure to select the correct country code or <b>sign in with email.</b>";
                error.style.height = "48px";
                errorMsg.style.padding = "10px 20px";
            }
        }
    }
    return false;
}

// show/hide password
function showPassword() {
    pass = document.getElementById("id-password");
    text = document.getElementById("id-show-hide");
    style = window.getComputedStyle(text),
    color = style.getPropertyValue('color');

    if( color == "rgb(140, 140, 140)" ) 
    {
        if( text.textContent == 'HIDE' )
            text.textContent = 'SHOW';
        else
            text.textContent = 'HIDE';

        if( pass.type == "password" )
            pass.type = "text";
        else 
            pass.type = "password";
    }
    else
        pass.focus();
}

// click on learn more
function expandRecaptcha() {
    more = document.getElementById("make-vis");
    text = document.getElementById("disappear");

    more.style.visibility = 'visible';
    text.style.visibility = 'hidden';
}
