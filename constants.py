import os
import json
import random

# Pokémon Categories
SAFARI = set([])
NEST_BALL = set([])
ULTRA_BALL = set([])
GREAT_BALL = set([])
REGULAR_BALL = set([
    "Bulbasaur", "Ivysaur", "Charmander", "Squirtle", "Charmeleon", "Wartortle", "Pidgey", "Pidgeotto", "Vulpix", "Ninetales",
    "Zubat", "Golbat", "Meowth", "Mankey", "Primeape", "Growlithe", "Abra", "Kadabra", "Tentacool", "Tentacruel", "Golem",
    "Farfetch'd", "Grimer", "Muk", "Shellder", "Gastly", "Haunter", "Voltorb", "Marowak", "Rhyhorn", "Rhydon", "Horsea", "Seadra",
    "Staryu", "Starmie", "Mr. Mime", "Scyther", "Tauros", "Magikarp", "Lapras", "Vaporeon", "Flareon", "Jolteon", "Porygon", "Dratini",
    "Dragonair", "Cyndaquil", "Quilava", "Totodile", "Croconaw", "Lanturn", "Togepi", "Togetic", "Mareep", "Flaaffy", "Espeon", "Gligar",
    "Sneasel", "Teddiursa", "Ursaring", "Houndour", "Kingdra", "Porygon2", "Blissey", "Treecko", "Grovyle", "Torchic", "Combusken", "Mudkip",
    "Marshtomp", "Lotad", "Lombre", "Slakoth", "Vigoroth", "Ninjask", "Electrike", "Anorith", "Bagon", "Shelgon", "Chimchar", "Monferno", "Piplup",
    "Prinplup", "Turtwig", "Starly", "Staravia", "Buizel", "Floatzel", "Buneary", "Gible", "Gabite", "Riolu", "Skorupi", "Croagunk", "Porygon-Z",
    "Froslass", "Tepig", "Pignite", "Lillipup", "Herdier", "Pidove", "Tranquill", "Drilbur","Timburr", "Gurdurr", "Basculin", "Sandile", "Krokorok",
    "Darmanitan", "Dwebble", "Scraggy", "Archen", "Zorua", "Zoroark", "Cinccino", "Ducklett", "Swanna", "Karrablast", "Escavalier", "Frillish", "Joltik",
    "Ferroseed", "Litwick", "Lampent", "Axew", "Fraxure", "Cryogonal", "Shelmet", "Accelgor", "Mienfoo", "Druddigon", "Golett", "Rufflet", "Vullaby", "Durant",
    "Deino", "Zweilous", "Larvesta", "Volcarona", "Chespin", "Quiladin", "Fennekin", "Braixen", "Delphox", "Greninja", "Fletchling", "Fletchinder", "Talonflame",
    "Litleo", "Flabebe", "Floette", "Skiddo", "Pancham", "Clauncher", "Helioptile", "Heliolisk", "Tyrunt", "Amaura", "Hawlucha", "Sylveon", "Goomy", "Sliggoo",
    "Phantump", "Trevenant", "Pumpkaboo", "Avalugg", "Noibat", "Rowlet", "Dartrix", "Decidueye", "Litten", "Torracat", "Popplio", "Brionne", "Pikipek", "Trumbeak",
    "Vikavolt", "Wishiwashi", "Mareanie", "Toxapex", "Mudbray", "Salandit", "Bounsweet", "Steenee", "Oranguru", "Passimian", "Wimpod", "Turtonator", "Mimikyu",
    "Jangmo-o", "Hakamo-o", "Grookey", "Thwackey", "Scorbunny", "Raboot", "Sobble", "Drizzile", "Rookidee", "Corvisquire", "Orbeetle", "Chewtle", "Yamper", "Rolycoly",
    "Carkol", "Applin", "Flapple", "Arrokuda", "Sizzlipede", "Hatenna", "Hattrem", "Impidimp", "Morgrem", "Perrserker", "Mr. Rime", "Morpeko", "Cufant", "Dracozolt",
    "Arctozolt", "Dracovish", "Arctovish", "Duraludon", "Wyrdeer", "Kleavor", "Sneasler", "Overqwil"
])

REPEAT_BALL = set([
    "Charizard", "Blastoise", "Venusaur", "Alakazam", "Pidgeot", "Snorlax", "Munchlax", "Rotom", "Drakloak", "Beedrill", "Slowbro", "Gengar", "Kangaskhan",
    "Pinsir", "Gyarados", "Aerodactyl", "Ampharos", "Steelix", "Scizor", "Heracross", "Houndoom", "Tyranitar", "Sceptile", "Blaziken", "Gardevoir", "Gallade",
    "Sableye", "Mawile", "Absol", "Aggron", "Medicham", "Manectric", "Sharpedo", "Camerupt", "Altaria", "Banette", "Glalie", "Salamence", "Beldum", "Metang",
    "Metagross", "Lopunny", "Lucario", "Audino", "Mewtwo", "Lugia", "Ho-Oh", "Rayquaza", "Latias", "Latios", "Groudon", "Kyogre", "Deoxys", "Arceus", "Giratina",
    "Dialga", "Palkia", "Regigigas", "Victini", "Kyurem", "Zekrom", "Reshiram", "Terrakion", "Virizion", "Zacian", "Zamazenta", "Spectrier", "Cosmog", "Cosmoem",
    "Xerneas", "Yveltal", "Zygarde"
])

# Hunting Team
POKEMON_TEAM = [
    "Corvisquire", "Sceptile", "Snorlax",
    "Sliggoo", "Scizor", "Solgaleo"
]   # Add your preferred Pokémon for hunting here

# Owner and Bot Information
OWNER_NAME = "Vegeta"
BOT_VERSION = "1.0"

# Commands
PING_COMMAND_REGEX = r'^\.ping$'
ALIVE_COMMAND_REGEX = r'^\.alive$'
HELP_COMMAND_REGEX = r'^\.help$'
EVAL_COMMAND_REGEX = r'^\.eval (.+)'
GUESSER_COMMAND_REGEX = r'^\.guess (on|off|stats)$'
HUNTER_COMMAND_REGEX = r'^\.hunt (on|off|stats)$'
LIST_COMMAND_REGEX = r'^\.list(?:\s+(\w+))?$'  # Now supports `.list <category>`

# AFK Commands
AFK_COMMAND_REGEX = r'^\.afk(?: |$)(.*)'  # Matches `.afk` or `.afk <message>`
UNAFK_COMMAND_REGEX = r'^\.unafk$'  # Matches `.unafk`

# Timing and Limits
COOLDOWN = lambda: random.randint(2, 3)  # Random cooldown between 3 and 6 seconds
PERIODICALLY_GUESS_SECONDS = 120  # Guess cooldown
PERIODICALLY_HUNT_SECONDS = 300  # Hunt cooldown (5 minutes)
HEXA_BOT_ID = 572621020  # ID of the Hexa bot

# Auto-Battle Constants
HUNT_DAILY_LIMIT_REACHED = "Daily hunt limit reached. Auto-battle stopped."
SHINY_FOUND = "Shiny Pokémon found! Auto-battle stopped for {0}."

# API Credentials
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION = os.getenv('SESSION')

# Chat ID
CHAT_ID = int(os.getenv('CHAT_ID'))

# Load Pokémon Data
with open('pokemon.json', 'r') as f:
    POKEMON = json.load(f)

__version__ = '1.0.0'
