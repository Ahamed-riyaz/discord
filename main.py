import discord
from discord.ext import commands
import openai

TOKEN = "MTA4NzI1MjE1NzA2Mjk3OTU4NA.GiaZeB.nie5kaQWzzkhF5JFchDdjd4vvqnO_eRATL626A"
CHANNEL_ID = 1087254649196785664
API_KEY = "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"
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

# @bot.command()
# async def hello(arg)
    # content = arg.content
    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You're an AI"},  # behaviour
    #         {"role": "user", "content": content},  # asking question
    #     ]
    # )
    # response = completion.choices[0].message.content
    # res = {"role": "assistant", "content": response}
    # channel = bot.get_channel(CHANNEL_ID)
    # # print(f"CHATGPT {response}")
    # await channel.send(f"{response}")


bot.run(TOKEN)
