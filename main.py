import time
import random
import os

# store possible options
yes = ["y", "Y", "yes", "Yes"]
no = ["no", "No", "n", "N"]
a = ["a", "A"]
b = ["b", "B"]
c = ["c", "C"]
d = ["d", "D"]


# function that takes in an option (one of the lists above), the next branch, and an optional extra message
# for some reason you have to put choice in there - idk why
def branch(choice, option, next_branch, message=""):
    if choice in option:
        os.system("clear")
        print(message)
        next_branch()

# function that runs if the choice does not match any of the options (else statement)
def choice_not_option(current_branch):
    print("\nChoose one of the options")
    current_branch()


# play again function
def play_again():
    print("\nDo you want to play again?")
    choice = input(">>> ")
    if choice in no:
        print("\nGame Over")
        exit()
    branch(choice, yes, intro)
    choice_not_option(play_again)


# actual game
def intro():
    print(
        "You stand in front of the counter at the Chocky Burrito Restaurant, determined to make the best burrito possible.\nFirst, you have to choose a wrap: "
    )
    time.sleep(1)
    print("A: plain\nB: whole wheat\nC: dollar bills")
    choice = input(">>> ")
    branch(choice, a, plain)
    branch(choice, b, farm)
    branch(choice, c, dollar_bill)
    choice_not_option(intro)


# plain path
def plain():
    print("Nice choice! Now, you have to choose a meat.")
    time.sleep(1)
    print("A: chicken\nB: beef\nC: pork")
    choice = input(">>> ")
    if choice in a or choice in b or choice in c:
        cheese()
    choice_not_option(plain)


def cheese():
    print("\nDo you want cheese?")
    choice = input(">>> ")
    if choice in yes or choice in no:
        spicy()
    choice_not_option(cheese)


def spicy():
    print(
        "\nDo you want hot sauce? (Note: this will make the burrito S P I C Y)"
    )
    choice = input(">>> ")
    if choice in yes or choice in no:
        take_out()
    choice_not_option(spicy)


def take_out():
    print(
        "\nYour amazing burrito has been made. Do you want to eat it here or take it to go?"
    )
    time.sleep(1)
    print("A: eat it here\nB: take it to go")
    choice = input(">>> ")
    branch(
        choice,
        a,
        intro,
        "\nAs you take the burrito to an empty booth, you slip on a puddle of soda and drop your burrito. Now you've got to make another one.\n",
    )
    branch(
        choice,
        b,
        play_again,
        "\nAs you take the burrito outside, you get hit by a kid on their bike and drop your burrito. No burrito for you, I guess.",
    )
    choice_not_option(take_out)


# farm path
def farm():
    print(
        "The cashier tells you that they have run out of whole wheat. Enraged, you demand to know who their supplier is. She directs you to a farm five miles away."
    )
    time.sleep(0.75)
    print(
        "When you finally get to the farm, you poke around for a while until you meet someone (you assume the farmer). How do you interact with the farmer?"
    )
    time.sleep(1)
    print(
        "A: ask for a job\nB: ask for whole wheat\nC: steal a tractor under the cover of night"
    )
    choice = input(">>> ")
    branch(choice, a, job)
    branch(
        choice,
        b,
        play_again,
        "\nThe farmer actually has a surplus of whole wheat! She informs you that she has just not gotten around to delivering it. With a bag of (very heavy) whole wheat in your arms, you set torward the burrito restaurant and hope you get there before it closes.",
    )
    branch(choice, c, tractor)
    choice_not_option(farm)


def job():
    print("The farmer declined your help.")
    print("Do you:")
    print("A: ask again\nB: steal a tractor out of spite")
    choice = input(">>> ")
    branch(choice, a, job)
    branch(choice, b, tractor)


