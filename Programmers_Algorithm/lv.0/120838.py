def solution(letter):
    letter = letter.split(' ')
    print(letter)
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    for i in range(len(letter)):
        letter[i] = morse[letter[i]]
    return ''.join(letter)

stri = ".... . .-.. .-.. ---"
print(solution(stri))