import pandas as pd

# Carregando as bases de dados
df_open_orders = pd.read_excel('data/raw_orders.xlsx')  
df_color_substitution = pd.read_csv('data/color_database.csv')  
df_client_info = pd.read_excel('data/client_info.xlsx')  

print("Data loaded:")
print(f"Open Orders: {df_open_orders.shape}")
print(f"Color Substitution: {df_color_substitution.shape}")
print(f"Travel Schedule: {df_client_info.shape}")

# Preenchendo valores ausentes (NaN) com string vazia
df_client_info['email'] = df_client_info['email'].fillna('')

# Agrupando por client_code e juntando emails de clientes registrados
df_client_info_no_dup = df_client_info.groupby('client_code')['email'].apply(', '.join).reset_index()

# Mesclando dados para adicionar informações como company_name e contact
df_client_info_desc = df_client_info_no_dup.merge(
    df_client_info[['client_code', 'company_name', 'contact']],
    on='client_code',
    how='left'
)

df_paused_items = df_color_substitution[
    (df_color_substitution['current_status'] == 'off')
]

df_open_orders_paused = df_open_orders[df_open_orders['material'].isin(df_paused_items['material'])]

# Criando um novo dataframe com os itens e informações de cada cliente
df_merged_desc = df_open_orders_paused.merge(df_client_info_desc, on='client_code', how='left')

# Mesclando com os dados de substituição de cores
list_fields = ['material', 'replacement_material_1', 'replacement_material_2', 
               'suggested_color', 'brand', 'R', 'G', 'B', 
               'R1', 'G1', 'B1', 'R2', 'G2', 'B2']
df_merged_desc_subs = df_merged_desc.merge(df_paused_items[list_fields], on='material', how='left')
