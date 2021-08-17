#!/opt/homebrew/bin/python3

# coding: utf-8
import pikepdf
import argparse


def unlockPdf(filename, password):
    pdf = pikepdf.open(filename, password, allow_overwriting_input=True)
    pdf.save()


def parseArguments():
    parser = argparse.ArgumentParser(description='Python script to unlock password protected pdf files')
    parser.add_argument('files', nargs='+', type=argparse.FileType('rb'), help='the pdf files to unlock')
    parser.add_argument('password', help='the password')

    return parser.parse_args()


def main():
    args = parseArguments()

    for file in args.files:
        print(f'unlocking {file.name}...', end='')
        try:
            file.close()
            unlockPdf(file.name, args.password)
            print('\033[92m DONE\033[00m')
        except:
            print('\033[91m FAILED\033[00m')


if __name__ == '__main__':
    main()