def tractor():
    print(
        "Thankfully, there isn't much sunlight left so you don't have to wait long. The tractor sits unguarded inside a barn and the keys are already in the ignition. You don't really know how to drive a tractor, but it can't be that dissimilar to a car."
    )
    time.sleep(1)
    print(
        "The sun has set and you sneak into the barn under the cover of darkness. After clambering up on the driver's seat, do you:"
    )
    time.sleep(1)
    print(
        "A: drive it forward\nB: drive it backward\nC: try to sell it\nD: change of plans: destroy the barn"
    )
    choice = input(">>> ")
    branch(choice, a, forward)
    branch(
        choice,
        b,
        play_again,
        "\nYou put the tractor in reverse and floor the gas pedal. You crash into the hay bales behind you at top speed, hitting various farm tools along the way.\nThe barn explodes, with you in it.",
    )
    branch(
        choice,
        c,
        jeff_bezos,
        "\nAfter sneaking the tractor out of the farm unnoticed, you post an ad online. Almost immediately, you get an offer for a ridiculous amount of money, and you set off to meet your mysterious buyer.\n",
    )
    branch(
        choice,
        d,
        jail,
        "\nAs you search the barn for things that can help you destroy it, you see the stash of whole wheat! Now that you've found what you're looking for, you can simply leave peacefully. \nAlas, all the time you spent looking has alerted the farmer to your presence and the police have now arrived.\nThe last thing you see before you get shoved into backseat of the police car is a half open bag of whole wheat.",
    )
    choice_not_option(tractor)


def forward():
    print(
        "Tractors really aren't that dissimilar to a car, and you sneak off the farm. Now you're out on the road, celebrating your victory, but you feel kind of lonely.\nDo you tweet about your accomplishment?"
    )
    choice = input(">>> ")
    branch(
        choice,
        yes,
        jail,
        "To your surprise, the tweet goes viral and you become an internet sensation overnight. Unfortunately, this means that the farmer has traced her missing tractor back to you and there are now police cars chasing your tractor.\nNo matter how hard you press on the gas pedal, a tractor is simply no match for a police cruiser and before you know it, you have been handcuffed and thrown into the backseat.",
    )
    branch(
        choice,
        no,
        play_again,
        "\nYou may have avoided jailtime, but you now live your life as a criminal.\n\nWhich would be completely fine, but now that their supplier doesn't have transportation, Chocky Burrito Restaurant has to take whole wheat wraps off their menu.",
    )
    choice_not_option(forward)


# jail escapades
def jail():
    time.sleep(1)
    print(
        "You don't have much to say in your defense, and your trial quickly concludes in a guilty verdict. You must now face your new life in jail."
    )
    time.sleep(2)
    print(
        "Some time into your sentence (you don't even know what day it is anymore), an opportunity arises. \nAs he was locking your door, the guard that was typically posted in your hallway suddenly left in a hurry and left the door ajar.\nDo you use this chance to escape?"
    )
    choice = input(">>> ")
    branch(choice, yes, escape)
    branch(
        choice,
        no,
        play_again,
        "\nYou turn your back on the door and go to sleep. You get released early a couple months later for good behavior.\nThe first thing you want to do with your new found freedom is to get a burrito.",
    )
    choice_not_option(jail)


def escape():
    print(
        "As quietly as you can, you open the door and go down the hallway. You reach an intersection. \nDo you:"
    )
    time.sleep(1)
    print("A: go left\nB: go forward")
    choice = input(">>> ")
    branch(
        choice,
        a,
        left,
        "\nAfter tiptoeing down the left hallway, you reach a door that goes off to the side.",
    )
    branch(
        choice,
        b,
        play_again,
        "\nYou haven't even taken five steps when you hear a guards running down the hallway. You are caught red-handed and return to your cell to serve out the rest of your sentence.\n\nThey don't serve burritos in jail.",
    )
    choice_not_option(escape)


def left():
    print("Do you:")
    time.sleep(1)
    print("A: open the door\nB: keep going down the hallway")
    choice = input(">>> ")
    branch(choice, a, door)
    branch(choice, b, forward_jail)
    choice_not_option(left)


def door():
    print(
        "Thankfully, the door doesn't creak when you open it. Unthankfully, there's a guard sitting right behind it. He seems asleep, but if you try to sneak past, he'll probably wake up. Do you:"
    )
    time.sleep(1)
    print("A: punch the guard\nB: go back")
    choice = input(">>> ")
    branch(
        choice,
        a,
        play_again,
        "\nYou get one measly punch in before the guard wakes up. Before you know it, you're knocked out on the floor and you know you won't be leaving this jail for a rather long time.",
    )
    branch(
        choice,
        b,
        left,
        "\nYou step back out into the hallway and cautiously close the door.",
    )
    choice_not_option(door)


