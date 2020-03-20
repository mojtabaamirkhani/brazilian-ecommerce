import pandas as pd
import numpy as np
import plotly
import sklearn
from matplotlib import pyplot as plt

df_customers=pd.read_parquet('df_customers.parquet')
df_locations=pd.read_parquet('df_locations.parquet')
df_items=pd.read_parquet('df_items.parquet')
df_payments=pd.read_parquet('df_payments.parquet')
df_reviews=pd.read_parquet('df_reviews.parquet')
df_orders=pd.read_parquet('df_orders.parquet')
df_products=pd.read_parquet('df_products.parquet')
df_sellers=pd.read_parquet('df_sellers.parquet')

df_items['shipping_limit_date']=pd.to_datetime(df_items['shipping_limit_date'],infer_datetime_format=True)
df_reviews['review_creation_date']=pd.to_datetime(df_reviews['review_creation_date'],infer_datetime_format=True)
df_reviews['review_answer_timestamp']=pd.to_datetime(df_reviews['review_answer_timestamp'],infer_datetime_format=True)
df_orders['order_purchase_timestamp']=pd.to_datetime(df_orders['order_purchase_timestamp'],infer_datetime_format=True)
df_orders['order_approved_at']=pd.to_datetime(df_orders['order_approved_at'],infer_datetime_format=True)
df_orders['order_delivered_carrier_date']=pd.to_datetime(df_orders['order_delivered_carrier_date'],infer_datetime_format=True)
df_orders['order_delivered_customer_date']=pd.to_datetime(df_orders['order_delivered_customer_date'],infer_datetime_format=True)
df_orders['order_estimated_delivery_date']=pd.to_datetime(df_orders['order_estimated_delivery_date'],infer_datetime_format=True)
