def convert_time(duration: int) -> str:
    seconds = duration % 60
    minutes = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400
    if days > 0 :
        result = f'{days} дн {hours} час {minutes} мин {seconds} сек'
    elif hours > 0:
       result = f'{hours} час {minutes} мин {seconds} сек'

    elif minutes > 0:
       result = f'{minutes} мин {seconds} сек'
    else:
       result = f'{seconds} сек'

    return result


duration = 120120
result = convert_time(duration)
print(result)