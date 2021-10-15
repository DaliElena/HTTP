const http = require('http');

const optionsGet = {
    'method': 'GET',
    'hostname': 'localhost',
    'port': 8000,
    'path': '/integration',
    'headers': {},
};
const optionsPost = {
    'method': 'POST',
    'hostname': 'localhost',
    'port': 8000,
    'path': '/',
    'headers': {
        'Content-Type': 'text/plain'
    },
};


function  GetMessage()
{
    const req = http.request(optionsGet, function (res) {
        const chunks = [];

        res.on("data", function (chunk) {
            chunks.push(chunk);
        });

        res.on("end", function (chunk) {
            const body = Buffer.concat(chunks);
            document.getElementById('textMessages').value=body.toString();
            console.log(body.toString());
        });

        res.on("error", function (error) {
            console.error(error);
        });
    });

    req.end();
}

function SendMessage(message)
{
    const req = http.request(optionsPost, function (res) {
        const chunks = [];

        res.on("data", function (chunk) {
            chunks.push(chunk);
        });

        res.on("end", function (chunk) {
            const body = Buffer.concat(chunks);
            console.log(body.toString());
        });

        res.on("error", function (error) {
            console.error(error);
        });
    });
    req.write(message);
    req.end();
}
document.getElementById('getMessages').onclick = function () {
    GetMessage();
}
document.getElementById('postMessage').onclick = function () {
   SendMessage(document.getElementById('textMessage').value);
}
