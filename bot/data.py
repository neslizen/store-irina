# data.py - Данные о товарах с фото

# URL фотографий (можно заменить на свои ссылки)
PHOTO_URLS = {
    "main_menu": "https://freeimage.host/i/qdmsiLN",  # Главное фото магазина
    "iphone_15_pro": "https://freeimage.host/i/qdpf5pR",
    "iphone_15": "https://freeimage.host/i/qdpf5pR",
    "iphone_14": "https://freeimage.host/i/qdpf5pR",
    "iphone_13": "https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fdicentre.ru%2Fsotovye-telefony%2Fapple%2Fiphone-13%2F128gb%2Fsmartfon-apple-iphone-13-128gb-a2633-belyy%2F&ved=0CBYQjRxqFwoTCOiy-6P24JIDFQAAAAAdAAAAABAf&opi=89978449",
    "iphone_se_2022": "https://freeimage.host/i/qdpf5pR"
}

# Данные о моделях iPhone
IPHONE_MODELS = {
    "iphone_15_pro": {
        "name": "iPhone 15 Pro",
        "description": "Флагманская модель с титановым корпусом",
        "price": "119 990 руб.",
        "specs": "Экран: 6.1″ Super Retina XDR\nПроцессор: A17 Pro\nКамера: 48 МП\nАккумулятор: До 23 ч воспроизведения видео",
        "photo": PHOTO_URLS["iphone_15_pro"]
    },
    "iphone_15": {
        "name": "iPhone 15",
        "description": "Инновации в доступном флагмане",
        "price": "79 990 руб.",
        "specs": "Экран: 6.1″ Super Retina XDR\nПроцессор: A16 Bionic\nКамера: 48 МП\nАккумулятор: До 20 ч воспроизведения видео",
        "photo": PHOTO_URLS["iphone_15"]
    },
    "iphone_14": {
        "name": "iPhone 14",
        "description": "Отличная камера и производительность",
        "price": "69 990 руб.",
        "specs": "Экран: 6.1″ Super Retina XDR\nПроцессор: A15 Bionic\nКамера: 12 МП\nАккумулятор: До 20 ч воспроизведения видео",
        "photo": PHOTO_URLS["iphone_14"]
    },
    "iphone_13": {
        "name": "iPhone 13",
        "description": "Надежный и проверенный временем",
        "price": "59 990 руб.",
        "specs": "Экран: 6.1″ Super Retina XDR\nПроцессор: A15 Bionic\nКамера: 12 МП\nАккумулятор: До 19 ч воспроизведения видео",
        "photo": PHOTO_URLS["iphone_13"]
    },
    "iphone_se_2022": {
        "name": "iPhone SE (2022)",
        "description": "Компактный и мощный",
        "price": "49 990 руб.",
        "specs": "Экран: 4.7″ Retina HD\nПроцессор: A15 Bionic\nКамера: 12 МП\nАккумулятор: До 15 ч воспроизведения видео",
        "photo": PHOTO_URLS["iphone_se_2022"]
    }
}

# Текст правил возврата
RETURN_RULES = """
📜 Правила возврата товара:

https://telegra.ph/PRAVILA-OBMENA-I-VOZVRATA-TOVARA-NADLEZHASHCHEGO-KACHESTVA-IRINA-STORE-02-17

По вопросам возврата обращайтесь к @holodnovat
"""