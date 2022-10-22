import json

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    with open('../../db.json', 'r') as file:
        f = json.loads(file.read())
    return f


@app.get('/pirata')
async def home():
    with open('../../db.json', 'r') as file:
        f = json.loads(file.read())
        users = f[0].get('users')

    return users[0].get('1')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)
