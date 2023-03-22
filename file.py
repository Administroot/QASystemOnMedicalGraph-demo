login_msg = []
try:
    with open("secret/keys.csv", 'r', encoding='utf-8') as f:
        login_msg = [line.split(',') for line in f]
except IndexError:
    print(IndexError)
    exit(1)

for i in range(len(login_msg[0])):
    print(f'login_msg[0][{i}]={login_msg[0][i]}')
del login_msg
