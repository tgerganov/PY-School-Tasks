#Q 6
#Q 6a
data = [1, 2, 3, 4, 5]
addTen = list(map(lambda y: y + 10, data))
print(addTen) #[11, 12, 13, 14, 15]

#Q 6b
naturalNumbers = [0,1,2,3,4,5,6,7,8,9]
printEvenNumbers = list(filter(lambda y: y%2==0, naturalNumbers))
print(printEvenNumbers) #[0, 2, 4, 6, 8]

#Q 7
#Q 7a


#Q 7b
class Singer:
    def sing(self):
        print('Singing')

class SongWriter:
    def compose(self):
        print('Composing')

class SingerSongwriter(Singer, SongWriter):
    def strum(self):
        print('Struming')
    def actSensitive(self):
        print('Acting sensitive')

ssw = SingerSongwriter()
ssw.sing() #Singing
ssw.compose() #Composing
ssw.strum() #Struming
ssw.actSensitive() #Acting sensitive