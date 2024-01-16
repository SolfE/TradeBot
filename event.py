def chk_event_1(data):
    df = data
    if len(df) >= 2:
        if df["CCI"][1] < -100 and -100 <= df["CCI"][0] <= 100:
            if df["50EMA"][0] > df["100EMA"][0]:
                return True
        if df["CCI"][1] > 100 and -100 <= df["CCI"][0] <= 100:
            if df["50EMA"][0] < df["100EMA"][0]:
                return True
    return False
# def chk_event_2(data):
#     df = data
#     if df["CCI"][1] > 100 and -100 <= df["CCI"][0] <= 100:
#         if df["50EMA"][0] > df["100EMA"][0]:
#             return True
#     if df["CCI"][1] < -100 and -100 <= df["CCI"][0] <= 100:
#         if df["50EMA"][0] < df["100EMA"][0]:
#             return True
#     return False
