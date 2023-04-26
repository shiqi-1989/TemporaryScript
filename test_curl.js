function getPublicIP(callback) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      callback(xhr.responseText);
    }
  }
  xhr.open('GET', 'https://api.ipify.org?format=json', true);
  xhr.send();
}

// 使用示例
getPublicIP(function(ip) {
  console.log(ip);
});