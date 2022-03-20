# Creado por: Ricardo Andres Caceres Villibord
# Matricula: A01706972
# Clase: TC2037.850

import re
from time import sleep
from tokenize import group
import winsound
import math


cancion2 = '''
#TITLE J. S. Bach Well-Tenpered Clavier, f , Prelude no. 11
F5e C5e A4s G4e A4s C5s F4s A4s C5s# E5s D5s C5h
'''

cancion = '''
F5e C5e A4s G4e A4s C5s F4s A4s C5s E#5s Db5s C5h
'''
notes_arr = [440, "A", 493, "B",261, "C", 293, "D", 229, "E", 349, "F", 392, "G"]
tvalues = [4000, "w", 2000, "h", 1000, "q", 500, "e", 250, "s", 125, "t", 62, "f"]

comments = re.compile(r'#TITLE[a-z]*(-|.)*(\s)*(\d)*')
pattern = re.compile(r'[A-G](#|b)?[0-8]?(w|h|q|e|s|t|f)?')
octave =  re.compile(r'[0-3]|[5-8]')
tval =  re.compile(r'(w|h|q|e|s|t|f)')
pitch = re.compile(r'(#|b)')

comentarios = comments.finditer(cancion2)
for comment in comentarios:
    print("Tocando la siguiente cancion: ")
    print(comment.group(0))


matches = pattern.finditer(cancion)
print("\nLAS NOTAS DETECTADAS SON: ")
for match in matches:
    print("\n")
    print(match)
    print(match.group(0))
    tono = pitch.search(match.group(0))
    octava = octave.search(match.group(0))
    tvalue = tval.search(match.group(0))
    if octava is None:
        for letra in match.group(0):
            # print(letra)
            for note in notes_arr:
                if note == letra:
                    freq_index = notes_arr.index(letra)-1
                    for tiempo in tvalues:
                        if tiempo == tvalue.group(0):
                            print("Octava: 4")
                            print("Frequency: " + str(notes_arr[freq_index]))
                            print("Duracion: " + str(tvalue.group(0)))
                            if tono is None:
                                winsound.Beep(notes_arr[freq_index], tvalues[tvalues.index(tiempo)-1])
                                sleep(0.5)
                            else:
                                modFreq = notes_arr[freq_index] * math.pow(2, 1/12)
                                print("Frequency with sharp or flat: " + str(modFreq))
                                winsound.Beep(round(modFreq), tvalues[tvalues.index(tiempo)-1])
                                sleep(0.5)
    else:
        # print("Octava:")
        print("Octava: " + octava.group(0))
        octava = int(octava.group(0))
        if (octava > 4): 
            resta = octava - 4
            i=1
            for letra in match.group(0):
                for note in notes_arr:
                    if note == letra:
                        freq_index = notes_arr.index(letra)-1
                        freq = notes_arr[freq_index] 
                        while i <= resta:
                            freq = freq * 2
                            i = i + 1
                        print("Frequency: " + str(freq))
                        for tiempo in tvalues:
                            if tiempo == tvalue.group(0):
                                print("Duracion: " + str(tvalue.group(0)))
                                if tono is None:
                                    winsound.Beep(freq, tvalues[tvalues.index(tiempo)-1])
                                    sleep(0.5)
                                else:
                                    modFreq = freq * math.pow(2, 1/12)
                                    print("Frequency with sharp or flat: " + str(modFreq))
                                    winsound.Beep(round(modFreq), tvalues[tvalues.index(tiempo)-1])
                                    sleep(0.5)

        elif (octava < 4):
            resta = 4 - octava 
            i=1
            for letra in match.group(0):
                for note in notes_arr:
                    if note == letra:
                        freq_index = notes_arr.index(letra)-1
                        freq = notes_arr[freq_index]
                        while i <= resta:
                            freq = round(freq / 2)
                            i = i + 1
                        # print(freq)
                        for tiempo in tvalues:
                            if tiempo == tvalue.group(0):
                                print("Frequency: " + str(freq))
                                print("Duracion: " + str(tvalue.group(0)))
                                winsound.Beep(freq, tvalues[tvalues.index(tiempo)-1])
                                sleep(0.5)

sleep(1)