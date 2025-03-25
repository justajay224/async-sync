from fastapi import FastAPI
from route.index import include_routers
from middleware.time_middleware import TimingMiddleware

app = FastAPI()

app.add_middleware(TimingMiddleware)

include_routers(app)

