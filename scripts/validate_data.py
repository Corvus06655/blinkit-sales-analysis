from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / 'blinkit_data.csv')
expected = {'Item Fat Content', 'Item Identifier', 'Item Type', 'Outlet Establishment Year', 'Outlet Identifier', 'Outlet Location Type', 'Outlet Size', 'Outlet Type', 'Item Visibility', 'Item Weight', 'Sales', 'Rating'}
assert set(df.columns) == expected, f'Unexpected columns: {set(df.columns) - expected}'
assert len(df) == 8523, f'Unexpected row count: {len(df)}'
assert int(df.duplicated().sum()) == 0, 'Duplicate rows found.'
assert pd.to_numeric(df['Sales'], errors='coerce').notna().all(), 'Sales contains non-numeric values.'
assert (df['Sales'] >= 0).all(), 'Sales contains negative values.'
assert round(float(df['Sales'].sum()), 2) == 1201681.48, f'Unexpected total sales: {df["Sales"].sum()}'
assert round(float(pd.to_numeric(df['Rating'], errors='coerce').mean()), 2) == 3.97, 'Average rating changed; review the source extract.'
clean_fat = df['Item Fat Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
assert set(clean_fat.dropna().unique()) <= {'Low Fat', 'Regular'}, 'Unexpected fat-content labels found.'
print('Blinkit validation passed')
print(f'rows={len(df)} total_sales={df["Sales"].sum():.2f} average_rating={df["Rating"].mean():.2f}')
