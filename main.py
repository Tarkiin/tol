import time
import discord


def updateTokens():
    with open('tokens.txt', 'r') as f:
        return f.read().splitlines()


def main():
    oldTokens = []
    while True:
        tokens = updateTokens()
        for token in tokens:
            if not (token in oldTokens):
                bot = discord.Client(self_bot=True)
                bot.run(token, bot=False)
        time.sleep(300)
        oldTokens = tokens


if __name__ == '__main__':
    main()
