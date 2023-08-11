import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def authenticate(json_credentials):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_credentials, scope)
    client = gspread.authorize(credentials)
    return client


def upload_csv_to_sheet(client, spreadsheet_url, sheet_name, csv_file_path):
    try:
        spreadsheet = client.open_by_url(spreadsheet_url)
        worksheet = spreadsheet.worksheet(sheet_name)

        df = pd.read_csv(csv_file_path)
        values = df.values.tolist()

        headers = df.columns.tolist()
        worksheet.update('A1', [headers])

        for row in values:
            try:
                worksheet.append_row(row)
            except gspread.exceptions.APIError as api_error:
                print(f"Error al agregar fila a la hoja '{sheet_name}': {api_error}")
    except gspread.exceptions.APIError as api_error:
        print(f"Error al abrir hoja de cálculo o hoja '{sheet_name}': {api_error}")
    except pd.errors.EmptyDataError as empty_data_error:
        print(f"Error al leer archivo CSV '{csv_file_path}': {empty_data_error}")
    except Exception as e:
        print(f"Error desconocido: {e}")

def upload_tables_to_sheets(json_credentials, spreadsheet_url, tables_folder):
    client = authenticate(json_credentials)

    # Obtener nombre del spreadsheet desde la URL
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