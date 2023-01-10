from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'hello, {update.effective_user.first_name}!\n'
                                    '\nВывод чисел НегаФибоначчи)')
   
    await update.message.reply_text(f'Введи целое число и /fib ')


async def fibonacci(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    n = int(update.message.text.split()[1])
    fib_list = [0] * (2 * n + 1)
    fib_list[n + 1], fib_list[n - 1] = 1, 1
    koef = -1
    for i in range(n + 2, 2 * n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        fib_list[-i - 1] = fib_list[i] * koef
        koef *= -1
    await update.message.reply_text(f'Числа :\n\n {fib_list}')

token = ('5986958913:AAFmLYs44wkSthfUJF8XRP0jyU7Ykj00mWA')

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("fib", fibonacci))
app.run_polling()