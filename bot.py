import discord
from classes.chained_list import Chained_list
from classes.hashmap import Hashmap
from classes.binary_tree import Discusion_tree
from classes.binary_tree import Node
from discord.ext import commands
import os
import json
import signal
import sys
import requests
from googletrans import LANGUAGES 
from googletrans import LANGCODES
from googletrans import Translator

intents = discord.Intents.all()

history_list = Chained_list()

hashmap = Hashmap(10)

discusion = Discusion_tree()
discusion.first_node = Node("Besoin d'aide ?")

discusion.add_message("Commande ?","oui","Besoin d'aide ?")
discusion.add_message("Fin","non","Besoin d'aide ?")

discusion.add_message("Historique ?","oui","Commande ?")
discusion.add_message("Fin","non","Commande ?")

discusion.add_message("!history pour voir votre historique","oui","Historique ?")
discusion.add_message("Stocker ?","non","Historique ?")

discusion.add_message("!store pour stocker votre historique","oui","Stocker ?")
discusion.add_message("Dernière commande tapé ?","non","Stocker ?")

discusion.add_message("!last pour regarder la dernière commande tapé","oui","Dernière commande tapé ?")
discusion.add_message("Nettoyer l'historique ?","non","Dernière commande tapé ?")

discusion.add_message("!clear pour nettoyer l'historique","oui","Nettoyer l'historique ?")
discusion.add_message("Faire une traduction ?","non","Nettoyer l'historique ?")

discusion.add_message("!translate (langue en anglais) (votre texte que vous voulez traduire)","oui","Faire une traduction ?")
discusion.add_message("Recherche de site ou image ?","non","Faire une traduction ?")

discusion.add_message("!search (type de recherche image ou site) (votre recherche)","oui","Recherche de site ou image ?")
discusion.add_message("Regarder la météo d'une ville ?","non","Recherche de site ou image ?")

discusion.add_message("!weather (ville ou pays en anglais)","oui","Regarder la météo d'une ville ?")
discusion.add_message("Fin","non","Regarder la météo d'une ville ?")

# function to replace the default action of control C (two parameters required, nomenclature of signal package)def handle_interrupt(_, __):
def handle_interrupt(_,__):
    print("Arrêt du Bot...")
    print("Sauvegarde...")
    j = json.dumps(hashmap.buckets)

    with open("sample.json", "w") as outfile:
        outfile.write(j)
    sys.exit(0)

# control C will take the action of the function set after
signal.signal(signal.SIGINT, handle_interrupt)

if os.path.isfile("./sample.json"):  
    f = open('sample.json')

    hashmap.load(json.load(f))

    for i in hashmap.buckets:
        if i != []:
            a = i[0]
            history_list.append((a[0], a[1]))
else :
    print("pas de sauvegarde")


# our bot, we specify it's a command bot, we specify the command prefix, intents -> the rights we give to the bot
bot = commands.Bot(command_prefix="!", intents = intents, help_command=None)

# Print the content, when the bot is online
@bot.event
async def on_ready(): 
    print("Le bot est prêt !") 

# Sends an error message when the user types a command incorrectly (command does not exist)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Commande non trouvée. Utilisez `{bot.command_prefix}help` pour voir la liste des commandes.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Un ou plusieurs arguments manquants. Utilisez `{bot.command_prefix}help` pour voir la liste des commandes.")
    else:
        # Gère d'autres erreurs
        print(f"Une erreur inattendue s'est produite: {error}")


# To view the history of the user typing the command
@bot.command(name="history")
async def show_history(ctx):
    history_list.append((ctx.author.id,ctx.message.content))
    display_command = "Votre liste de commande / mot spécial commençant par $ : " + history_list.get_commands_with_userId(ctx.author.id)
    await ctx.send(display_command)

# To see the last command/special word linked to the user typing the command
@bot.command(name="last")
async def show_history(ctx):
    # history_list.append((ctx.author.id,ctx.message.content))
    await ctx.send(history_list.last_index(ctx.author.id)[1])

# To clear all history 
@bot.command(name="clear")
async def show_history(ctx):
    history_list.append((ctx.author.id,ctx.message.content))
    
    history_list.clean()

    await ctx.send("Votre historique a été vidé ! ")

# To store your data (history linked to the user typing the command)
@bot.command(name="store")
async def store_history(ctx):
   history_list.append((ctx.author.id,ctx.message.content))   
   users_commands = history_list.get_commands_with_userId(ctx.author.id)
   hashmap.set(ctx.author.id, users_commands)
   await ctx.send("Vous avez stocké votre historique !")

