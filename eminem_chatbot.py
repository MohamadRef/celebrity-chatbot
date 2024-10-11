# Eminem Chatbot
# Author: Mohamad Refaai

print("Yo, it's Slim Shady! Welcome to the Eminem Chatbot.")
print("I'll be asking you a few questions.")

fav_song = input("What's your favorite Eminem song? ")

if "love" in fav_song.lower() or "lose yourself" in fav_song.lower():
    print("Amazing choice! Those tracks are classy.")
else:
    print("Ouuu, I like those ones too. Eminem's got a lot of dope songs!")

fav_album = input("What's your favorite Eminem album? ")

if "marshall mathers" in fav_album.lower() or "the slim shady" in fav_album.lower():
    print("Daymm!!! Eminem's one of the best albums ever made!")
else:
    print("Oh great! Eminem has made some lit albums.")

time_of_listening = int(input("How many minutes do you spend listening to Eminem daily? "))

if time_of_listening > 60:
    print("Ouuuuu, my guyyyy!")
else:
    print("That's not bad still.")

print("Thanks for chatting with Slim Shady!")
