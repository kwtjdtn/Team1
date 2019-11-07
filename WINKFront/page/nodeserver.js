// JavaScript source code
var http = require('http');
var express = require('express');
var app = express();
var fs = require('fs');
const bodyParser = require('body-parser')
const session = require('express-session');
const axios = require('axios');
const FileStore = require('session-file-store')(session);



//if (request.headers.cookie) {
//    var cookie = request.headers.cookie.split(';').map(function (element) {
//        var element = element.split('=');
//        return {
//            key: element[0],
//            value: element[1]
//        };
//    });
//    document.cookie = element;
//}

const apiHost = "http://localhost:8000/";


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(session({
    secret: '2$!h2kf66k+f61-#r(ts_v_0ex(h#7+1e@afhxl^ee1#sw@tt2',
    resave: false,
    saveUninitialized: false,
    cookie: {
        maxAge: 3600000,
        secure: false,
        httpOnly: false,
    },
}))

app.listen(3000, function (){
    console.log('Server Start');
});

//router.route('/').get(function (req, res) {
//    console.log('/');
//    req.cookies.[Set - Cookie]
//    res.send()
app.use(express.static('assets'));




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
// login/api/ktislogin/
app.post('/login', function (req, res) {
    axios.post(apiHost + 'login/api/login/', req.body)
        .then(response => {
            let auth_token = response.data.TOKEN;
            var tkn = auth_token;

            //console.log(req.session)
            req.session.auth = auth_token;
            //return response
            return req.session.save(function () {
                res.end()
            })
        })
})
app.get('/afterlogin', function (req, res) {
    fs.readFile('wink_afterlogin.html', function (error, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});
app.get('/createschedule', function (req, res) {
    console.log(req.session.auth);
   
    axios.get(apiHost + 'login/api/createschedule/', { headers: { Token: req.session.auth } })
        .then(res => {
            console.log(res.data);
            res.end()
        })
        .catch(error => {
            res.end()
        });
})
app.get('/main', function (req, res) {
    fs.readFile('wink_main.html', function (error, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

app.get('/timetable', function (req, res) {
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
