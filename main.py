from fastapi import FastAPI
from seed_data import fitness_classes
from pydantic import BaseModel
from datetime import datetime
import pytz
from fastapi import HTTPException, Query
from database import bookings
from schema import BookingRequest, BookingResponse


app = FastAPI()

class ClassResponse(BaseModel):
    id: int
    name: str
    datetime: str
    instructor: str
    available_slots: int


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/classes", response_model=list[ClassResponse])
def get_classes():
    try:
        tz = pytz.timezone(timezone)
    except:
        raise HTTPException(status_code=400, detail="Invalid timezone")
    return [
        {
            "id": cls.id,
            "name": cls.name,
            "datetime": cls.datetime_ist.strftime("%Y-%m-%d %H:%M"),
            "instructor": cls.instructor,
            "available_slots": cls.slots
        }
        for cls in fitness_classes
    ]


@app.post("/book", response_model=BookingResponse)
def book_class(request: BookingRequest):
    cls = next((c for c in fitness_classes if c.id == request.class_id), None)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    if cls.slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")
    
    cls.slots -= 1
    bookings.append({
        "class_id": cls.id,
        "client_name": request.client_name,
        "client_email": request.client_email
    })

    return {"message": "Booking confirmed"}

@app.get("/bookings")
def get_bookings(client_email: str = Query(...)):
    user_bookings = [b for b in bookings if b["client_email"] == client_email]
    return user_bookings