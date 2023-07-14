import pickle
#from player import U


def file2data(pickled):
    try:
        with open(pickled, 'rb') as jar:
            return pickle.load(jar)
    except AttributeError as e:
        print('this is probably an instance of a usermade class')
        print('you may need the class (attribute) below to go with this..')
        print(f'*** {e} ')
        print('ie. import the class before unpickling this file')
        

def typecheck(thedata):
    if thedata is None:
        return 
    types = [list, type, dict]
    for each in types:
        print(f'{each}: {type(thedata)==each}')
    print(type(thedata))
    print(f'length: {len(thedata)}')


def test(pickled='horselist.dat'):
    thedata = file2data(pickled)
    typecheck(thedata)



if __name__ == '__main__':
    test()
