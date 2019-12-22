### pycorsproxy

#### how to...
##### ... use it
```shell script
python3 srv.py
```

```javascript
let cp = "http://{addressOfThisProxy}/proxy/";
$.get(cp + "https://github.com/", function(data) {
  console.log(data);  // or do whatever
});
```
