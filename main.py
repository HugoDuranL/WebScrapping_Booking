from fastapi import FastAPI, Query
import controller.booking_controller as booking_controller

app = FastAPI()

app.include_router(booking_controller.router)