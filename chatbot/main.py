from Controller.botController import*

# Bot entra em loop
bot.message_loop({
    "chat": receive_message,
    "callback_query": on_callback_query
})

while True:
    pass
