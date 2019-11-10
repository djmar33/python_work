#8-8专辑,增加while循环，读取用户数据，并且提供退出循环条件；

def make_album(star, song, number=''):
    album = {star: song}
    if number:
        album[number] = number
    
    return album


while True:
    print("请输入您喜欢的专辑：\n")
    print("随时可以输入'q'退出")

    star_i = input("歌手：")
    if star_i == 'q':
        break
    song_i = input("歌曲名：")
    if song_i == 'q':
        break

    musician = make_album(star_i, song_i)
    print(musician)
