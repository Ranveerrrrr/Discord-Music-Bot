# Discord Music Bot (Python)

A **free, open-source Discord music bot** built with **Python** that plays high-quality music in voice channels using **yt-dlp** and **FFmpeg**.

This project is beginner-friendly, lightweight, and does **not require any paid services**.

---

## Features
- Join & leave voice channels
- Play music using song names or links
- High-quality audio playback
- ⏸ Pause / ▶ Resume / ⏹ Stop
- Song end notification
- 100% free & open source

---

## Requirements

Make sure you have the following installed:

- **Python 3.10+**
- **FFmpeg**
- **Discord Bot Token**
- Internet connection

---

## Step 1: Create a Discord Bot Application

1. Go to the **Discord Developer Portal**  
   https://discord.com/developers/applications

2. Click **New Application**
3. Give it a name and click **Create**

### Add a Bot
1. Open your application
2. Go to **Bot** (left sidebar)
3. Click **Add Bot**
4. Copy the **Bot Token**

 **Never share or commit your bot token to GitHub**

---

## Step 2: Enable Required Intents

In the **Bot** section, enable:
- ✅ **Message Content Intent**

Click **Save Changes**.

---

## Step 3: Invite the Bot to Your Server

1. Go to **OAuth2 → URL Generator**
2. Scopes:
   - ☑️ `bot`
3. Bot Permissions:
   - ☑️ Connect
   - ☑️ Speak
   - ☑️ Send Messages
   - ☑️ Read Message History
4. Copy the generated URL
5. Open it in your browser and invite the bot to your server

---

## Step 4: Install Dependencies

Install required Python libraries:

```bash
pip install -U discord.py yt-dlp PyNaCl
```

---

## Step 5: Install FFmpeg (Windows)

1. Download FFmpeg from:
   https://www.gyan.dev/ffmpeg/builds/
2. Download **ffmpeg-release-essentials.zip**
3. Extract it to:
   ```
   C:\ffmpeg\
   ```
4. Make sure this file exists:
   ```
   C:\ffmpeg\bin\ffmpeg.exe
   ```
   
---

## Step 6: Store Bot Token Safely (IMPORTANT)

Create a `.env` file
```
DISCORD_TOKEN=your_bot_token_here
```

Add `.env` to `.gitignore`
```
.env
```
This prevents your token from being leaked.

---

## Step 7: Run the Bot
   ```bash
   python music_bot.py
   ```

If successful, you should see:
```
Logged in as <YourBotName>
```
   
---

## Bot Commands
Join a voice channel first, then use these commands in a text channel:
   ```commands
   !join
  !play <song name or link>
  !pause
  !resume
  !stop
  !leave
   ```

Examples:
  ```
  !play believer imagine dragons
  !play https://www.youtube.com/watch?v=7wtfhZwyrcc
  ```
   
---

## Audio Quality Notes
For best audio quality:
- Use headphones in stereo mode
- Avoid Bluetooth headset microphones (hands-free mode)
- Use a separate microphone if possible

---

 ## Project Structure
 ```
Discord-Music-Bot/
│
├── music_bot.py
├── README.md
├── .gitignore
└── .env   (not committed)
```

---

## Known Limitations
- Discord re-encodes audio (lossless audio is not possible)
- Spotify audio cannot be streamed directly (DRM)
- Works best with YouTube audio sources

---

## License
This project is licensed under the MIT License.

---

##⭐ Support

If you like this project:
⭐ Star the repository
🍴 Fork it
🛠 Improve it
Contributions and suggestions are welcome.
