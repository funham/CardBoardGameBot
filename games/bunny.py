games = {}

def on_message(message):
    contentArr = message['text'].split()[1:]
    if contentArr[0] == 'init':
        games[id] = {
            "players": int(contentArr[1])
        }