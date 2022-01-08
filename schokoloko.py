import websocket
import json
import random
import tkinter.filedialog
import os
import sys
import time
import psutil
import threading

root = tkinter.Tk()
root.withdraw()

mobile = {
    "op": 2,
    "d": {
        "token": "",
        "properties": {
            "$os": "Android",
            "$browser": "Discord Android",
            "$device": "Android 12"
        },
    }
}
pc = {
    "op": 2,
    "d": {
        "token": "",
        "capabilities": 125,
        "properties": {
            "$os": "Windows",
            "$browser": "Chrome",
            "$device": "Windows Device",
            "system_locale": "en-US",
            "browser_user_agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "browser_version": "96.0.4664.45",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 105691,
            "client_event_source": None
        },
        "presence": {
            "status": random.choice(["online", "dnd", "idle"]),
            "since": 0,
            "activities": [],
            "afk": False
        },
        "compress": False,
        "client_state": {
            "guild_hashes": {},
            "highest_last_message_id": "0",
            "read_state_version": 0,
            "user_guild_settings_version": -1,
            "user_settings_version": -1
        }
    },
    "s": None,
    "t": None
}


def WSLogin(token):
    try:
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?encoding=json&v=6")
        mobile["d"]["token"] = token
        pc["d"]["token"] = token
        ws.send(json.dumps(random.choice([pc, mobile])))
        print("Presence Set (%s)" % (token))
        heartbeat = json.loads(ws.recv())['d']['heartbeat_interval']
        while True:
            time.sleep(heartbeat / 1000)
            ws.send(json.dumps({"op": 1, "d": None}))
    except Exception as e:
        print(e)


def gather_tokens():
    tokens = []
    try:
        tokenFile = open(
            tkinter.filedialog.askopenfilename(title="Open Tokens file",
                                               filetypes=(('text files',
                                                           'txt'), )), 'r')
        tokens = tokenFile.read().split("\n")
    except Exception:
        print("Failed to open token file")
        sys.exit()
    return tokens


def keepAllOnlineThreaded(tokens: list):
    for token in tokens:
        threading.Thread(target=lambda: WSLogin(token.split(":")[0])).start()


# print(tokensList)

if __name__ == "__main__":
    tokens = gather_tokens()
    keepAllOnlineThreaded(tokens)