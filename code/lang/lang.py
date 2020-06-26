def lang(myLanguage):

    if myLanguage == 'en':
        assoc_1, assoc_2, continue_last = ['association_1.jpg','association_2.jpg','Continue_last.jpg']
        bonus_cant_already, lotery_free, lotery_bonus = ['bonus_cant-collected_already.jpg','lotery_free_2.jpg', 'lotery_free.jpg']
        bonus_you, video_present, secure_bonus, skip_buy_ticket = ['watch_bonus_you.jpg','video_present.jpg', 'secure_special_bonus.jpg', 'skip_buy_ticket.jpg']
        bonus_money, bonus_prestige, sudenly_error = ['image$.jpg', 'imagePP.jpg', 'sudenly_error.jpg']
    else:
        assoc_1, assoc_2, continue_last = [None]*3
        bonus_cant, bonus_already, lotery_free = [None]*3
        bonus_you, no_video, video_not_load, video_present, skip = [None]*5

    return [assoc_1, assoc_2, continue_last, bonus_cant_already, lotery_free, lotery_bonus, bonus_you, video_present, secure_bonus, skip_buy_ticket, bonus_money, bonus_prestige, sudenly_error]

if __name__ == "__main__":
    # usefull for debuging
    print(lang('en'))
