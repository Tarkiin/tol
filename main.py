import time
import discord


def updateTokens():
    with open('tokens.txt', 'r') as f:
        return f.read().splitlines()


class Onliner:
    def __init__(self, token):
        bot = discord.Client(self_bot=True)
        bot.run(token, bot=False)


def main():
    oldTokens = []
    onlineTokens = []
    while True:
        tokens = updateTokens()
        for token in tokens:
            if not (token in oldTokens):
                onlineTokens.append(Onliner(token))
        time.sleep(300)
        oldTokens = tokens


if __name__ == '__main__':
    main()
