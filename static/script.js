// ==========================================
// COPY PASSWORD
// ==========================================

function copyPassword() {

    const password =
        document.getElementById("password");

    if (!password) return;

    navigator.clipboard.writeText(password.value);

    const toast =
        document.getElementById("toast");

    toast.classList.add("show");

    setTimeout(function(){

        toast.classList.remove("show");

    },2000);

}


// ==========================================
// SHOW / HIDE PASSWORD
// ==========================================

function togglePassword() {

    const input =
        document.getElementById("analyzePassword");

    if (!input) return;

    if (input.type === "password") {

        input.type = "text";

    }

    else {

        input.type = "password";

    }

}

// ==========================================
// LIVE PASSWORD STRENGTH METER
// ==========================================

function updateStrengthMeter() {

    const input =
        document.getElementById("analyzePassword");

    const bar =
        document.getElementById("strengthFill");

    const text =
        document.getElementById("strengthText");

    if (!input || !bar || !text) return;

    const password = input.value;

    let score = 0;

    if (password.length >= 8) score++;

    if (/[A-Z]/.test(password)) score++;

    if (/[a-z]/.test(password)) score++;

    if (/[0-9]/.test(password)) score++;

    if (/[^A-Za-z0-9]/.test(password)) score++;

    if (score <= 2) {

        bar.style.width = "30%";
        bar.className = "strength-fill weak";
        text.innerHTML = "Weak Password";

    }

    else if (score <= 4) {

        bar.style.width = "70%";
        bar.className = "strength-fill medium";
        text.innerHTML = "Medium Password";

    }

    else {

        bar.style.width = "100%";
        bar.className = "strength-fill strong";
        text.innerHTML = "Strong Password";

    }

}


// ==========================================
// PAGE LOADED
// ==========================================

window.onload = function () {

    console.log(
        "Advanced Password Security Suite Loaded"
    );

};

// ==========================================
// LIVE PASSWORD LENGTH
// ==========================================

function updateLengthValue() {

    const slider =
        document.getElementById("lengthSlider");

    const value =
        document.getElementById("lengthValue");

    if (!slider || !value) return;

    value.innerHTML = slider.value;

}


// Initialize when page loads
window.addEventListener("load", function () {

    updateLengthValue();

});