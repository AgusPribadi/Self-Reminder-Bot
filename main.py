import telebot

api = '5671732652:AAHXOWs9Vxuhx_ZUOtAZw4dDns31L27ftq0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Halo selamat datang, silahkan ketik angka 1-10 ya (menggunakan tanda /)')

@bot.message_handler(commands=['1'])
def send_pertama(message):
    bot.reply_to(message, 'Jangan lupa minum air putih ya')

@bot.message_handler(commands=['2'])
def send_kedua(message):
    bot.reply_to(message, 'Saat merasa pekerjaanmu terhambat, coba sedekah ke orang-orang yang membutuhkan')

@bot.message_handler(commands=['3'])
def send_ketiga(message):
    bot.reply_to(message, 'Saat sedang gelisah coba ingat Allah dan segera shalat tahajud')

@bot.message_handler(commands=['4'])
def send_keempat(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

@bot.message_handler(commands=['5'])
def send_kelima(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

@bot.message_handler(commands=['6'])
def send_keenam(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

@bot.message_handler(commands=['7'])
def send_ketujuh(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

@bot.message_handler(commands=['8'])
def send_kedelapan(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

@bot.message_handler(commands=['9'])
def send_kesembilan(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

@bot.message_handler(commands=['10'])
def send_kesepuluh(message):
    bot.reply_to(message, 'Jika kamu merasa miskin, ingatlah masih ada orang yang lebih miskin')

print('Bot Start Running')
bot.polling()