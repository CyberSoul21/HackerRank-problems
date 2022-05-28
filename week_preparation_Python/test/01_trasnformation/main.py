


def transformation(in_out_word):
    #write code
    lst = in_out_word.split()
    orig = lst[0]
    encr = lst[1]
    conc = ''
    for x in orig:
        if x.isupper():
            if x in encr: 
                conc += str(encr.index(x)) + 'O'
            elif x.lower() in encr:
                conc += str(encr.index(x.lower())) + 'L'    
        elif x.islower():
            if x in encr: 
                conc += str(encr.index(x)) + 'O'
            elif x.upper() in encr:
                conc += str(encr.index(x.upper())) + 'U'                                
    return conc

if __name__ == '__main__':
    words = input().strip()
    print(transformation(words))    
