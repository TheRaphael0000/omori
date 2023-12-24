import base64
for line in open("roboheart.txt").read().split("\n"):
    print(base64.b64decode(line).decode("ascii"))
