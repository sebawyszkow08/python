import os
os.system("cls")


points = 0
strength = 10
inteligence = 10
endurance = 10



all_traits = ["weak","strong","brawler","smart","dumb","stupid","fit","unfit","fatty", "smoker","coward","teenage","bully"]
character_traits = []
print("pick traits : ", all_traits)


while True:
    choice = input()

    if all_traits.count(choice) == 1:

        

    
        if character_traits.count(choice) == 0 and choice == "strong":
            if character_traits.count("weak") == 0 and character_traits.count("brawler") == 0 and points > 2:
                points -= 2
                strength += 2
                character_traits.append(choice) 

        if character_traits.count(choice) == 0 and choice == "weak":
            if character_traits.count("strong") == 0 and character_traits.count("brawler") == 0:
                points += 5
                strength -= 4
                character_traits.append(choice) 

        if character_traits.count(choice) == 0 and choice == "brawler":
            if character_traits.count("weak") == 0 and character_traits.count("strong") == 0 and points > 8:
                points -= 8
                strength += 5
                character_traits.append(choice)



        if character_traits.count(choice) == 0 and choice == "smart":
            if character_traits.count("dumb") == 0 and character_traits.count("stupid") == 0 and points > 2:
                points -= 2
                inteligence += 2
                character_traits.append(choice) 

        if character_traits.count(choice) == 0 and choice == "dumb":
            if character_traits.count("smart") == 0 and character_traits.count("stupid") == 0:
                points += 3
                inteligence -= 3
                character_traits.append(choice)

        if character_traits.count(choice) == 0 and choice == "stupid":
            if character_traits.count("smart") == 0 and character_traits.count("dumb") == 0:
                points += 6
                inteligence -= 6
                character_traits.append(choice)



        if character_traits.count(choice) == 0 and choice == "fit":
            if character_traits.count("unfit") == 0 and character_traits.count("fatty") == 0 and points > 5:
                points -= 5
                fitness += 4
                character_traits.append(choice)

        if character_traits.count(choice) == 0 and choice == "unfit":
            if character_traits.count("fit") == 0 and character_traits.count("fatty") == 0:
                points += 2
                fitness -= 3
                character_traits.append(choice)

        if character_traits.count(choice) == 0 and choice == "fatty":
            if character_traits.count("unfit") == 0 and character_traits.count("fit") == 0:
                points += 8
                fitness -= 6
                character_traits.append(choice)


        if character_traits.count(choice) == 0 and choice == "smoker":
            
            points += 2
            endurance -= 1
            character_traits.append(choice)

        if character_traits.count(choice) == 0 and choice == "coward":
            
            points += 3
            
            character_traits.append(choice)

        if character_traits.count(choice) == 0 and choice == "teenage":
            
            points += 6
            endurance -= 1
            strength -= 2
            inteligence -= 2
            
            character_traits.append(choice)
            
        if character_traits.count(choice) == 0 and choice == "bully":
            
            points -= 4
            endurance += 1
            strength += 3
            inteligence -= 3
            
            character_traits.append(choice)
            
        

        



    elif character_traits.count(choice) == 0 and choice == "show":
        print(character_traits, " pionts left: ", points)

    elif character_traits.count(choice) == 0 and choice == "reset":
        character_traits.clear()
        points = 0
        strength = 10
        inteligence = 10
        fitness = 10

    elif character_traits.count(choice) == 0 and choice == "end":
        break

    else:
        print("wrong command")


print("chosen character traits: ",character_traits)
print("stats: ", strength, inteligence , fitness )
print("points : ", points)
input()