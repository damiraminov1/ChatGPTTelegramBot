import os
import telebot
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    prompt = message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response.choices[0].text)

bot.polling()
