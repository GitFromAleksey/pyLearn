import argparse
# import optparse



def main():
    parser = argparse.ArgumentParser(prog='MY_CLI Prog', description='this is a description!')
    # parser.add_argument('a', type=int, help='a-help') # обязательный аргумент
    parser.add_argument('-b', type=int, help='b-help') # необязательный аргумент
    parser.add_argument('-f', type=argparse.FileType('r',encoding='utf-8')) # передача файла
    args = parser.parse_args()
    print(f'args: {args}')
    if args.f:
        for line in args.f:
            print(f'file: {line}')

if __name__ == '__main__':
    main()