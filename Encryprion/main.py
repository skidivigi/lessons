import pyAesCrypt, os

def encryprion(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(str(file), str(file) + '.crp',
                                password, buffer_size)
    print(str(os.path.splitext(file)[0]) +' encrypted.')
    os.remove(file)

def look_in_dirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                encryprion(path, password)
            except Exception as ex:
                print(ex)

        else:
            look_in_dirs(path, password)

password = input('Pls enter ur password:')
dir = input('Pls specify the path:')
def main(dir, password):
    look_in_dirs(dir, password)

if __name__ == '__main__':
    main(dir, password)