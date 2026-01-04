const express = require("express");
const app = express();
app.get("/", function (req,res) {
    // (req,res) => {}
    return res.send("안녕하세요");
});

// 3000 << port를 의미
// 수정할때마다 node server.js를 입력해줘야 함
// node.js는 임베디드 방식
app.listen(3000, function() {
    console.log("server listening on port 3000");
});