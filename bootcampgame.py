def show_instruction():
    print("""\n
    Permainan Petualangan Berbasis Teks
    ===================================
    Perintah :
        pergi[arah]
        ambil[item]
    """)

def show_status(player):
    print("------------------------")
    print(f"kamu berada di {player ['location']}")
    print(f"inventaris: {player ['inventory']}")
    if "item" in rooms[player["location"]]:
        print(f"kamu melihat sebuah {rooms[player['location']]['item']}")
    print("------------------------")

def main():
    rooms = {
        'Hall':{
            'south':'kitchen',
            'east': 'dining room',
            'item':'key'
        },
        'kitchen':{
            'north':'Hall',
            'item':'monster'
        },
        'dining room':{
            'west':'Hall',
            'south':'garden',
            'item':'potion'
        },
        'garden':{
            'north':'dining room'
        }
    }

    player = {
        "location":"Hall",
        "inventory":[]
    }
    show_instruction()

    while True:
        show_status(player)

        move = input(">").lower().split()

        if move[0] == "go":
            direction=move[1]

            if direction in rooms[player["location"]]:
                player["location"] = rooms[player["location"]][direction]
            else:
                print("kamu tidak bisa pergi ke arah itu!")

        elif move[0] == "get":
            item = move[1]

            if "item" in rooms[player["location"]] and item == rooms[player["location"]]["item"]:
                player["inventory"].append(item)
                del rooms[player["location"]]["item"] 
                print(f"{item.capitalize()} diambil!")
            else:
                print(f"tidak bisa mengambil {item}!")

        elif move[0] == "quit":
            print("terima kkasih telah bermain!")
            break

        else:
            print("perintah tidak valid.")

        if 'item' in rooms[player["location"]]and rooms[player["location"]]['item'] == 'monster':
            print("seekor monster menangkapmu...........GAME OVER")
            break

        if player ['location'] == 'garden' and 'key' in player['inventory'] and 'potion' in player ['inventory']:
            print("YOU WIN")
            break

if __name__ == "__main__":
    main()