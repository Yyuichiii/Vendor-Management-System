
# Vendor Management System

Below are the steps to get started with the project.

## Cloning the Repository

To get started, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Yyuichiii/Vendor-Management-System.git
```

## Installing Dependencies

Navigate to the project directory and install the required dependencies using pip. We recommend using a virtual environment to manage your dependencies.

```bash
cd Vendor-Management-System
pip install -r requirements.txt
```

## Making Migrations

Before running the application, you need to make migrations for the database schema changes. Run the following command:

```bash
python manage.py makemigrations
```

## Migrating the Database

After making migrations, apply them to the database using the following command:

```bash
python manage.py migrate
```

## Creating Superuser

To have administrative privileges in the application, create a superuser account using the following command and follow the prompts:

```bash
python manage.py createsuperuser
```

## Running the Server

Finally, you can run the development server using the following command:

```bash
python manage.py runserver
```

The server will start running at http://127.0.0.1:8000/ by default. 

## API Endpoints

Below are the API endpoints available in this project:

### Vendor Register: `/api/vendors/`

- **Method:** POST
- **Description:** Create the vendor profile.
- **Request Body:**
  ```json
  {
    "vendor_code": "test_tset",
    "name": "test",
    "password": "test1234",
    "password2": "test1234"
  }
  ```

### Vendor List: `/api/vendors/`

- **Method:** GET
- **Description:** List all the vendors.

### Vendor Performace: `/api/vendors/{vendor_id}/performance`

- **Method:** GET
- **Description:** get the vendor performance.


### Vendor-details-update: `/api/vendors/{vendor_id}`

- **Method:** PUT
- **Description:** Update the vendor profile.
- **Request Body:**
  ```json
  {
    "name": "test",
    "contact_details": "test_contacts",
    "address": "test_address"
  }
  ```

### Vendor Delete: `/api/vendors/{vendor_id}`

- **Method:** DELETE
- **Description:** Delete the vendor profile.


### Create Purchase Order: `/api/purchase_orders/`

- **Method:** POST
- **Description:** Create the Purchase Order.
- **Request Body:**
  ```json
  {
    "po_number":"afdgdsdfdfdgdcd",
    "vendor":1,
    "delivery_date":"2024-05-06",
    "quantity":5,
    "items":{
        "id":1,
        "name":"tsst"
          }
  }
  ```

### Purchase Order list: `/api/purchase_orders/`

- **Method:** GET
- **Description:** Get the Purchase orders list.

### Purchase Order Details: `/api/purchase_orders/{po_id}`

- **Method:** GET
- **Description:** Get the Purchase order based on the id provided.


### Update Purchase Order: `/api/purchase_orders/{po_id}`

- **Method:** PUT
- **Description:** Update the Purchase Order.
- **Request Body:**
  ```json
  {
    "po_number":"assd"
  }
  ```

### Delete Purchase Order: `/api/purchase_orders/{po_id}`

- **Method:** DELETE
- **Description:** Delete the Purchase Order.

### Purchase Order Acknowlege: `/api/purchase_orders/{po_id}/acknowledge`

- **Method:** POST
- **Description:** Acknowledge the Purchase order by the Vendor.

### Complete Purchase Order: `/api/purchase_orders/{po_id}/completed`

- **Method:** POST
- **Description:** Complete the Purchase order by the Vendor
- **Request Body:**
  ```json
  {
    "rating": 3
  }
  ```

### Vendor Performance History: `/api/vendors/{po_id}/history_performance`

- **Method:** GET
- **Description:** Get the Performance history of the vendor for the future evaluation.



