import random

def destroy(all_tiles,tile):
    if all_tiles[tile] >0:
        all_tiles[tile] -= 1
 




all_tiles = {}
size = 16
#0 - nic, 1- trawa, 2 - sciana

for tile_nr in range(1,size*size+1):
    all_tiles[tile_nr] = random.randint(0,2)


#for a in all_tiles.items():
#    print(a)

#WYSWIETLANIE PLANSZY


tile_keys = [key for key in all_tiles]

while True:   
    for tile in tile_keys:

        match all_tiles[tile]:
            case 0:
                tile_sprite = "   "
            case 1:
                tile_sprite = ",,,"
            case 2:
                tile_sprite = "|||"


        print(tile_sprite, end="")
        if tile % size == 0:
            print()

    aa = input()
    destroy(all_tiles,aa)






