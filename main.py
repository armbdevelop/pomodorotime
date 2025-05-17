from fastapi import FastAPI
import uvicorn
from handlers import routers
app = FastAPI()

for router in routers:
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, env_file='.local.env')
