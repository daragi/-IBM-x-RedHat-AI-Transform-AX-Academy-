from typing import Union
from fastapi import FastAPI, WebSocket, Request
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
    "http://127.0.0.1:3000"
    "http://localhost:3000"
    "http://192.168.0.231:3000"
    "http://192.168.0.231:8000"
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

@app.get("/")
async def get():
    return HTMLResponse(html)

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
     
    while True:
        data = await websocket.receive_text()
        print(data)
        # await websocket.send_text(f"Message text was: {data}")
        for client in clients:
            await client.send_text(f"Message text was: {data}")
                
@app.get("/items/{item_id}") # REST API http://localhost:8000/items/5
                             # Request data : ?q=somequery
def read_item(item_id: int, q: Union[str, None] = None) :
    return {"item_id": item_id, "q":q}

@app.post("/items/{item_id}") # REST API http://localhost:8000/items/2
def read_item(item_id: int, request: Request) :
    return {"item_id": item_id, "q(post)": request.values}

@app.put("/items/{item_id}") 
def update_item(item_id: int, item:Item) :
    print(item)
    return {"item_name": item.name, "item_id": item_id}
