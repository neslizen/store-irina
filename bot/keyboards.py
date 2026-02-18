from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import IPHONE_MODELS

def get_start_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для стартового экрана"""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="📜 Правила возврата",
        callback_data="show_rules_start"
    ))
    builder.row(InlineKeyboardButton(
        text="✅ Я ознакомлен(а) и подтверждаю",
        callback_data="confirm_rules"
    ))
    return builder.as_markup()

def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Главное меню"""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="📱 Актуальные модели",
        callback_data="catalog"
    ))
    builder.row(InlineKeyboardButton(
        text="📞 Связаться с поддержкой",
        callback_data="support"
    ))
    builder.row(InlineKeyboardButton(
        text="📖 Правила возврата",
        callback_data="show_rules"
    ))
    return builder.as_markup()

def get_models_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура со списком моделей"""
    builder = InlineKeyboardBuilder()
    
    for model_id, model_data in IPHONE_MODELS.items():
        builder.row(InlineKeyboardButton(
            text=model_data["name"],
            callback_data=f"model_{model_id}"
        ))
    
    builder.row(InlineKeyboardButton(
        text="↩️ Назад в главное меню",
        callback_data="back_to_main"
    ))
    
    return builder.as_markup()

def get_model_detail_keyboard(model_id: str) -> InlineKeyboardMarkup:
    """Клавиатура для детальной информации о модели"""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="💾 Характеристики",
            callback_data=f"specs_{model_id}"
        ),
        InlineKeyboardButton(
            text="💰 Купить",
            callback_data=f"buy_{model_id}"
        )
    )
    builder.row(InlineKeyboardButton(
        text="↩️ Назад к списку моделей",
        callback_data="back_to_models"
    ))
    return builder.as_markup()

def get_back_to_main_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с кнопкой возврата в главное меню"""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="🏠 В главное меню",
        callback_data="back_to_main"
    ))
    return builder.as_markup()