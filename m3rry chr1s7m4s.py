import winsound as sound
n={'C4':261,'C#4':277,'D4':293,'D#4':311,
   'E4':329,'F4':349,'F#4':370,'G4':392,'G#4':415,'A4':440,
   'A#4':466,'B4':494,'C5':523,'C#5':554,'D5':587}
w=1000*2
h=500*2
q=250*2
e=125*2
s=62*2

def playnote(note,dur):
    
    sound.Beep(n[note],dur)
while True:
    playnote('C4',q)

    playnote('F4',q)
    playnote('F4',e)
    playnote('G4',e)
    playnote('F4',e)
    playnote('E4',e)

    playnote('D4',q)
    playnote('D4',q)
    playnote('D4',q)

    playnote('G4',q)
    playnote('G4',e)
    playnote('A4',e)
    playnote('G4',e)
    playnote('F4',e)

    playnote('E4',q)
    playnote('E4',q)
    playnote('E4',q)

    playnote('A4',q)
    playnote('A4',e)
    playnote('A#4',e)
    playnote('A4',e)
    playnote('G4',e)

    playnote('F4',q)
    playnote('D4',q)
    playnote('C4',e)
    playnote('C4',e)

    playnote('D4',q)
    playnote('G4',q)
    playnote('E4',q)

    playnote('F4',w)
    playnote('C4',q)

    playnote('F4',q)
    playnote('F4',q)
    playnote('F4',q)

    playnote('E4',w)
    playnote('E4',q)

    playnote('F4',q)
    playnote('E4',q)
    playnote('D4',q)

    playnote('C4',w)
    playnote('G4',q)

    playnote('A4',q)
    playnote('G4',e)
    playnote('G4',e)
    playnote('F4',e)
    playnote('F4',e)

    playnote('C5',q)
    playnote('C4',q)
    playnote('C4',e)
    playnote('C4',e)

    playnote('D4',q)
    playnote('G4',q)
    playnote('E4',q)

    playnote('F4',w)