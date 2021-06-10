sharp_key = ['C','G','D','A','E','B','F#']
flat_key = ['F','Bb','Eb','Ab','Db','Gb']
sharp = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
flat = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

def sharp_or_flat(key):
    if key in sharp_key:
        return True
    else:
        return False

def get_notes():
    if is_sharp == True:
        return sharp
    else:
        return flat

def major_key(k):
    key_map = [0,2,4,5,7,9,11]
    key_get = []
    i = 0
    while i<7:
        key_get.append(notes[(k+key_map[i])%12])
        i = i+1
    return key_get
    
key_in = input()
is_sharp = sharp_or_flat(key_in)
notes = get_notes()
index = notes.index(key_in)
print(major_key(index))