from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = '5557234590:AAFHF1tYQcJDgeWVM4g5jUnRjeJZ0dbsFiw'
ADMINS = [827124888]
IP = 'localhost'

