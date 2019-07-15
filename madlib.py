# prompt user with series of inputs for Mad Lib fill ins - example, a singular noun, an adjective, etc.
# place that data in pre made story template
print("Lets Mad Lib!!!")

adjetive1 = input("Give me an adjetive   >")
adjetive2 = input("Another adjetive please  >")
adjetive3 = input("Another adjetive  >")
plural_noun1 = input("Give me a plural noun")
verb1 = input("Now a verb  >")
plural_noun_animal1 = input("Now a plural noun or animal  >")
plural_noun_animal2 = input("Another plural noun or animal  >")
verb2 = input("A verb  >")
noun_food1 = input("Now give me a noun or food  >")
noun_food2 = input("Another noun or food  >")
verb3 = input("A verb  >")
plural_noun2 = input("A plural noun  >")
adjetive4 = input("Yet again, another adjetive  >")
noun_animal1 = input("Now a noun or animal  >")
noun_food3 = input("Give me another noun or food  >")
noun_food4 = input("A noun or food  >")

print("The rainforest is a {} and {} place with a variety of {} {} who live there. Some animals {} high in the trees, like {} and {}. These animals {} foods like {} and {}. Other animals {} on the forest floor, like {} and the {} {}, eating {} and {} to survive.".format(adjetive1, adjetive2, adjetive3, plural_noun1, verb1, plural_noun_animal1, plural_noun_animal2, verb2, noun_food1, noun_food2,verb3, plural_noun2, adjetive4, noun_animal1, noun_food3, noun_food4))