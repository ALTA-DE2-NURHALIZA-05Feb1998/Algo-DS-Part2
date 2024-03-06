def count_item_and_sort(items):
    kemunculan_barang = {}
    for barang in items:
        if barang in kemunculan_barang:
            kemunculan_barang[barang] += 1
        else:
            kemunculan_barang[barang] = 1
    barang_urut = sorted(kemunculan_barang.items(), key=lambda x: (x[1], x[0]))
    result = " ".join([f"{barang}->{jumlah}" for barang, jumlah in barang_urut])
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"