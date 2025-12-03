function sqSum(num) {
    return num ** 2 + (num - 1 ? sqSum(num - 1) : 0);
}

console.log(sqSum(100));
