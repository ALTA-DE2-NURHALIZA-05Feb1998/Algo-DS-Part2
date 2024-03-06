def bisa_dimainkan(cards, deck):
    for kartu in cards:
        if kartu[0] in deck or kartu[1] in deck:
            return True
    return False

def cetak_kartu_dimainkan(cards, deck):
    for kartu in cards:
        if kartu[0] in deck or kartu[1] in deck:
            return kartu
    return []

def playing_domino(cards, deck):
    if bisa_dimainkan(cards, deck):
        hasil = cetak_kartu_dimainkan(cards, deck)
    else:
        hasil = []
    return hasil
if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []