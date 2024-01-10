import pyodbc
from fastapi import FastAPI

app = FastAPI()

server = 'server'
database = 'Database'
uid = 'User'
password = '*******'

def get_supplier_rank(int_item_id):
    try:
        connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={uid};PWD={password}'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(f"SELECT intItemID, intSupplierID, Supplier_Rank FROM pre.tblSupplierRank WHERE intItemID = {int_item_id} ORDER BY Supplier_Rank")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append({"intItemID": row.intItemID, "intSupplierID": row.intSupplierID, "Supplier_Rank": row.Supplier_Rank})
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.get("/supplier_rank/{int_item_id}")
async def read_supplier_rank(int_item_id: int):
    return get_supplier_rank(int_item_id)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
