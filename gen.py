from random import randint

##Making lists
color_lst = ("pink", "red", "yellow", "green","blue","purple")
arcana_lst = ("conscience","bard","magician", "healer", "fighter","sea","field","stars","candle","tome","reverence","crown","spear","eye","hospice","plague","gambler","rat","wolf","raven","snake","dragon")

##Generate numbers
def num_color():
    return randint(0,5)
def num_card():
    return randint(0,len(arcana_lst)-1)

##Link numbers and dictionary
def return_card(n_color, n_card):
    if n_color == 7:
        color = "white"
    else:
        color = color_lst[n_color]
    card = arcana_lst[n_card]
    return color, card

##Main
def main():
    n_card_1=num_card()
    color_1, card_1 = return_card(7,n_card_1)
    print("Your first card is the", card_1)
    for i in range(0,3):
        n_card = num_card()
        n_color = num_color()
        color, card = return_card(n_color,n_card)
        if i!=2:
            print("Your next card is the",color, card)
        else:
            print("Your last card is the",color, card)
    return


main()
