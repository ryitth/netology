import yadisk


def get_token():
    with open('z:\PY projects\\token.txt') as token:
        return token.readline()


def file_name(full):
    return str(full[full.rfind('\\') + 1:])


y = yadisk.YaDisk(token=get_token())
y.upload('Z:\pic.jpg', file_name('Z:\pic.jpg'))
