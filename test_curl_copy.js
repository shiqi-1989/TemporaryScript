// const request = require('request');
import request from 'request'
function getPublicIp(ppint) {
  const url = 'https://api.ipify.org?format=json';
  request(url, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      const data = JSON.parse(body);
      callback(data.ip);
    } else {
      callback(null);
    }
  });
}

function ppint(x){
  console.log(x);
}
getPublicIp(ppint)