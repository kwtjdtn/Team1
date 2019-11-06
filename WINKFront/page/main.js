
function a() {
    console.log('1');
    var http = require('http');

// HTTPRequest의 옵션 설정
    var jsonDataObj = {'id': '20153159', 'pw': 'rhrnak2628!'};
//20153159
//rhrnak2628
    var options = {
        host: 'localhost',
        port: '8000',
        path: '/login/api/login/',
        method: 'POST',
        Body: jsonDataObj,
    };
console.log('2');
// 콜백 함수로 Response를 받아온다
    var callback = function (response) {
        // response 이벤트가 감지되면 데이터를 body에 받아온다
        var body = '';
        response.on('data', function (data) {
            body += data;
        });

        // end 이벤트가 감지되면 데이터 수신을 종료하고 내용을 출력한다
        response.on('end', function () {
            // 데이저 수신 완료
            console.log(body);
            console.log(response.headers['set-cookie'])
        });
    }
// 서버에 HTTP Request 를 날린다.
    var req = http.request(options, callback);
    req.end();
}
function b() {
            var input_id = document.getElementById("input-id").value;
            var input_pw = document.getElementById("input-pw").value;
            var data = { id: input_id, pw: input_pw };
            $.ajax({
                url: 'http://localhost:8000/login/api/login/',
                type: 'POST',
                contentType: 'application/x-www-form-urlencoded',
                dataType: 'json',
                data: data,
                async: false,
                error: function (error) {
                    alert(error);
                },
                success: function (msg,status,xmr) {
                    if (JSON.stringify(msg) == "{\"login\":\"fail\"}") {
                        alert("로그인 실패");
                    }
                    else {
                        alert(xmr.getAllResponseHeaders())
                        var parsedData = msg;
                        var TOKEN = parsedData['TOKEN'];
                        var jsTOKEN = JSON.stringify(TOKEN);
                        var completeTOKEN = jsTOKEN.replace(/\"/gi, "");
                        sessionStorage.setItem("session", completeTOKEN);
                        location.href = "wink_afterlogin.html";
                    }
                }
            });
        }