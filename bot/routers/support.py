from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from keyboards import get_back_to_main_keyboard, get_main_menu_keyboard
from config import SUPPORT_USERNAME
from data import PHOTO_URLS

router = Router()

@router.callback_query(F.data == "support")
async def show_support(callback: CallbackQuery):
    """Показать контакты поддержки"""
    text = f"📞 По всем вопросам пишите @{SUPPORT_USERNAME}"
    await callback.message.edit_media(
        InputMediaPhoto(
            media=PHOTO_URLS["main_menu"],
            caption=text
        ),
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