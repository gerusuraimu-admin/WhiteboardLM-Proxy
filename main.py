from utils import get_server, request
from utils import (
    AuthPayload,
    LoginPayload,
    LogoutPayload,
    RegisterPayload
)

server = get_server()


@server.post('/auth')
async def auth(payload: AuthPayload):
    return request(payload, 'auth')


@server.post('/login')
async def login(payload: LoginPayload):
    return request(payload, 'login')


@server.post('/logout')
async def logout(payload: LogoutPayload):
    return request(payload, 'logout')


@server.post('/register')
async def register(payload: RegisterPayload):
    return request(payload, 'register')


@server.post('/embed')
async def embed(payload: AuthPayload):
    return request(payload, 'embed')
