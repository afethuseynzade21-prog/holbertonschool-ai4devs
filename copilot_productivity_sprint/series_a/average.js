function calculateAverage(numbers) {
    if (numbers.length === 0) {
        return 0;
    }

    const sum = numbers.reduce((total, number) => total + number, 0);

    return sum / numbers.length;
}

module.exports = calculateAverage;