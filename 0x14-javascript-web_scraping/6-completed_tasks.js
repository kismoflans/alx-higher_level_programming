#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completed[todo.userId]) {
          completed[todo.userId] = 0;
        }
        completed[todo.userId] += 1;
      }
    });

    console.log(completed);
  } else {
    console.error('Error:', error);
  }
});
