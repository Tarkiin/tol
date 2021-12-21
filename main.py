import time
import requests as rq


def updateTokens():
    with open('tokens.txt', 'r') as f:
        return f.read().splitlines()


def main():
    while True:
        tokens = updateTokens()
        for token in tokens:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
            resp = rq.get('https://discord.com/api/v9/users/@me', headers={"authorization": token, "User-Agent": user_agent})
            if resp.status_code != 200:
                print(f'{token} - Token died.')
            time.sleep(5)
        time.sleep(540)


if __name__ == '__main__':
    main()
