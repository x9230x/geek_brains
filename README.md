Я пытался сделать ещё другой вариант но что то пошло не по плану. (1 задание)
Я пытался сделать это вот так.
Но потом пересмотрел 1 урок и понял что можно решить иначе.

def convert_time(duration: int) -> str:
    seconds = duration % 60
    minutes = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400
    if days > 0 :
        print(hours + 'часов' + minutes + 'минут' + seconds + 'секунд')

    elif hours > 0:
       print(minutes + 'минут' + seconds + 'секунд')

    else:
        print(seconds + 'секунд')


    return result


duration = 120120
result = convert_time(duration)
print(result)
