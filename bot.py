import discord
from discord.ext import commands
import random
import os
import servidorweb
from dotenv import load_dotenv
load_dotenv() 


# Cargar el .env ANTES de buscar la variable
load_dotenv()

# Guardar el token en la variable
DISCORD_TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

#---------------saludos-------------------

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

respuestas_hola = [
    "klk bb soy galcii, na mentira jaja",
    "Hola que hij@ de puta? hable bien",
    "Hola bb",
    "Epa, buenas buenas",
    "¿Que quieres zorrita??",
    "¡Hola! ¿Cómo estás? 😎",
    "Holaaaaas, qué más pues 🔥",
    "Epa, llegó alguien 👋",
    "Buenas buenas, ¿todo bien?",
    "Hola bb 😹",
    "Qué más, máquina 😎",
    "Saludos, criatura del internet 🤖",
    "Hola, espero que tengas un buen día ✨",
    "Ey ey, ¿qué se cuenta?",
    "Llegó el saludo oficial de Emma.bot 🤖",
    "¿Otra vez tú por aquí? 😂",
    "Mira quién apareció jajaja",
    "Pensé que nunca ibas a saludar 😴",
    "Hola pues, no seas tímido 😎",
    "Bienvenido al rincón del caos 🔥",
    "Aquí estamos, dando servicio 🫡",
    "Un saludo para ti, campeón 🏆",
    "Qué hubo, leyenda 😎",
    "Todo bien por acá, ¿y tú?",
    "Hola humano, sigo funcionando 🤖",
    "¿Eso era todo? ¿Un hola? 😂",
    "Wow, qué saludo tan elaborado 😐",
    "Me esforcé más yo respondiendo que tú escribiendo eso 😭",
    "Hola... supongo 😑",
    "Excelente aporte al servidor 😂",
    "Un saludo de parte del robot trabajador 🫡",
    "¿Vienes a saludar o a molestar? 👀",
    "Te estaba esperando (mentira, soy un bot) 🤖",
    "Otra persona activando mi comando 😭",
    "Mi programación dice que debo saludarte 😎",
    "Epa mi llave, qué más pues 🔥",
    "Quiubo parcero, todo bien?",
    "Buenas buenas 😎",
    "No me hables que ando ocupadita optimizando el juego",
    "Holaaaaaa. Saludos desde la nube ☁️",
    "Bla bla bla, chao canson(a)",
    "Hola 👋",
    "Un saludo de calidad premium 😂",
    "Hola hola, doble saludo para ti",
    "Klk, ¿qué me cuenta el más insano del Blood Strike?",
    "¿Otra vez usando comandos? Ya duermeee",
    "Creo que te gusta hablar conmigo 🤨",
    "Holaaaa me alegra verte 🙄",
    "Pa que me necesitas? 🙄",
    "Hola, usuario misterioso 👀",
    "holaaaas jijiji",
    "Que se te antoja bb??",
    "Saludos aceptados",
    "Emma.bot reportándose",
    "Hola, ¿qué me cuentas?"
]

@bot.event
async def on_message(message):

    # Evita que Emma se responda sola
    if message.author == bot.user:
        return

    # Convierte todo a minúsculas
    texto = message.content.lower()

    # Detecta "Emma hl"
    if texto.startswith("emma hl"):

        mensaje = random.choice(respuestas_hola)

        embed = discord.Embed(
            description=mensaje,
            color=0xbf58ca
        )

        await message.reply(embed=embed)

    # Mantiene funcionando otros comandos
    await bot.process_commands(message)
#-------------------final de saludo-------------------

# Iniciar servidor web
servidorweb.comandodeinicio()

# Arrancar el bot con la variable correcta
bot.run(DISCORD_TOKEN)