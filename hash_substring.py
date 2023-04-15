# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    type=input().strip().upper()
    if type == 'I':
        findtxt=input().strip()
        txt=input().strip()
    elif type == 'F':
        file ='/workspaces/string-pattern-kristapsskudra/tests/06'
        with open(file,'r') as f:
            findtxt = f.readline().strip()
            txt = f.readline().strip()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return findtxt, txt

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(findtxt, txt):
    # this function should find the occurances using Rabin Karp alghoritm 
    occurrences = []
    find_len = len(findtxt)
    txt_len = len(txt)
    find_hesh = hash(findtxt)
    txt_hesh = hash(txt[:find_len])
    # check text for length txt - pattern length
    for i in range(txt_len - find_len +1):
        if find_hesh == txt_hesh and findtxt == txt[i:i+find_len]:
            occurrences.append(i)
        if i < txt_len - find_len:
            txt_hesh = hash(txt[i+1:i+find_len+1])
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

