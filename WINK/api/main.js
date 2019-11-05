
            var request = require('request');

// Set the headers
            var headers = {
                'User-Agent': 'Super Agent/0.0.1',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

// Configure the request
            var options = {
                url: 'http://localhost:8000/login/api/login',
                method: 'POST',
                headers: headers,
                qs: {'id': '20153159', 'pw': 'rhrnak2628!'}
            }

// Start the request
            request(options, function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    // Print out the response body
                    alert(body)
                }
            })
