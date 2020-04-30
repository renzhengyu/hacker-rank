def howManyGames(p, d, m, s):
    game = 0
    price_to_pay = p
    while price_to_pay < s:
        game += 1
        s -= price_to_pay
        price_to_pay -= d
        if price_to_pay <= m:
            price_to_pay = m
            same = int(s / m)
            game += same
            s -= same * price_to_pay
    return game
