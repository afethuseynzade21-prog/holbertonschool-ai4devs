function validateUser(user) {
    const errors = [];

    if (!user.name) {
        errors.push("Name is required");
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(user.email)) {
        errors.push("Invalid email format");
    }

    if (!user.password || user.password.length < 8) {
        errors.push("Password must be at least 8 characters");
    }

    return {
        isValid: errors.length === 0,
        errors: errors
    };
} console.log(validateUser({
    name: "Afet",
    email: "",
    password: "12345678"
}));

console.log(validateUser({
    name: "",
    email: "invalid-email",
    password: "123"
}));