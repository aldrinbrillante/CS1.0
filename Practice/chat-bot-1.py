# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_mood_bot_response(user_response):

  #add some bot responses to this list
  bot_response_happy = []

  if user_response == "happy":
    #TODO: use choice to randomly return a response from the list
    ...
  else:
    return ...




print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while ...:
  user_response = input("How are you feeling today?: ")
  #TODO: what goes here
  bot_response = ...
  print(bot_response)



