
const { test, before, after } = require("node:test");
const assert = require("node:assert");
const app = require("./index");

let server;
let base;

before(async () => {
    await new Promise((resolve) => {
        server = app.listen(0, resolve);
    });
    base = `http://localhost:${server.address().port}`;
});

after(() => server.close());

const post = (body) =>
    fetch(`${base}/users`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });

test("valid data returns 201", async () => {
    const res = await post({
        name: "Afet",
        email: "afet@example.com"
    });

    assert.strictEqual(res.status, 201);

    const body = await res.json();
    assert.strictEqual(body.name, "Afet");
    assert.strictEqual(body.email, "afet@example.com");
    assert.ok(body.id);
});

test("missing name returns 400", async () => {
    const res = await post({
        email: "afet@example.com"
    });

    assert.strictEqual(res.status, 400);
});

test("missing email returns 400", async () => {
    const res = await post({
        name: "Afet"
    });

    assert.strictEqual(res.status, 400);
});

test("empty fields return 400", async () => {
    const res = await post({
        name: "   ",
        email: ""
    });

    assert.strictEqual(res.status, 400);
});
