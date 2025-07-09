# Dieses Skript gibt Nachrichten aus, die in einer Schleife alternierend angezeigt werden.
# Die Nachrichten werden in einer Liste gespeichert und basierend auf dem Modulo-Wert der Iteration darauf zugegriffen.
# Dadurch wird die Wiederholung von Code reduziert und die Lesbarkeit verbessert.

messages = ["Hello, World!", "Helloooo", "Hgello Wold"]
for i in range(20):
    message = messages[i % 3]
    for _ in range(5):
        print(message)