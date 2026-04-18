
import asyncio
import subprocess
from aiogram import Bot, Dispatcher, types

TOKEN = "8553556522:AAHxPB3OAV2zj1J1U-badyJudpMQXGGih68"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handler(message: types.Message):
    username = message.text.strip()

    await message.answer("🔍 Ищу...")

    try:
        result = subprocess.run(
            ["python3", "sherlock/sherlock.py", username, "--print-found"],
            capture_output=True,
            text=True
        )

        output = result.stdout or "❌ Ничего не найдено"

        if len(output) > 3500:
            output = output[:3500] + "\n...обрезано"

        await message.answer(output)

    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
