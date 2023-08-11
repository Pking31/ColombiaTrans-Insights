# upload_data.py
import os
from upload_data import authenticate, upload_csv_to_sheet

def upload_tables_to_sheets(json_credentials, spreadsheet_url, tables_folder):
    client = authenticate(json_credentials)

    # Obtener el ID del spreadsheet desde la URL
    spreadsheet_id = spreadsheet_url.split('/')[-2]

    for table_file in os.listdir(tables_folder):
        if table_file.endswith('.csv'):
            table_name = os.path.splitext(table_file)[0]
            sheet_name = table_name[0:30]
            csv_file_path = os.path.join(tables_folder, table_file)
            
            spreadsheet = client.open_by_key(spreadsheet_id)
            try:
                worksheet = spreadsheet.worksheet(sheet_name)
            except:
                worksheet = spreadsheet.add_worksheet(sheet_name, 1, 1)  # Crear hoja si no existe

            upload_csv_to_sheet(client, spreadsheet_url, sheet_name, csv_file_path)
            print(f"Tabla '{table_name}' subida exitosamente a la hoja '{sheet_name}'")

if __name__ == "__main__":
    json_credentials = 'credentials.json'
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1c-z_ayAeWISy9C8Ph60BGjgDpuu4uZJZnQZtYNOxYGM/edit#gid=0'
    tables_folder = 'tablas'  # Ruta de la carpeta de tablas
    
    upload_tables_to_sheets(json_credentials, spreadsheet_url, tables_folder)

