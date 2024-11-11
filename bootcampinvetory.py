inventory = []

def add_item(name,quantity,price):
    """menambahkan item ke inventaris"""
    inventory.append({"name":name , "quantity":quantity , "price":price})
    print(f"{name} ditambahkan ke inventaris.")

def remove_item(name):
    """mengapus item dari inventaris."""
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print(f"{name} dihapus dari inventaris.")
            return
        print(f"{name} tidak ditemukan di inventaris.")

def display_inventory():
    """"menampilkan inventory"""
    print("/nInventaris:")
    for item in inventory:
        print(f"nama: {item['name']}, jumlah: {item['quantity']}, harga: {item['price']:.2f}")

def main():
    add_item("laptop",10,999.99)
    add_item("mouse",20,19.99)
    add_item("keyboard",15,49.99)
    display_inventory()
    remove_item("mouse")
    display_inventory()

if __name__=="__main__":
    main()