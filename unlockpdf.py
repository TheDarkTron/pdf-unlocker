#!/opt/homebrew/bin/python3

# coding: utf-8
import pikepdf
import argparse


def unlockPdf(filename, password):
    pdf = pikepdf.open(filename, password, allow_overwriting_input=True)
    pdf.save()


def parseArguments():
    parser = argparse.ArgumentParser(description='Unlocks pdfs')
    parser.add_argument('files', nargs='+', type=argparse.FileType('rb'), help='the pdf files to unlock')
    parser.add_argument('password', help='the password')

    return parser.parse_args()


def main():
    args = parseArguments()

    for file in args.files:
        print(f'unlocking {file.name}... ', end='')
        try:
            file.close()
            unlockPdf(file.name, args.password)
            print('DONE')
        except:
            print('FAILED')


if __name__ == '__main__':
    main()
