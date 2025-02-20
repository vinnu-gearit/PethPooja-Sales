import requests
import json

# API endpoint URL
url = "https://pethpooja-sales-production.up.railway.app/get_sales_data"

# Headers
headers = {
    "Content-Type": "application/json"
}

# Payload (Same as the one provided)
payload = {
    "token": "",
    "properties": {
        "Restaurant": {
            "res_name": "Petpooja_Rider_Testing",
            "address": "Ahmedabad",
            "contact_information": "1234567890",
            "restID": "bosak1qj"
        },
        "Customer": {
            "name": "Rohan",
            "address": "ahmedbad",
            "phone": "1234567890"
        },
        "Order": {
            "orderID": 78,
            "customer_invoice_id": "78",
            "delivery_charges": 0,
            "order_type": "Dine In",
            "payment_type": "Cash",
            "table_no": "A17",
            "no_of_persons": 0,
            "discount_total": 97.45,
            "tax_total": 0,
            "round_off": "-0.05",
            "core_total": 974.5,
            "total": 887,
            "created_on": "2024-11-25 17:37:31",
            "order_from": "POS",
            "order_from_id": "",
            "sub_order_type": "AC",
            "packaging_charge": 10,
            "status": "Success",
            "comment": "",
            "service_charge": 0
        },
        "Tax": [],
        "Discount": [
            {
                "title": "Special Discount",
                "type": "P",
                "rate": 10,
                "amount": 97.45
            }
        ],
        "OrderItem": [
            {
                "name": "Add Caramel",
                "itemid": 149362613,
                "itemcode": "add caramel",
                "vendoritemcode": "",
                "specialnotes": "",
                "price": 49,
                "quantity": 2,
                "total": 98,
                "addon": [],
                "category_name": "",
                "sap_code": "",
                "discount": 9.8,
                "tax": 0
            }
        ]
    },
    "event": "orderdetails"
}

# Making the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Printing the response
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
