import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0iTtq0Ib1--xzE'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me a file, and I'll save it for you!")

def save_file(update: Update, context: CallbackContext) -> None:
    file = update.message.document
    file_id = file.file_id
    file_name = file.file_name

    # Create a directory for saving files
    folder_name = "received_files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Inform the user that the file is being processed
    update.message.reply_text(f"Processing the file '{file_name}'...")

    # Download the file using the file_id in chunks
    file_url = context.bot.get_file(file_id).file_path
    response = requests.get(file_url, stream=True)

    # Save the file in the created directory
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    update.message.reply_text(f"File '{file_name}' has been saved in the '{folder_name}' folder!")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("application/*"), save_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
