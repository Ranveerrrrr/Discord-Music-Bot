import discord
from discord.ext import commands
import yt_dlp
import os

# ---------------- CONFIG ---------------- #

BOT_TOKEN = "ADD_YOUR_TOKEN_HERE"

FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

FFMPEG_OPTIONS = {
    "executable": FFMPEG_PATH,
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn -ac 2 -ar 48000 -loglevel panic"
}

YDL_OPTIONS = {
    "format": "bestaudio[acodec=opus]/bestaudio",
    "quiet": True,
    "default_search": "ytsearch",
    "source_address": "0.0.0.0",
    "noplaylist": True,
    "extract_flat": False,
}

# ---------------------------------------- #

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        return await ctx.send("❌ Join a voice channel first")

    if ctx.voice_client:
        return await ctx.send("✅ Already in a voice channel")

    await ctx.author.voice.channel.connect(
        timeout=60,
        reconnect=True,
        self_deaf=True
    )

    await ctx.send("🎧 Joined voice channel")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Left voice channel")


@bot.command()
async def play(ctx, *, search: str):
    if not ctx.author.voice:
        return await ctx.send("❌ Join a voice channel first")

    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()

    vc = ctx.voice_client

    if vc.is_playing():
        vc.stop()

    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(search, download=False)
        if "entries" in info:
            info = info["entries"][0]

        url = info["url"]
        title = info["title"]

    source = discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)
    vc.play(source)

    await ctx.send(f"🎶 Now playing: **{title}**")


@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("⏸ Paused")


@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("▶️ Resumed")


@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.send("⏹ Stopped")


bot.run(BOT_TOKEN)

