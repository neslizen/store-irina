from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from keyboards import get_models_keyboard, get_model_detail_keyboard, get_main_menu_keyboard, get_back_to_main_keyboard
from data import IPHONE_MODELS, RETURN_RULES, PHOTO_URLS
from config import MANAGER_USERNAME

router = Router()

@router.callback_query(F.data == "catalog")
async def show_catalog(callback: CallbackQuery):
    """Показать каталог моделей"""
    await callback.message.edit_media(
        InputMediaPhoto(
            media=PHOTO_URLS["main_menu"],
            caption="Выберите модель iPhone:"
        ),
        reply_markup=get_models_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_models")
async def back_to_models(callback: CallbackQuery):
    """Вернуться к списку моделей"""
    await callback.message.edit_media(
        InputMediaPhoto(
            media=PHOTO_URLS["main_menu"],
            caption="Выберите модель iPhone:"
        ),
        reply_markup=get_models_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data.startswith("model_"))
async def show_model_detail(callback: CallbackQuery):
    """Показать детальную информацию о модели"""
    model_id = callback.data.replace("model_", "")
    model = IPHONE_MODELS.get(model_id)
    
    if model:
        text = f"{model['name']}\n\n{model['description']}\n💰 Цена: {model['price']}"
        await callback.message.edit_media(
            InputMediaPhoto(
                media=model['photo'],
                caption=text
            ),
            reply_markup=get_model_detail_keyboard(model_id)
        )
    await callback.answer()

@router.callback_query(F.data.startswith("specs_"))
async def show_specs(callback: CallbackQuery):
    """Показать характеристики модели"""
    model_id = callback.data.replace("specs_", "")
    model = IPHONE_MODELS.get(model_id)
    
    if model:
        text = f"📊 Характеристики {model['name']}:\n\n{model['specs']}"
        await callback.message.edit_caption(
            caption=text,
            reply_markup=get_model_detail_keyboard(model_id)
        )
    await callback.answer()

@router.callback_query(F.data.startswith("buy_"))
async def buy_model(callback: CallbackQuery):
    """Обработка покупки"""
    model_id = callback.data.replace("buy_", "")
    model = IPHONE_MODELS.get(model_id)
    
    if model:
        text = f"✅ Для оформления заказа {model['name']} напишите @{MANAGER_USERNAME}"
        await callback.message.edit_caption(
            caption=text,
            reply_markup=get_back_to_main_keyboard()
        )
    await callback.answer()

@router.callback_query(F.data == "show_rules")
async def show_rules(callback: CallbackQuery):
    """Показать правила возврата"""
    await callback.message.edit_caption(
        caption=RETURN_RULES,
        reply_markup=get_back_to_main_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    """Вернуться в главное меню"""
    await callback.message.edit_media(
        InputMediaPhoto(
            media=PHOTO_URLS["main_menu"],
            caption="Добро пожаловать в магазин iPhone! Выберите категорию:"
        ),
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()