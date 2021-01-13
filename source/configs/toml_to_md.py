import os

if __name__ == "__main__":
    files = []
    for filename in os.listdir('.'):
        if '.toml' in filename:
            files.append(filename)
    for filename in files:
        f = open(filename, 'r', encoding="utf-8")
        f.close()
        f = open(filename.replace('.toml', '.rst'), 'w', encoding="utf-8")

        f.write(filename+'\n')
        for i in range(len(filename)+1):
            f.write('-')
        f.write('\n\n')
        f.write('.. literalinclude:: {}'.format(filename))
        f.write('\n    :linenos:')
        f.write('\n')
        f.write('\n')
        f.close()
        


    