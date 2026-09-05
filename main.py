import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

main_menu = ReplyKeyboardMarkup(
    [
        ["≡ƒôï Menyu", "Γä╣∩╕Å Ma'lumot"],
        ["≡ƒô₧ Aloqa", "Γ¥ô Yordam"]
    ],
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Kerakli bo'limni tanlang:",
        reply_markup=main_menu
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "≡ƒôï Menyu":
        await update.message.reply_text(
            "≡ƒôï Menyu bo'limi\n\n"
            "Bu yerda turli xil variantlar bor.\n"
            "Boshqa bo'limlarga o'ting yoki savol bering!"
        )

    elif text == "Γä╣∩╕Å Ma'lumot":
        await update.message.reply_text(
            "Γä╣∩╕Å Ma'lumot bo'limi\n\n"
            "Bot haqida ma'lumot:\n"
            "- Bot 24/7 ishlaydi\n"
            "- Uzluksiz xizmat ko'rsatadi\n"
            "- Tez va ishonchli"
        )

    elif text == "≡ƒô₧ Aloqa":
        await update.message.reply_text(
            "≡ƒô₧ Aloqa uchun:\n\n"
            "Telefon: +998903544777\n"
            "Telegram: @jah0n_299"
        )

    elif text == "Γ¥ô Yordam":
        await update.message.reply_text(
            "Γ¥ô Yordam bo'limi\n\n"
            "Savolingiz bo'lsa:\n"
            "1. Savol yozing\n"
            "2. Javob kutib turing\n"
            "3. Ishonchli javoblar olasiz"
        )

    else:
        await update.message.reply_text("Iltimos, menyudan birini tanlang.")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
