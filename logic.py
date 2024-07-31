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
