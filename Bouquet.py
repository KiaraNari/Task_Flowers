class Flower:
    def __init__(self, sort, f_prise):
        self.sort = sort
        self.f_price = f_prise

class Accessory:
    def __init__(self, a_type, a_price):
        self.a_type = a_type
        self.a_price = a_price

class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower, f_count):
        for i in range(f_count):
            self.flowers.append(flower)

    def add_accessory(self, accessory, a_count):
        for i in range(a_count):
            self.accessories.append(accessory)

    def cost_bouquet(self):
        total = 0
        for flower in self.flowers:
            total = total + flower.f_price
        for accessory in self.accessories:
            total = total + accessory.a_price
        return total


def main():
    rose = Flower("Rose", 30)
    calla = Flower("Calla", 25)
    narcissus = Flower("Narcissus", 20)
    gerbera = Flower ("Gerbera", 25)
    ribbon = Accessory("Ribbon", 10)
    netting = Accessory("Netting", 15)
    wrapper = Accessory("Wrapper", 10)
    first_bouquet = Bouquet()
    first_bouquet.add_flower(rose, 5)
    first_bouquet.add_flower(calla, 4)
    first_bouquet.add_flower(gerbera, 5)
    first_bouquet.add_accessory(ribbon, 1)
    first_bouquet.add_accessory(netting, 1)
    print(first_bouquet.cost_bouquet())


    second_bouquet = Bouquet()
    print("What sort of flowers you want to add to the bouquet?"
          "\nPress 1 if roses"
          "\nPress 2 if callas"
          "\nPress 3 if narcissus"
          "\nPress 4 if gerberas")
    sort_of_flowers = int(input())
    if sort_of_flowers>=1 and sort_of_flowers<=4:
        print("How many flowers do you want?")
        count_of_flowers = int(input())
        dict_flowers = {
            1 : rose,
            2 : calla,
            3 : narcissus,
            4 : gerbera
        }

        print("What kind of accessories you want?"
              "\nPress 1 if ribbon"
              "\nPress 2 if netting"
              "\nPress 3 if wrapper"
              "\nPress 4 if none")
        type_of_accessories = int(input())

        if type_of_accessories != 4 :
            print("How many of accessories do you want?")
            count_of_accessories = int(input())
        else: count_of_accessories = 0

        dict_accessories = {
            1 : ribbon,
            2 : netting,
            3 : wrapper,
            4 : "None"
        }

        second_bouquet.add_flower(dict_flowers[sort_of_flowers], count_of_flowers)
        second_bouquet.add_accessory(dict_accessories[type_of_accessories], count_of_accessories)
        print (second_bouquet.cost_bouquet())
    else:
        print("We haven't the sort of flowers like this. Have a nice day!")

main()