def forward_jail():
    print(
        "You reach the end of the empty hallway and turn to find a room with the keys to all fo the cells in the jail. Do you go back and release your cellmates?"
    )
    choice = input(">>> ")
    branch(
        choice,
        yes,
        play_again,
        "Your cellmates and you all make your way out of the jail. Just as you're about to make it out, someone trips the alarm. Someone shoves you backward and by the time you get back to your feet, the guides have arrived. As they restrain you and drag you back into the jail, you see the rest of the group disappear into the woods.",
    )
    branch(choice, no, ditch_cellmates)
    choice_not_option(forward_jail)


def ditch_cellmates():
    print(
        "You ignore the room and continue down the hallway. You must be somewhere close to the exit by now. Up ahead, you can see an intersection. Do you:"
    )
    time.sleep(1)
    print("A: go left\nB: go right")
    choice = input(">>> ")
    rand = random.randInt(0, 1)
    if rand == 0:
        choice = "a"
    else:
        choice = "b"
    branch(
        choice,
        a,
        play_again,
        "This hallway looks like all the others, but when you get to the end, you can see a door. Hoping for the best, you open it and it leads outside! You are free!\nAll this escaping has left you rather hungry. You could really go for a burrito right now.",
    )
    branch(
        choice,
        b,
        play_again,
        "This hallway looks like all the others, but but as you walk down you hear footsteps coming from in front. Hurriedly, you try to go back the way you came, but there are guards coming from there as well. Trapped, you have no choice but to be led back to your cell.",
    )
    choice_not_option(ditch_cellmates)


# dollar bill path
def dollar_bill():
    print(
        'The cashier\'s facial expression barely changes, but you notice a man sitting in the corner perk up and begin regarding you intensely. As your burrito is being made, he strides over and asks "Are you rich?"(You aren\'t)'
    )
    choice = input(">>> ")
    branch(choice, yes, ask_about_job)
    branch(
        choice,
        no,
        play_again,
        "The man nods curtly and leaves the restaurant.\nYour burrito never arrives.",
    )
    choice_not_option(dollar_bill)


def ask_about_job():
    print(
        "The man nods. Is he impressed? You can't tell.\n\"What's your job?\"\n(You're technically in between jobs at the moment, but lying can't hurt, right?)\nWhat do you tell him?"
    )
    print("A: farmer\nB: lawyer\nC: CEO")
    time.sleep(1)
    choice = input(">>> ")
    branch(
        choice,
        a,
        play_again,
        "There's a beat of silence.\nThen the man throws his head back and laughs. When he's finally finished, he abruptly turns around and leaves, leaving you mystified.\nWhen you finally get your burrito, you find that it's been paid for, though the wrap is whole wheat.",
    )
    branch(
        choice,
        b,
        play_again,
        "The man suddenly backs away, muttering something about being late for an appointment. He practically flees out the door, leaving you dumbfounded. Did you say something wrong?",
    )
    branch(
        choice,
        c,
        jeff_bezos,
        "\nThe man nods and then beckons you to follow him. Confused, and with nothing better to do, you follow him.",
    )
    choice_not_option(ask_about_job)


def jeff_bezos():
    print('"I am Jeff Bezos."\n')
    time.sleep(1)
    print("You stare at him blankly.\n")
    print("\"And I want to offer you a job.\"")
    time.sleep(1)
    print(
        "You have a rather interesting decision to make.\nDo you take the job?"
    )
    choice = input(">>> ")
    branch(choice, yes, payday)
    branch(
        choice,
        no,
        play_again,
        "Jeff Bezos (is it even him?) doesn't look too affronted, just nods and walks away.\nYou can't help but feel you just missed out on something big.",
    )


def payday():
    print("A while later, you have a rather cushy job working at Amazon...")
    time.sleep(1)
    print("Stealing cybertrucks.")
    time.sleep(1)
    print(
        "You're actually pretty good at it and it's much more enjoyable than a boring desk job. There's just one thing that's been bugging you for a while. \nPayday is coming up soon and you can't help but be reminded that you don't have Amazon Prime."
    )
    time.sleep(1)
    print(
        "Now as one of Jeff Bezos' most important employees, (There could be a whole tangent about the Bezos/Musk rivalry, but suffice to say your work in making Elon Musk's life harder is valued extremely highly.) you feel that you should at least be entitled to free Amazon Prime."
    )
    time.sleep(1)
    print("You've asked Bezos.\nHe said no.\nSo there's only one thing to do:")
    time.sleep(1)
    print("Do you fight Jeff Bezos for free Amazon Prime?")
    choice = input(">>> ")
    branch(
        choice,
        yes,
        play_again,
        "\nThe fight isn't even close.\nJeff doesn't even see you coming. In fact, the defeat is so humiliating that he had to retire out of shame and you are now the owner of Amazon. \n\nSo of course the first thing you do is to buy the Chocky Burrito Restaurant. You now have unlimited burritos at your disposal.",
    )
    branch(choice, no, elon_musk)
    choice_not_option(payday)


