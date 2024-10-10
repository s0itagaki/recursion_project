def reverse_file(inputpath, outputpath):
    if not isinstance(inputpath, str):
        print('第一引数には文字列(ファイルパス)を渡してください。')
        return None
    if not isinstance(inputpath, str):
        print('第二引数には文字列(ファイルパス)を渡してください。')
        return None
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(outputpath, 'x') as f:
        f.write(contents[::-1])

def copy_file(inputpath, outputpath):
    if not isinstance(inputpath, str) or not isinstance(outputpath, str):
        print('第一引数には文字列(ファイルパス)を渡してください。')
        return None
    if not isinstance(inputpath, str) or not isinstance(outputpath, str):
        print('第二引数には文字列(ファイルパス)を渡してください。')
        return None
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)

def duplicate_contents(inputpath, n):
    if not isinstance(inputpath, str):
        print('第一引数には文字列(ファイルパス)を渡してください。')
        return None
    if not isinstance(n, int):
        print('第二引数には数字を渡してください。')
        return None
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(inputpath, 'a') as f:
        for _ in range(n):
            f.write('\n' + contents)

def replace_string(inputpath, word='needle', newword='newstring'):
    if not isinstance(inputpath, str):
        print('第一引数には文字列(ファイルパス)を渡してください。')
        return None
    with open(inputpath, 'r') as f:
        contents = f.read()
        contents = contents.replace(word, newword)
    with open(inputpath, 'w') as f:
        f.write(contents)

if __name__ == '__main__':
    inputpath = 'sample.txt'
    # reverse_file(inputpath, 'test1.txt')
    # copy_file(inputpath,'test2.txt')
    # duplicate_contents('sample.txt', 2)
    # replace_string(inputpath)
