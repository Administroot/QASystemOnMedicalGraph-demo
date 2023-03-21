login_msg = []
try:
    with open("secret/keys.csv", 'r', encoding='utf-8') as f:
        for line in f:
            login_msg = line.split(',')
except IndexError:
    print(IndexError)
    exit(1)
print(login_msg[0], login_msg[1], login_msg[2])
del login_msg
