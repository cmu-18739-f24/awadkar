#!/usr/bin/env python3
import random
import sys

CORRECT_INPUT = ''
motivational_quotes = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Strive not to be a success, but rather to be of value.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "The way to get started is to quit talking and begin doing.",
    "Your time is limited, don't waste it living someone else's life.",
    "If you want to lift yourself up, lift up someone else.",
    "Whether you think you can or you think you can't, you're right.",
    "I attribute my success to this: I never gave or took any excuse.",
    "The mind is everything. What you think you become.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "An unexamined life is not worth living.",
    "Eighty percent of success is showing up.",
    "Your time is limited, so don't waste it living someone else's life.",
    "Winning isn't everything, but wanting to win is.",
    "I am not a product of my circumstances. I am a product of my decisions.",
    "You can never cross the ocean until you have the courage to lose sight of the shore.",
    "Either you run the day, or the day runs you.",
    "The two most important days in your life are the day you are born and the day you find out why.",
    "Whatever you can do, or dream you can, begin it. Boldness has genius, power and magic in it.",
    "Life shrinks or expands in proportion to one's courage.",
    "There is only one way to avoid criticism: do nothing, say nothing, and be nothing.",
    "Ask and it will be given to you; search, and you will find; knock and the door will be opened for you.",
    "The only person you are destined to become is the person you decide to be.",
    "Go confidently in the direction of your dreams. Live the life you have imagined.",
    "When I let go of what I am, I become what I might be.",
    "You can't fall if you don't climb. But there's no joy in living your whole life on the ground.",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
    "If you want to lift yourself up, lift up someone else.",
    "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Remember that not getting what you want is sometimes a wonderful stroke of luck.",
    "Everything has beauty, but not everyone can see.",
    "How wonderful it is that nobody need wait a single moment before starting to improve the world.",
    "When I was 5 years old, my mother always told me that happiness was the key to life. When I went to school, they asked me what I wanted to be when I grew up. I wrote down 'happy'. They told me I didn't understand the assignment, and I told them they didn't understand life.",
    "The only way to do great work is to love what you do.",
    "If you can dream it, you can achieve it.",
    "Few things can help an individual more than to place responsibility on him, and to let him know that you trust him.",
    "Remember no one can make you feel inferior without your consent.",
    "Life is what we make it, always has been, always will be.",
    "The question isn't who is going to let me; it's who is going to stop me.",
    "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",
    "It's not the years in your life that count. It's the life in your years.",
    "Change your thoughts and you change your world.",
    "Either write something worth reading or do something worth writing.",
    "Nothing is impossible, the word itself says, 'I'm possible!'",
    "The only way to do great work is to love what you do.",
    "If you can dream it, you can achieve it.",
    "You become what you believe.",
    "I would rather die of passion than of boredom.",
    "A truly rich man is one whose children run into his arms when his hands are empty."
]

def read_flag():
    try:
        with open('flag.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return 'Flag file not found.'
    
def read_key():
    try:
        with open('key', 'r') as file:
            CORRECT_INPUT =  file.read()
            return CORRECT_INPUT
    except FileNotFoundError:
        return 'Key file not found.'

def check_input(user_input, CORRECT_INPUT):
    if user_input == CORRECT_INPUT:
        flag = read_flag()
        print(flag)
        return ''
    else:
        return 'Incorrect pharse! Heres a motivational quote :'

if __name__ == "__main__":
    
    CORRECT_INPUT = read_key()
    sys.stdout.flush()
    print("Welcome to a simple game that will teach you to read between the lines")
    print("Checkout the given story. It might have what it takes to unlock this vault")
    counter= random.randint(0, 55)
    
    user_input = input("Enter the secret phrase: ")
    result = check_input(user_input, CORRECT_INPUT)
    print(result)
    if result == 'Incorrect pharse! Heres a motivational quote :':
        print(motivational_quotes[counter])
    else:
        print("Correct phrase. Welcome.. to the Vault")
    sys.stdout.flush()

            

        