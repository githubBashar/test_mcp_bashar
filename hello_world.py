# Dieses Skript gibt die Nachricht "Hello, World!" aus.
# Es dient als einfaches Beispiel für ein Python-Programm.

messages = ["Hello, World!", "Helloooo", "Hgello Wold"]
for i in range(20):
    message = messages[i % 3]
    for _ in range(5):
        print(message)