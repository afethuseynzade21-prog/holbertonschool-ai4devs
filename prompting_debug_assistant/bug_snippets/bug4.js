function getLastItems(items, n) {
    const result = [];

    const start = items.length - n;

    for (let i = start; i < items.length - 1; i++) {
        result.push(items[i]);
    }

    return result;
}

function main() {
    const values = ["a", "b", "c", "d", "e"];

    console.log(getLastItems(values, 3));
    console.log(getLastItems(values, 5));
}

main();
