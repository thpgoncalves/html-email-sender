from data_processing import df_merged_desc_subs
from email_service.gmail_email_service import send_email

# Lista de informações processadas
info_fields = ['client_code', 'contact', 'sales_doc', 'material', 'item', 'R', 'G', 'B', 'suggested_color', 'brand']

def process_and_send_email(dataframe):
    rows = dataframe.shape[0]
    print(f"Processing {rows} rows in the dataframe.")
    for i in range(rows):
        suggested_color = dataframe.iloc[i]['suggested_color']
        print(f"Row {i}: Suggested color = {suggested_color}")

        if suggested_color == 1:
            print(f"Sending email for row {i} with substitution type 1.")
            auxiliary_list = ['R1', 'G1', 'B1', 'Material_1']
            details = dataframe.iloc[i][info_fields + auxiliary_list]
            details = details.rename({'Material_1': 'replacement_material', 'R1': 'R_replacement', 'G1': 'G_replacement', 'B1': 'B_replacement'})
            send_email(details)
            break
        elif suggested_color == 2:
            print(f"Sending email for row {i} with substitution type 2.")
            auxiliary_list = ['R2', 'G2', 'B2', 'Material_2']
            details = dataframe.iloc[i][info_fields + auxiliary_list]
            details = details.rename({'Material_2': 'replacement_material', 'R2': 'R_replacement', 'G2': 'G_replacement', 'B2': 'B_replacement'})
            send_email(details)
            break
        else:
            print(f"Row {i}: No substitution found.")

process_and_send_email(df_merged_desc_subs)