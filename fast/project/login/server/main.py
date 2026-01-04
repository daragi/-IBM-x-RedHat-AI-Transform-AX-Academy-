from typing import Union
from fastapi import FastAPI, WebSocket, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app =FastAPI()

html = """

<body>

<h1>WebSocket Chat</h1>

<form action="" onsubmit="sendMessage(event)">

<input type="text" id="messageText"
autocomplete="off"/>

<button>Send</button>

</form>

<ul id='messages'>

</ul>
<script>

var ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function(event) {
    // alert(event.data);
var messages = document.getElementById('messages')

var message = document.createElement('li')

var content = document.createTextNode(event.data)

message.appendChild(content)

messages.appendChild(message)
};

function sendMessage(event) {
var input = document.getElementById("messageText")

ws.send(input.value)

input.value = ''

event.preventDefault()
}

</script>

</body>

"""

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://192.168.0.231:3000",
    "http://192.168.0.231:8000",
    "http://www.himedia1.com:8000"
]

# WEB, WAS -> Front : WEB, Middle : WAS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 사용자 검증
def authenticate_user(id: str, password: str):
    if id == "id001" and password == "pwd001" :
        result = True
    else: result = False
    return result


@app.get("/hello")
def  hello(): return {"message": "FastApi: /hello"}

@app.post("/login")
def login(loginId: str = Form(...), pwd: str = Form(...)):
    print("loginId:", loginId, "pwd:", pwd)
    if loginId == "id001" and  pwd == "1234":
        return {"isLogin": True, "userName":loginId}
    else:
        return JSONResponse(status_code=401, 
                            content={"detail": "아이디 또는 비밀번호를 입력하세요"})