def elon_musk():
    print(
        "Of course, with no Amazon Prime membership, you don't feel like you're truly being valued in the workplace. So you quit."
    )
    print("Life is rather boring until one day you get a job offer.")
    time.sleep(1)
    print("You might have to think this one through for a second.")
    time.sleep(2)
    print("Do you accept a job to steal Amazon Prime vans for Elon Musk?")
    choice = input(">>> ")
    branch(choice, yes, cybertruck)
    branch(choice, no, refuse_elon)
    choice_not_option(elon_musk)


def cybertruck():
    print(
        "Stealing Amazon Prime vans is just about as easy as stealing cybertrucks and you flourish at your new job. One day, Elon Musk approaches you and says that as a reward for your work, he would like to gift you a cybertruck."
    )
    print("Do you:")
    time.sleep(1)
    print(
        "A: take it to use on the road\nB: use your new ride to go to the Chocky Burrito Restaurant\nC: sell it"
    )
    choice = input(">>> ")
    branch(
        choice,
        a,
        play_again,
        "\nYour new wheels serve you pretty well on the road, though you have to be wary anything potentially hitting your windows. \nLike burritos.",
    )
    branch(
        choice,
        b,
        play_again,
        "\nIt's been a really long time since you've gone to Chocky Burrito Restaurant and you're anxious to finally make your perfect burrito. \nAlas when you get there, you see that the sign has been changed to Chocky Ice. \nYou drive home burrito-less.",
    )
    branch(choice, c, sellers)
    choice_not_option(cybertruck)


def sellers():
    print(
        "You put up an ad for the cybertruck, not really expecting anything. But when you check the listing the day after, you now have three rather interesting choices."
    )
    print("Do you sell your cybertruck to:")
    time.sleep(1)
    print("A: a Republican\nB: Jeff Bezos' ex-wife\nC: a shady charity")
    choice = input(">>> ")
    branch(
        choice,
        a,
        play_again,
        '\n"Aw man I\'m gonna put so many stickers on this thing," the Republican says.\nAs he drives off, you realize that you now have enough money to buy lots of burritos.',
    )
    branch(
        choice,
        b,
        play_again,
        '\n"This isn\'t to get back at Jeff" is the first thing she says.\n"Here\'s the money" is the second (and last) thing she says.\nAs you count the bills in the thick wad of cash, you realize that you can now buy as many burritos as you could ever want.',
    )
    branch(
        choice,
        c,
        play_again,
        '\nThe man that shows up thanks you profusely and promises that the cybertruck is going to be used "for education." \nYou don\'t really mind because you now have enough money to buy all the burritos your heart desires.',
    )
    choice_not_option(sellers)


def refuse_elon():
    print(
        'Elon Musk looks rather surprised that you wouldn\'t want his cybertruck and when he asks why, you make the mistake of telling him it looks "ugly as hell."'
    )
    time.sleep(1)
    print("You now no longer work for Elon Musk.")
    print("Do you:")
    time.sleep(1)
    print(
        "A: try to get your Amazon job back\nB: continuing stealing Amazon Prime vans on your own\nC: buy a burrito to drown your sorrows"
    )
    choice = input(">>> ")
    branch(
        choice,
        a,
        play_again,
        "\nJeff Bezos laughs in your face.\nYou die unemployed.",
    )
    branch(
        choice,
        b,
        play_again,
        "\nAs the world's leading expert on stealing vehicles from billionaires, you start your own illegal billionaire vehicle stealing business. Soon enough, you're raking in cash and you hire a personal chef to make you all the burritos you want.",
    )
    branch(
        choice,
        c,
        play_again,
        "\nIt's not a bad burrito, but it's not good enough to solve your life problems. \nOh well, at least you're not in jail.",
    )


print(
    "Welcome to the Burrito Text Adventure! Type your answer when presented with the prompt. Answers can be a, b, c, d or yes/no depending on the question. Try to stay out of jail!\n"
)
time.sleep(2)
intro()