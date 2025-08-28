import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ---------- Загружаем таблицу ----------
file_path = "running stat.xlsx"
df = pd.read_excel(file_path, sheet_name="Лист1")
df["data"] = pd.to_datetime(df["data"], errors='coerce')
df = df.sort_values("data")

# ---------- Функция для графика с читаемыми датами ----------
def plot_metric_with_readable_dates(y_column, ylabel, title, color="red"):
    plt.figure(figsize=(12,5))
    ax = plt.gca()
    
    # Рисуем линию
    ax.plot(df["data"], df[y_column], color=color)
    
    # Настройка X
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # показываем каждый месяц
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # сокращённый формат
    plt.xticks(rotation=45)  # подписи читаемые
    
    # Настройка Y
    y_min, y_max = df[y_column].min(), df[y_column].max()
    ax.set_yticks(np.linspace(y_min, y_max, 10))  # 10 делений
    
    # Сетка
    ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
    ax.grid(which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
    
    ax.set_title(title)
    ax.set_xlabel("Дата")
    ax.set_ylabel(ylabel)
    plt.show()

# ---------- Построение всех трёх графиков ----------
plot_metric_with_readable_dates("average pace, /km", "Мин/км", "Средний темп (мин/км)", color="red")
plot_metric_with_readable_dates("distance, km", "Км", "Дистанция пробежек (км)", color="green")
plot_metric_with_readable_dates("average speed, km/h", "Км/ч", "Средняя скорость (км/ч)", color="orange")

