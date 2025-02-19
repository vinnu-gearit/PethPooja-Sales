from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
import uvicorn

# Load environment variables from .env file (for local development)
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# MongoDB Connection
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)
db = client["PethPooja"]
collection = db["Sales"]

# Define data models
class Restaurant(BaseModel):
    res_name: str
    address: str
    contact_information: str
    restID: str

class Customer(BaseModel):
    name: str
    address: str
    phone: str

class Discount(BaseModel):
    title: str
    type: str
    rate: float
    amount: float

class OrderItem(BaseModel):
    name: str
    itemid: int
    itemcode: str
    vendoritemcode: Optional[str] = ""
    specialnotes: Optional[str] = ""
    price: float
    quantity: int
    total: float
    addon: List = []
    category_name: Optional[str] = ""
    sap_code: Optional[str] = ""
    discount: float
    tax: float

class Order(BaseModel):
    orderID: int
    customer_invoice_id: str
    delivery_charges: float
    order_type: str
    payment_type: str
    table_no: Optional[str] = None
    no_of_persons: int
    discount_total: float
    tax_total: float
    round_off: str
    core_total: float
    total: float
    created_on: str
    order_from: str
    order_from_id: Optional[str] = ""
    sub_order_type: Optional[str] = ""
    packaging_charge: float
    status: str
    comment: Optional[str] = ""
    service_charge: float

class Properties(BaseModel):
    Restaurant: Restaurant
    Customer: Customer
    Order: Order
    Tax: List = []
    Discount: List[Discount]
    OrderItem: List[OrderItem]

class DumpData(BaseModel):
    token: Optional[str] = ""
    properties: Properties
    event: str

# Define the API endpoint
@app.post("/get_sales_data")
async def get_sales_data(data: DumpData):
    # Convert data to dictionary & add a timestamp
    data_dict = data.dict()
    data_dict["received_at"] = datetime.utcnow()

    # Insert into MongoDB
    result = collection.insert_one(data_dict)

    return {"message": "Data saved successfully", "status": "success", "inserted_id": str(result.inserted_id)}

# Add a GET endpoint to retrieve data
@app.get("/sales_data")
async def get_all_sales_data():
    data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB _id field
    return data

# Add a root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the Sales Data API"}



# @app.get("/")
# def read_root():
#     return {"message": "Hello, Railway!"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Change 8000 to use $PORT