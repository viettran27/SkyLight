import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.config import settings
from controller.router import router
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from config.websocket import manager
from positions import Hod, Req, Acct, Ca, Dir
from enums.Auth import POSITION
from repository.auth import AuthRepository
import jwt

def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(router, prefix=settings.API_PREFIX)

    return application


app = get_application()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str):
    await manager.connect(websocket)
    
    user = AuthRepository.getMe(token)
    position = user.skylight

    positions = {
        POSITION.REQ.value: Req.REQ,
        POSITION.HOD.value: Hod.HOD,
        POSITION.ACCT.value: Acct.ACCT,
        POSITION.CA.value: Ca.CA,
        POSITION.DIR.value: Dir.DIR
    }

    try:
        notifications = positions[position].get_notification()
        await websocket.send_json(notifications)
        
        while True:
            await websocket.receive_text() 
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)