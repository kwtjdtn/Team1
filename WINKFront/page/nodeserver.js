// JavaScript source code
var http = require('http');
var express = require('express');
var app = express();
var fs = require('fs');
var session = require('express-session');

app.listen(3000, function (){
    console.log('Server Start');
});

app.use(express.static('assets'));
app.use(express.session({
    secret: 'mySecret',
    cookie: { httpOnly: false }
}));

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

app.get('/main', function (req, res) {
    fs.readFile('wink_main.html', function (error, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

app.get('/timetalbe', function (req, res) {
    fs.readFile('wink_timetable.html', function (error, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

app.get('/signup', function (req, res) {
    fs.readFile('wink_singup.html', function (error, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});
