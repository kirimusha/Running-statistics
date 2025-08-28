import pandas as pd

file_path = "running stat.xlsx"
df = pd.read_excel(file_path, sheet_name="Лист1")

# ---------- Проверяем типы ----------
print(df.dtypes)

# ---------- Преобразуем даты ----------
df["data"] = pd.to_datetime(df["data"], errors='coerce')

# ---------- Преобразуем числовые колонки ----------
numeric_cols = ["average pace, /km", "distance, km", "average speed, km/h"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nПосле конвертации:")
print(df.dtypes)

# ---------- Проверим на пропуски ----------
print("\nКоличество пропусков по колонкам:")
print(df[["data"] + numeric_cols].isna().sum())
