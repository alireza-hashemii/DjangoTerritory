from . import jalali
 

def persian_numbers_converter(my_str):
    nums = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e,p in nums.items():
        my_str = my_str.replace(e,p)
    return my_str

def jalali_converter(time):

    jmonth = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","ابان","اذر","دی","بهمن","اسفند"]

    time_to_str = f"{time.year}.{time.month}.{time.day}"
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index,month in enumerate(jmonth):
        if time_to_list[1] == index +1:
            time_to_list[1] = month
            break

    output =  "{} {}".format(
        time_to_list[0],
        time_to_list[1],
    )
    return persian_numbers_converter(output)