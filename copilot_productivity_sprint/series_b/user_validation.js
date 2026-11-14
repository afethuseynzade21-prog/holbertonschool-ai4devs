function validateUser(user) {
    const errors = [];

    if (!user || typeof user !== "object") {
        return {
            isValid: false,
            errors: ["Invalid user data"]
        };
    }

    if (typeof user.name !== "string" || !user.name.trim()) {
        errors.push("Name is required");
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (
        typeof user.email !== "string" ||
        !emailPattern.test(user.email)
    ) {
        errors.push("Invalid email format");
    }

    if (
        typeof user.password !== "string" ||
        user.password.length < 8
    ) {
        errors.push("Password must be at least 8 characters");
    }

    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Test 1: Valid user
console.log(validateUser({
    name: "Afet",
    email: "afet@example.com",
    password: "12345678"
}));

// Test 2: Invalid user
console.log(validateUser({
    name: "",
    email: "invalid-email",
    password: "123"
}));

// Test 3: Empty email
console.log(validateUser({
    name: "Afet",
    email: "",
    password: "12345678"
}));

// Test 4: Null input
console.log(validateUser(null));