    #XadievDev
#36-lesson.Funksiyalarni tekshirish

#------------------------------------------------------------------#

# import unittest

# from name_test import get_full_name

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('amirbek','xadiev')
#         self.assertEqual(formatted_name,'Amirbek Xadiev')

# unittest.main()

#------------------------------------------------------------------#

# import unittest
# from name_test import get_full_name

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('alijon','valiyev')        
#         self.assertEqual(formatted_name, 'Alijon Valiyev')
#     def test_toliq_ism_otasi(self):
#         name = get_full_name('hasan','husanov','olimovich')
#         self.assertEqual(name,'Hasan Olimovich Husanov')

# unittest.main()

#------------------------------------------------------------------#

# import unittest
# from name_test import getArea, getPerimeter

# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertAlmostEqual(getArea(10), 314.159)
#         self.assertAlmostEqual(getArea(3),28.27431)
#     def test_perimeter(self):
#         self.assertAlmostEqual(getPerimeter(10), 62.8318)
#         self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
# unittest.main()

#------------------------------------------------------------------#

# import unittest
# from name_test import katta_kichik

# class KattaKichik(unittest.TestCase):
#     def kkichik(self):
#         b = katta_kichik(5,6,7)
#         self.assertEqual(b,7)

# unittest.main()

#------------------------------------------------------------------#

# import unittest
# from name_test import katta

# class KattaYoz(unittest.TestCase):
#     def kyoz(self):
#         matn = katta("amirbek xadiev 2006-yil.")
#         self.assertEqual(matn,'Amirbek Xadiev 2006-Yil.')

# unittest.main()

#------------------------------------------------------------------#

import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = ""  # <-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()