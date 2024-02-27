import discord
from discord.ext import commands
import openai

TOKEN = "TOKEN"
CHANNEL_ID = "CHANNEL_ID"
API_KEY = "API_KEY"
openai.api_key = API_KEY

bot = commands.Bot(command_prefix="@", intents=discord.Intents.all())


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    content = message.content
    messages = [{"role": "system", "content": "ask question after my response and tell the answer related to what i responded"},  # behaviour
            {"role": "user", "content": content},  # asking question
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    response = completion.choices[0].message.content
    print(response)
    messages.append({"role": "assistant", "content": response})
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"{response}")

bot.run(TOKEN)
