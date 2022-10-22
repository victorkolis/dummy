import json
import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

file_path = os.path.abspath('app/db/db.json')


@app.get('/')
async def home():
    with open(file_path, 'r') as file:
        f = json.loads(file.read())
    return f


@app.get('/{name}')
async def home(name):
    with open(file_path, 'r') as file:
        f = json.loads(file.read())
        users = f[0].get('users')

    for user in users:
        if name in user:
            return user


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)
