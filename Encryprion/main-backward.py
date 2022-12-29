import pyAesCrypt, os

def decryprion(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]),
                                               password, buffer_size)

    print(str(os.path.splitext(file)[0]) +' decrypted.')
    os.remove(file)

def look_in_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decryprion(path, password)
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