### pycorsproxy

server running at: [corspro.xyz](http://corspro.xyz)
#### how to...
##### ... use it
```shell script
python3 srv.py
```

```javascript
let cp = "http://corspro.xyz/proxy/";
$.get(cp + "https://github.com/", function(data) {
  console.log(data);  // or do whatever
});
```
