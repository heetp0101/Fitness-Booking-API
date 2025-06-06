This is simple small Fitness Booking API project to demonstrate the implementation of Fast API 

## Steps to run Fitness Booking API 

1. Clone the Git Repository\
```
git clone https://github.com/heetp0101/Fitness-Booking-API.git
```
2. Install neccessary libraries
  ```
  pip install -r requirements.txt
  ```

3. Start Fast API web application
   ```
   uvicorn main:app --reload
   ```
   > Default application runs at port 8080, you can change by adding port
   ```
   uvicorn main:app --reload --port 8080
   ```

4. Run the curl command in cmd terminal to run API end points
    > API request /classes (to fetch and display upcoming classes)
    ```
    curl http://127.0.0.1:8000/classes
    ```
    > API request /book (to book a class with parameters like class_id, client_name and client_email)
    ```
    curl -X POST http://127.0.0.1:8000/book -H "Content-Type: application/json" -d "{\"class_id\": 1, \"client_name\": \"Sanket\", \"client_email\": \"sanket.patil@gmail.com\"}"
    ```
    > API request /bookings (to fetch the client bookings )
    ```
    curl "http://127.0.0.1:8000/bookings?client_email=sanket.patil@gmail.com"
    ```


