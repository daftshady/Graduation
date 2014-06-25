table = {}
def setup():
    with open('chars') as chars:
        for char in chars:
            if '|' in char:
                table[char[-3]] = char[:-4].split('|')

def write(word):
    for row in range(len(table.values()[0])):
        for c in word:
            print table[c][row],
        print

if __name__ == '__main__':
    setup()
    write('Fucking KAIST')
