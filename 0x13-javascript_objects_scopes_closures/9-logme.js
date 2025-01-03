#!/usr/bin/node
exports.logMe = function (item) {
  const args = [];
  if (item) {
    args.push(item);
  }

  for (let i = 0; i < args.length; i++) {
    console.log(`${i} : ${args[i]}`);
  }
};
