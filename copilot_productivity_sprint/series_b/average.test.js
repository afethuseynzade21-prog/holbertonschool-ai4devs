const test = require("node:test");
const assert = require("node:assert");
const calculateAverage = require("./average");

test("calculates the average of positive numbers", () => {
    assert.strictEqual(calculateAverage([10, 20, 30]), 20);
});

test("calculates the average of positive and negative numbers", () => {
    assert.strictEqual(calculateAverage([5, -5]), 0);
});

test("returns 0 for an empty array", () => {
    assert.strictEqual(calculateAverage([]), 0);
});

test("calculates the average of a single number", () => {
    assert.strictEqual(calculateAverage([15]), 15);
});