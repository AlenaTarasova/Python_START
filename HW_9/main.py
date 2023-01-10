# 2 задача
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'hello, {update.effective_user.first_name}!\n'
                                    'перевод в двоичеую систему исчисления')
    await update.message.reply_text(f'Введите число и /bin')


async def binary_sistem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    int_num = int(update.message.text.split()[1])
    print_num = int_num
    print(int_num)
    double_num = ''
    while int_num > 0:
        double_elem = int_num % 2
        int_num = int_num // 2
        double_num += str(double_elem)
    await update.message.reply_text(f'число в двоичной системе {print_num}: {int(double_num[::-1])}')


token = ('5986958913:AAFmLYs44wkSthfUJF8XRP0jyU7Ykj00mWA')

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("bin", binary_sistem))
app.run_polling()
