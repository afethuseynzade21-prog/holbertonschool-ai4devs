
const express = require("express");

const app = express();

app.use(express.json());

let users = [];
let nextId = 1;

app.post("/users", (req, res) => {
    const { name, email } = req.body || {};

    if (typeof name !== "string" || !name.trim()) {
        return res.status(400).json({
            error: "Name is required"
        });
    }

    if (typeof email !== "string" || !email.trim()) {
        return res.status(400).json({
            error: "Email is required"
        });
    }

    const user = {
        id: nextId++,
        name: name.trim(),
        email: email.trim()
    };

    users.push(user);

    return res.status(201).json(user);
});

module.exports = app;
