#8-7专辑

def make_album(star, song, number=''):
    album = {star: song}
    if number:
        album['数量'] = number
    
    return album


musician = make_album('周杰伦', '不想你哭')
print(musician)

musician = make_album('张国荣', '我')
print(musician)

musician = make_album('刘德华', '17岁', number = 20)
print(musician)
