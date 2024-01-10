# Supplier Rank API

This API retrieves `intItemID`, `intSupplierID`, and `Supplier_Rank` from a SQL Server table (`pre.tblSupplierRank`) for a specific `int_item_id`.

## Requirements

- Python 3.7+
- pyodbc
- FastAPI
- uvicorn

## Setup

1. **Clone the repository:**

   git clone https://github.com/your-username/supplier-rank-api.git

2. **Navigate to the project directory:**

   cd supplier-rank-api

3. **Create a Python virtual environment (recommended):**

   python3 -m venv venv

4. **Activate the virtual environment:**

   - **Windows:**

     venv\Scripts\activate

   - **Unix or MacOS:**

     source venv/bin/activate

5. **Install the required packages:**

   pip install -r requirements.txt

6. **Configure the SQL Server connection details in the code:**

   Open main.py and modify the following variables:

   server = 'your_server_name'
   database = 'YourDatabase'
   uid = 'YourUser'
   password = 'YourPassword'

7. **Run the FastAPI server:**

   uvicorn main:app --reload

## Usage

### Retrieving Supplier Rank

Send a GET request to http://127.0.0.1:8000/supplier_rank/{int_item_id}.

Replace {int_item_id} with the desired intItemID to get the corresponding intSupplierID and Supplier_Rank.

Example:

curl http://127.0.0.1:8000/supplier_rank/123

## Support

For any issues or queries, please open an issue here: https://github.com/your-username/supplier-rank-api/issues.
