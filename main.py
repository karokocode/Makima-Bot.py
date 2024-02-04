from discord.ext import commands  # Importa el módulo commands desde discord.ext
import random  # Importa el módulo random

bot = commands.Bot(command_prefix='!')  # Inicializa un bot con el prefijo de comando ejemplo '!'

saludos = ["Hola", "Buenos días", "¿Qué tal?", "¡Hola amigo!", "¡Saludos!"]  # Define una lista de saludos en español

@bot.event  # Decorador para definir un evento del bot
async def on_ready():  # Define una función asincrónica que se ejecuta cuando el bot se conecta
    print('El bot está conectado a Discord!')  # Imprime un mensaje indicando que el bot está conectado a Discord

@bot.command(name='hola', description='Saluda al bot')  # Decorador para definir un comando del bot
async def hola(ctx):  # Define una función asincrónica para el comando 'hola'
    await ctx.send(random.choice(saludos))  # Envia un saludo aleatorio al canal donde se invocó el comando

@bot.command(name='chancho', description='enviar giff de un chancho')  # Decorador para definir un comando del bot
async def chancho(ctx):  # Define una función asincrónica para el comando 'chancho'
    await ctx.send('https://tenor.com/es-419/view/wtf-what-do-you-want-pig-turn-around-looking-gif-18737565')  # Envia un enlace de un GIF de un chancho al canal donde se invocó el comando

bot.run('TOKEN')  # Ejecuta el bot usando el token de autenticación
