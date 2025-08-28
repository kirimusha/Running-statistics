import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ---------- Загружаем данные ----------
data = pd.read_excel("running stat.xlsx")

# ---------- Преобразуем даты ----------
data['data'] = pd.to_datetime(data['data'], dayfirst=True)
data = data.sort_values('data')

# ---------- Считаем дельту ----------
data['delta_days'] = data['data'].diff().dt.days

# ---------- Строим график ----------
plt.figure(figsize=(14, 6))
plt.plot(data['data'], data['delta_days'], color='orange', linestyle='-')

# ---------- Настройка осей ----------
plt.xlabel("Дата пробежки")
plt.ylabel("Дельта дней с предыдущей пробежки")
plt.title("Дельта времени между пробежками")

# Больше дат на оси X
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # отметка каждого месяца
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))  # формат даты
plt.xticks(rotation=45, ha='right')  # наклон подписей

plt.grid(True)
plt.tight_layout()
plt.show()
