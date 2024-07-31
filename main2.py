import matplotlib.pyplot as plt

def create_map(cities):
    """
    Создает карту с городами.
    
    Parameters:
    cities (list of tuple): Список городов в формате [(name, (latitude, longitude)), ...]
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    # Координаты для всех городов
    lats = [city[1][0] for city in cities]
    longs = [city[1][1] for city in cities]

    ax.scatter(longs, lats, color='skyblue', s=100)

    # Отмечаем города
    for city in cities:
        name, (lat, long) = city
        ax.text(long, lat, name, fontsize=12, ha='right')

    return fig, ax

def draw_map(fig, ax):
    """
    Рисует карту с городами.
    
    Parameters:
    fig, ax: Объекты matplotlib.figure.Figure и matplotlib.axes.Axes
    """
    plt.show()
Шаг 2: Файл bot.py
bot.py
python
Копировать код
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from logic import create_map
import io
from PIL import Image

# Список городов (название, (широта, долгота))
cities = [
    ("Moscow", (55.7558, 37.6173)),
    ("Saint Petersburg", (59.9343, 30.3351)),
    ("Novosibirsk", (55.0084, 82.9357)),
    # Добавьте остальные города
]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для отображения городов на карте.')

def draw_all_cities(update: Update, context: CallbackContext) -> None:
    fig, ax = create_map(cities)
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    update.message.reply_photo(photo=buf)

def draw_city(update: Update, context: CallbackContext) -> None:
    city_name = ' '.join(context.args)
    city = next((city for city in cities if city[0].lower() == city_name.lower()), None)
    
    if not city:
        update.message.reply_text(f'Город {city_name} не найден.')
        return
    
    fig, ax = create_map([city])
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    update.message.reply_photo(photo=buf)

def main():
    updater = Updater("YOUR_TOKEN", use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("draw_all_cities", draw_all_cities))
    dp.add_handler(CommandHandler("draw_city", draw_city))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
