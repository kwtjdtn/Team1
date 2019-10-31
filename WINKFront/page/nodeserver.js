// JavaScript source code

var express = require('express');
var app = express();
var fs = require('fs');

app.listen(8080, function (){
    console.log('Server Start');
});

app.get('/', function (req, res) {
    fs.readFile('wink.html', function (error, data) {
        if (error) {
            console.log(error);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(data);
        }
    });
});
app.get('/afterlogin', function (req, res) {
    fs.readFile('wink_afterlogin.html', function (error, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});
