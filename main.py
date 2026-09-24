import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, eu sou o {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def enviar_arq(ctx):
    envio = ctx.message.attachments

    if envio:
        for arquivo in envio:
            nome_arquivo = arquivo.filename
            url_arquivo = arquivo.url
            print(f"Arquivo recebido: {nome_arquivo} - URL: {url_arquivo}")

            await arquivo.save(f"save/{nome_arquivo}")
            await ctx.send("Arquivo recebido!")
    else:
        await ctx.send("Nenhum arquivo enviado.")

@bot.command()
async def classificar(ctx):
    envio = ctx.message.attachments

    if envio:
        for arquivo in envio:
            nome_arquivo = arquivo.filename
            url_arquivo = arquivo.url
            print(f"Arquivo recebido: {nome_arquivo} - URL: {url_arquivo}")

            classe, confianca = get_class("keras_model.h5", "labels.txt", f"save/{nome_arquivo}")

            await arquivo.save(f"save/{nome_arquivo}")
            if confianca < 0.3:
                await ctx.send(f"Não tenho certeza do que está sendo enviado na imagem, Tente novamente!")
            else:
                await ctx.send(f"Arquivo recebido! Personagem: {classe} - Confiança: {confianca:.2f}")
    else:

            await ctx.send("Oops! Nenhum arquivo enviado...")
bot.run("TOKEN")
