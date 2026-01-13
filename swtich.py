nome = "joao"
rank = ""
xp = 4658

match xp:
    case xp if xp < 1000:
        rank = "Ferro"
    case xp if xp < 2000:
        rank = "Bronze"
    case xp if xp < 5000:
        rank = "Prata"
    case xp if xp < 7000:
        rank = "Ouro"
    case xp if xp < 8000:
        rank = "Platina"
    case xp if xp < 9000:
        rank = "Diamante"
    case xp if xp < 10000:
        rank = "Lendário"
    case _:
        rank = "Imortal"

print(rank)