# Starts a command help discussion
@bot.command(name="help")
async def help(ctx):
    history_list.append((ctx.author.id,ctx.message.content))
    loop = True
    def check(m: discord.Message):  # m = discord.Message.
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 

    while loop == True:
        await ctx.send("Mettez oui ou non, si vous voulez quitté répondez stop")
        if discusion.current_conversation_node != None:
            await ctx.send(discusion.current_conversation_node.message)
        else:
             await ctx.send(discusion.first_node.message)

        if discusion.current_conversation_node != None:
            if discusion.current_conversation_node.yes_node == None and discusion.current_conversation_node.no_node == None:
                await ctx.send("Au revoir !")
                break

        msg = await bot.wait_for('message', check=check, timeout = 60.0)

        content = msg.content.lower()

        if content == "stop":
            await ctx.send("Au revoir !")
            break

        if discusion.check_yes_or_no(content) == True:
            discusion.next_message(content)
        else:
            await ctx.send("Vous devez mettre oui ou non, d'autre réponse ne marcheront pas")

# Reset the discussion
@bot.command(name="reset")
async def reset_tree(ctx):
    history_list.append((ctx.author.id,ctx.message.content))
    discusion.current_conversation_node = None
    await ctx.send("Vous avez réinitialisé la discussion avec le bot discord")

# To translate a text give by the user
@bot.command(name="translate")
async def translate(ctx, lang_to, *, args):
    history_list.append((ctx.author.id, ctx.message.content))
    languages = LANGUAGES
    langcodes = LANGCODES

    lang_to = lang_to.lower()
    if lang_to not in languages and lang_to not in langcodes:
        await ctx.send("Langue invalide")
    translator = Translator()

    try:
        translation = translator.translate(args, dest=lang_to, src='auto')
        original_text = translation.origin
        translated_text = translation.text

        result_message = (
            f"**Traduction**\n"
            f"De : {translator.detect(original_text).lang}\n"
            f"À : {lang_to.capitalize()}\n"
            f"Texte original : {original_text}\n"
            f"Texte traduit : {translated_text}"
        )

        await ctx.send(result_message)

    except Exception as e:
        await ctx.send(f"Une erreur s'est produite lors de la traduction : {str(e)}")

# To search a site or image
@bot.command(name="search")
async def search(ctx,type,*, search):
    history_list.append((ctx.author.id, ctx.message.content))

    api_key = "AIzaSyBlmZGx8MgGNbL8YFsDAEg558Pl4b4gP_I"
    search_key = "01a2e115871b54854"
    url = "https://www.googleapis.com/customsearch/v1/"

    search_query = search.lower()

    params_site = {
        'q': search_query,
        'key': api_key,
        'cx': search_key
    }

    params_image = {
        'q': search_query,
        'key': api_key,
        'cx': search_key,
        'searchType': 'image'
    }

    if type == "site":
        response = requests.get(url, params=params_site).json()

        if 'items' in response and response['items']:
            await ctx.send(f"Résultat de recherche pour '{search}':\n{response['items'][0]['link']}")
        else:
            await ctx.send(f"Aucun résultat trouvé pour '{search}', veuillez changer de recherche.")

    elif type == 'image':
        response = requests.get(url, params=params_image).json()

        if 'items' in response and response['items']:
            await ctx.send(f"Image trouvée pour '{search}':\n{response['items'][0]['link']}")
        else:
            await ctx.send(f"Aucune image trouvée pour '{search}', veuillez changer de recherche.")

    else:
        await ctx.send("Type de recherche invalide. Veuillez utiliser 'site' pour un site ou 'image' pour une image.")


# To have weather of a city or country
@bot.command(name="weather")
async def weather(ctx, *, args):
    history_list.append((ctx.author.id, ctx.message.content))
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "19d383d8d0361e1bf9049a65c9226148"
    city = args
    url = base_url + "appid=" + api_key + "&q=" + city

    def kelvin_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return round(celsius)

    response = requests.get(url).json()

    if response['cod'] == '404':
        await ctx.send("La ville n'a pas été trouvée.")
    else:
        temp = response['main']['temp']
        temp_celsius = kelvin_to_celsius(temp)
        feels_like = response['main']['feels_like']
        feels_like_celsius = kelvin_to_celsius(feels_like)
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']

        result_message = (
            f"**Météo pour {city.capitalize()}**\n"
            f"Conditions: {description.capitalize()}\n"
            f"Température actuelle: {temp_celsius} °C\n"
            f"Ressentie: {feels_like_celsius} °C\n"
            f"Humidité: {humidity}%"
        )

        await ctx.send(result_message)

# Append in the history all word starts with "$"
@bot.event 
async def on_message(message): 

  if message.content.startswith("$"):
    history_list.append((message.author.id, message.content)) 

  await bot.process_commands(message) 

# launch the bot (with token key)
bot.run("MTE2NzQ2OTIxMDk1MjI3Mzk5MQ.GY729o.hkQRJ97pLKOnAdXtv9ABMN0mdeSDLV5IEun7p8")