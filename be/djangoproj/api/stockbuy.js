const assert = require("assert");

/*
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

Return the result in the following format `{ buyIndex: 2, sellIndex: 3 }`

For example, given [9, 11, 8, 5, 7, 10], you should return  `{ buyIndex: 3, sellIndex: 5 }`, since you could buy the stock at 5 dollars and sell it at 10 dollars. Return undefined if there are no positive trades.
*/

// YOUR CODE HERE ==============================
const mostProfit = (inputs) => {};
// ================================================

const tests = [
  {
    question: [9, 11, 8, 5, 7, 10],
    answer: { buyIndex: 3, sellIndex: 5 },
  },
  { question: [43, 43, 43, 43, 43], answer: undefined },
  {
    question: [12, 17, 23, 29, 34],
    answer: { buyIndex: 0, sellIndex: 4 },
  },
  { question: [48, 42, 37, 31, 25], answer: undefined },
  {
    question: [21, 29, 18, 32, 24],
    answer: { buyIndex: 2, sellIndex: 3 },
  },
  {
    question: [15, 45, 74, 46, 16],
    answer: { buyIndex: 0, sellIndex: 2 },
  },
  {
    question: [73, 44, 15, 43, 72],
    answer: { buyIndex: 2, sellIndex: 4 },
  },
  {
    question: [8, 67, 35, 98, 59],
    answer: { buyIndex: 0, sellIndex: 3 },
  },
  {
    question: [52, 53, 51, 54, 52],
    answer: { buyIndex: 2, sellIndex: 3 },
  },
].map(({ question, answer }) => assert.deepEqual(mostProfit(question), answer));
if (tests.every((x) => x == undefined)) {
  console.log("Correct 🎉");
}
