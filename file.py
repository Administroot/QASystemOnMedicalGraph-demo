try:
    with open("secret/keys.csv", 'r', encoding='utf-8') as f:
        login_msg = {line.strip().split(',')[0]:line.strip().split(',')[1] for line in f }
        print(login_msg['hello'])
except IndexError:
    print(IndexError)
    exit(1)

print(login_msg)
del login_msg
