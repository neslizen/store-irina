from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import get_start_keyboard, get_main_menu_keyboard
from data import RETURN_RULES, PHOTO_URLS

router = Router()

class UserState(StatesGroup):
    """Состояния пользователя"""
    waiting_for_confirmation = State()
    confirmed = State()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    """Обработчик команды /start"""
    await state.set_state(UserState.waiting_for_confirmation)
    
    await message.answer_photo(
        photo=PHOTO_URLS["main_menu"],
        caption="Перед покупкой ознакомьтесь с правилами возврата товара.",
        reply_markup=get_start_keyboard()
    )

@router.callback_query(F.data == "show_rules_start")
async def show_rules_start(callback: CallbackQuery):
    """Показать правила возврата из стартового экрана"""
    await callback.message.edit_caption(
        caption=RETURN_RULES,
        reply_markup=get_start_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "confirm_rules")
async def confirm_rules(callback: CallbackQuery, state: FSMContext):
    """Подтверждение ознакомления с правилами"""
    await state.set_state(UserState.confirmed)
    
    await callback.message.edit_media(
        InputMediaPhoto(
            media=PHOTO_URLS["main_menu"],
            caption="Добро пожаловать в магазин iPhone! Выберите категорию:"
        ),
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()

@router.message(UserState.waiting_for_confirmation)
async def handle_unconfirmed_message(message: Message, state: FSMContext):
    """Обработка сообщений от неподтвержденных пользователей"""
    await message.answer_photo(
        photo=PHOTO_URLS["main_menu"],
        caption="Перед покупкой ознакомьтесь с правилами возврата товара.",
        reply_markup=get_start_keyboard()
    )

@router.callback_query(F.data == "back_to_main", UserState.confirmed)
async def back_to_main_confirmed(callback: CallbackQuery):
    """Вернуться в главное меню для подтвержденных пользователей"""
    await callback.message.edit_media(
        InputMediaPhoto(
            media=PHOTO_URLS["main_menu"],
            caption="Добро пожаловать в магазин iPhone! Выберите категорию:"
        ),
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()