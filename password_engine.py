# ==========================================================
# ADVANCED PASSWORD SECURITY SUITE
# PASSWORD ENGINE
# ==========================================================

import secrets
import string
import math
import re


# ==========================================================
# COMMON PASSWORD DATABASE
# ==========================================================

COMMON_PASSWORDS = {

    "123456",
    "123456789",
    "password",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "abc123",
    "welcome",
    "letmein",
    "football",
    "dragon",
    "monkey",
    "india123"

}


# ==========================================================
# PASSWORD GENERATOR
# ==========================================================

def generate_password(

        length,

        uppercase,

        lowercase,

        numbers,

        symbols

):

    characters = ""

    if uppercase:

        characters += string.ascii_uppercase

    if lowercase:

        characters += string.ascii_lowercase

    if numbers:

        characters += string.digits

    if symbols:

        characters += "!@#$%^&*()-_=+[]{}<>?/"

    if characters == "":

        characters = string.ascii_letters + string.digits

    password = ""

    for _ in range(length):

        password += secrets.choice(characters)

    return password


# ==========================================================
# ENTROPY CALCULATOR
# ==========================================================

def calculate_entropy(password):

    pool = 0

    if any(c.islower() for c in password):

        pool += 26

    if any(c.isupper() for c in password):

        pool += 26

    if any(c.isdigit() for c in password):

        pool += 10

    if any(not c.isalnum() for c in password):

        pool += 32

    if pool == 0:

        return 0

    entropy = len(password) * math.log2(pool)

    return round(entropy, 2)

# ==========================================================
# CRACK TIME ESTIMATION
# ==========================================================

def estimate_crack_time(entropy):

    if entropy < 28:
        return "Instantly"

    elif entropy < 36:
        return "Few Minutes"

    elif entropy < 60:
        return "Few Days"

    elif entropy < 80:
        return "Several Years"

    elif entropy < 100:
        return "Millions of Years"

    else:
        return "Practically Impossible"


# ==========================================================
# PASSWORD SCORE
# ==========================================================

def calculate_score(password):

    score = 0

    if len(password) >= 8:
        score += 15

    if len(password) >= 12:
        score += 15

    if any(c.isupper() for c in password):
        score += 15

    if any(c.islower() for c in password):
        score += 15

    if any(c.isdigit() for c in password):
        score += 15

    if any(not c.isalnum() for c in password):
        score += 15

    if password.lower() not in COMMON_PASSWORDS:
        score += 10

    if not re.search(r"(.)\1\1", password):
        score += 10

    return min(score, 100)


# ==========================================================
# PASSWORD LEVEL
# ==========================================================

def password_level(score):

    if score >= 90:
        return "Very Strong"

    elif score >= 70:
        return "Strong"

    elif score >= 50:
        return "Medium"

    elif score >= 30:
        return "Weak"

    return "Very Weak"

# ==========================================================
# PASSWORD ANALYZER
# ==========================================================

def analyze_password(password):

    entropy = calculate_entropy(password)

    score = calculate_score(password)

    level = password_level(score)

    crack_time = estimate_crack_time(entropy)

    feedback = []

    if len(password) < 12:
        feedback.append(
            "Use at least 12 characters."
        )

    if not any(c.isupper() for c in password):
        feedback.append(
            "Add uppercase letters."
        )

    if not any(c.islower() for c in password):
        feedback.append(
            "Add lowercase letters."
        )

    if not any(c.isdigit() for c in password):
        feedback.append(
            "Include numbers."
        )

    if not any(not c.isalnum() for c in password):
        feedback.append(
            "Include special symbols."
        )

    if password.lower() in COMMON_PASSWORDS:

        feedback.append(
            "This is a commonly used password."
        )

    if re.search(r"(.)\1\1", password):

        feedback.append(
            "Avoid repeated characters."
        )

    if "123" in password or "abc" in password.lower():

        feedback.append(
            "Avoid predictable sequences."
        )

    if len(feedback) == 0:

        feedback.append(
            "Excellent! Your password follows strong security practices."
        )

    return {

        "score": score,

        "level": level,

        "entropy": entropy,

        "crack_time": crack_time,

        "length": len(password),

        "feedback": feedback,

        "has_uppercase": any(c.isupper() for c in password),

        "has_lowercase": any(c.islower() for c in password),

        "has_numbers": any(c.isdigit() for c in password),

        "has_symbols": any(not c.isalnum() for c in password)

    }

