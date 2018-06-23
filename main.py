from termcolor import cprint as cp # allows for colored text
from termcolor import colored as cd # allows for colored input
from random import choice # to create customized responses
from time import sleep as wait # to enable wait times
from hashlib import sha512 # to allow for authentic passwords
from googletrans import Translator # to change bot language
import socket # to gather ip's
from pyfiglet import figlet_format as ff # for ascii text

import database.db as db # to transfer data to the server
from database.query import * # to write data to server

import time # to allow time to be recorded on database

# There are easter eggs hidden in this code! If you can find them, take a screenshot of you using them and send them to my email listed below! If I feel that you HAVE found them, I will add you to the credits!

# Hint: the easter eggs have to do with the symbol --> ! <--

# Have fun and keep coding!

# email: lukas.woodruff20@d155.org


conversations = db.ConnectedDatabase("pybot","conversations")

suggestions = db.ConnectedDatabase("pybot","suggestions")

names = db.ConnectedDatabase("pybot","names")

superowner = "kingofcode"

owner = "pyelias"

superowneranswer = [
superowner + " is the best!",
"I like " + superowner + "!",
"Everyone likes " + superowner + "!",
superowner + " is the coolest!",
"You gotta love " + superowner + "!",
superowner + " is da bomb!",
superowner + " is a great coder! Just like " + owner + "!",
]
owneranswer = [
owner + " is a good person!",
owner + " is an awesome friend!",
"that guy " + owner + " is a riot!",
"Don't mess with " + owner + ", or you'll have to go through me!",
owner + " is the best!",
owner + " is a great coder! Just like " + superowner + "!",
owner + " is a cool kid!",
]

ATTRS = [
  "bold",
  "dark",
  "underline",
  "blink",
  "concealed",
]

COLORS = [
  "grey",
  "red",
  "green",
  "yellow",
  "blue",
  "magenta",
  "cyan",
  "white",
]

COMMANDS = [
"!suggest",
"!leave"
"!commands",
"!changelog",
"!grab-ip",
"!secure",
"!exitsecure",
"!change-lang",
"!session",
"!new-session",
"!new-name",
]

prizeunbox = [
"congrats! you're a winner!" ,
"good job! you won!",
"and we have a winner!",
"i'm sorry, today's not your day!",
"not today! try again another time!",
"you almost did it!",
"guess what? you won!",
"i just want you to know that you won!",
"hurrah! you my friend, have won!",
"i don't know about you, but i think we got a winner!",
"it didn't happen as planned, sorry!",
"you can do better next time!",
"almost!",
"awww, try again later!",
"you missed it by this much!",
"you hit the jackpot!",
"dig into some of that gold!",
"yeah man! great job!",
"woo-hoo! you did it!",
"nice going, dude! do it again!",
"holy cow, that's a lot of bank!",
"100% WOW FACTOR",
"boi! how'd you do that!",
"hella cool, man!",
"it's hard to do, i know! try some other time!",
"it takes practice! try next time!",
"it takes time! maybe next time will be the time!",
"it didn't work, sorry!",
"that was awful! sorry, dude!",
"you'll get it next time!",
]
stupidanswer = [
"what did you say",
"i don't speak english, oh wait i do",
"do you eat grass",
"pop music is what i like most about the country genre",
"selena gomez is a cool dude",
"i really don't understand why the bears lose so much",
"aren't bears the coolest marsupials ever",
"if i had to pick a favorite color, i'd pick milk",
"aren't you going to tell me why you're here",
"let's talk about why perl sucks... it just does",
"the best thing about the 23rd century is justin timberlake",
"this is going lavishly, isn't it",
"gold nuggets are the best type of food to eat",
"democracy, am i right",
"you're a cool bot",
"i LOVE popcorn, don't you",
"this is going smoothly right",
"lets talk about that last avengers movie",
"repl.it is awesome!",
"imma go now... JK!",
"bruh... it's so cold! kidding!",
"are you stupid, or am i"
]
fakeanswer = [
"you're not real"  ,
"come back to life and maybe i'll talk",
"If you're not gonna be real, i ain't either",
"no way alien",
"maybe next time stranger",
"i don't think so unknown person",
"you're not very lifelike",
"you really think i'm gonna talk to you",
"not today e.t.",
"you better walk away now shadowman",
"if you really think i'm gonna talk, you're crazy",
"it ain't gonna work mongrel",
"who do you think you are",
"get outta here",
"i gotta shotgun man, scoot it",
"move along buddy boy",
"scat you freaking bat",
"traipse in someone else's territory",
"try again tomorrow",
"it'd be nice if you were real with me here",
]
phrase1 = [
"dimwitted ",
"brainless ",
"smelly ",
"yellow-bellied ",
"grubby ",
"maggoty ",
"sappy ",
"dopey ",
"warty ",
"forgetful ",
"immature ",
"friendless ",
"dumb ",
"funky ",
"shotty ",
"illiterate ",
]
phrase2 = [
"bellerina-skeeving ",
"peasant-loving ",
"dunce-wearing ",
"book-reading ",
"mother-loving ",
"ale-drinking ",
"grub-eating ",
"reptile-looking ",
"ribbet-rabbeting ",
"skunk-scented ",
"special-needs ",
"baboon-butted ",
"subway-living ",
]
phrase3 = [
"monster",
"jester",
"bedswerver",
"skeever",
"loser",
"junebug",
"marshmallow head",
"lubberwort",
"frog",
"whiffle-whaffle",
"tinman",
"fretter",
"feifer-fiefer",
"morsel",
]
uselessstuff = [
"do you like chicken",
"you look like my mother",
"you smell like burning shoes",
"do you have a brain",
"do you eat",
"are you going to answer me",
]
uselessanswers = [
"you're a dumbo",
"you wish",
"never",
"i do, do i",
"i'm gonna call the popo on you",
"i'm initiating a witch hunt on you",
]
nosay = [
  "",
  " ",
  "  ",
  "   ",
  "    ",
  "     ",
  "      ",
  "       ",
  "*",
  "**",
  "* *",
  "place holder",
  "place-holder",
  "nothing here",
  "not talking",
  "silence",
  "jaw locked",
  "pure awkwardness",
]
saysomething = [
  "say something",
  "you didn't say anything",
  "is your mouth numb",
  "did you just get a root canal",
  "your gonna get lockjaw",
  "your mouth's gonna stay that way",
  "flabber your gaster",
  "you must not have any language processing up there",
  "do you want me to get a hammer to knock your mouth loose",
  "you're like the opposite of me",
  "let's get a-talkin'",
]
chatgreetings = [
  "hello",
  "how are you",
  "nice to meet you",
  "glad to see you",
  "at your service",
  "we meet again",
  "how nice to see you",
  "i'm good",
  "it's wonderful talking to you",
  "welcome back",
  "how's it going",
]
usergreetings = [
  "hi",
  "hello",
  "how are you",
  "pleased to meet you",
  "i finally meet you",
  "good day to you",
  "good day",
  "how do you do",
  "hola como estas",
  "wassup",
  "what's up",
  "hey",
  "what up",
  "long time no see",
  "how is everything",
  "how's everything",
  "how's life",
  "how you doing",
  "i'm back",
  "heyo",
  "hey buddy",
  "boi",
  "imma talk to you",
  "imma go and talk to you",
  "imma go'an talk to you",
  "tryna say something here",
  "tryna say something to you",
  "oh, hey",
  "oh hey",
  "hey bud",
]
userquestions = [
  "are you real",
  "is this for real",
  "is this happening",
  "how does this work",
  "do you speak",
  "do you work",
  "do you have intelligence",
  "are you harmless",
  "how's your day going",
  "is the weather nice",
  "should i stop talking",
  "am i annoying",
  "do you like me",
  "are you smart",
  "do you like food",
  "do you understand",
  "do you understand me",
]
whatsyourname = [
  "what's your name",
  "who are you",
  "who do you think you are",
  "who the heck do you thing you are",
  "who might you be",
  "and who might you be",
  "may i enquire your identity",
  "who you be",
  "are you an imposter",
  "license please",
  "i take it you are",
  "i take it you are...",
  "your name is"
  "your name is...",
  "what are you",
  "so you said your name was...",
]
mynameis = [
  "i am a chatbot",
  "we've met before",
  "i have no identity",
  "i am who you say i am",
  "i can be anything or anyone",
  "it doesn't matter",
  "what's it to you",
  "why do you want to know",
  "who do you think i am",
  "no-one really knows",
  "it's a mystery",
  "only god knows",
  "it's written in the heavens, want me to kick you there",
  "it's all a matter of... mind your own business",
  "I can't really say",
  "do your parents know you're asking this",
  "my, aren't you nosy",
  "you're a curious sort aren't you",
  "that's rude to ask!",
]
chatanswers = [
  "yes",
  "no",
  "i don't know",
  "maybe",
  "hopefully",
  "it just is",
  "if you think so",
  "probably not",
  "why",
  "why not",
  "good",
  "great",
  "bleh",
  "whatever",
  "oh, ok",
  "ok",
  "i am",
  "if you say i am",
  "i will",
  "i'll try"
]
useranswers = [
  "yes",
  "no",
  "maybe",
  "i don't know",
  "idk",
  "probably",
  "sure",
  "whatever you say",
  "i don't care",
  "doesn't matter",
  "definitely",
  "that's what she said",
  "as if",
  "that's funny"
  "i don't believe so",
  "thank you",
  "thanks",
  "thx",
  "i'm good",
  "i can",
  "why",
  "why not",
  "what",
  "what do you mean",
  "ha",
  "haha",
  "hahaha",
  "really",
  "ok",
  "okay",
  "that's cool",
  "you smell",
  "bruh",
  "breh",
  "bro",
  "dude",
  "what the heck",
  "yep",
  "yup",
  "yeppers",
  "yuppers",
  "yeah",
  "cool",
  "coolio",
  "that's good",
  "that's great",
  "that's awesome",
  "that's amazing",
  "because",
  "bc",
  "because i said",
  "because i said so",
  "why wouldn't i",
  "why can't i",
  "what's it to you",
  "you heard me",
  "are you deaf",
  "do you need hearing aids",
  "just asking",
  "i wanted to",
  "because i wanted to",
  "i wanted to know",
  "i want to know",
  "i'm curious",
  "seems interesting",
  "still here",
  "rattling off sentences here",
  "nuh-uh",
  "nuh uh",
  "not true",
  "deceiver",
  "liar",
  "you're lying",
  "you're a liar",
  "you are",
  "really, you are",
  "good",
  "not nice",
  "oh yeah",
  "oh, yeah",
  "i forgot",
  "now i remember",
  "i remember",
  "sorry",
  "i'm sorry",
  "i'm so sorry",
  "lol",
  "laugh out loud",
  "that makes no sense",
  "you make no sense",
  "i agree",
  "i definitely agree",
  "you're right",
  "so right",
  "oh yeah",
  "i know",
  "i know that",
  "of course i know",
  "of course i know that",
  "duh, of course i know",
  "duh, of course i know that",
  "you too",
  "so are you",
  "oh",
  "oops",
  "oopsies",
  "oops-a-daisy",
  "upsy daisy",
  "no you",
  "no, you",
  "how about you",
  "right back at you",
  "yessir",
  "yessiree",
  "im back",
  "i'm back",
]
userexclamations = [
  "this can't be happening",
  "this is fake",
  "this is stupid",
  "i hate you",
  "this sucks",
  "i love this",
  "this is great",
  "this is cool",
  "i don't like this",
  "this blows",
  "this rocks",
  "cool beans",
  "this is da bomb",
  "hot diggity-dog",
  "shutup",
  "shut-up",
  "shaddap",
  "shut it",
  "shut your pie hole",
  "shut your flabber",
  "you suck",
  "i will",
  "maybe i will",
  "i'll try",
  "i'll give it a go",
  "maybe next time",
  "maybe tomorrow",
  "maybe another time",
  "another time",
  "alright then",
  "a'right then",
  "a'ight then",
  "alright",
  "a'right",
  "a'ight",
  "ight",
  "uh-huh",
  "uh huh",
  "ok then",
  "okay then",
  "ok den",
  "okay den",
  "i don't like your attitude",
  "i don't like yer attitude",
  "your attitude makes me angry",
  "check your attitude",
  "watch it buster",
  "watch it",
  "nah",
  "nah boi",
  "nah brah",
  "nah bruh",
  "do what",
  "nope",
  "nopity-nope",
  "nopity-nope-nope-nope",
  "yes i am",
  "yeah i am",
  "of course i am",
  "if you think so",
  "no way",
  "no way dude",
  "neither are you", 
  "you're not exactly perfect",
  "look who's talking",
  "says the one who is you",
  "no me",
  "no i did",
  "it was me",
  "you're looking at them",
  "great",
  "fine",
  "i'm fine",
  "i'm doing fine",
  "you do",
  "you definitely do",
  "you most definitely do",
  "you're not",
  "you are not",
  "i dunno",
  "i really dunno",
  "i am not",
  "i'm not",
  "i'm really not",
  "i am really not",
  "i don't like you",
  "i really don't like you",
  "i do not like you",
  "i really do not like you",
  "nothing",
  "so what",
  "so the heck what",
  "so the freaking heck what",
  "neither do i",
  "neither am i",
  "i am neither",
  "me neither",
  "i don't either",
  "me too",
  "i am also",
  "i am too",
  "i myself am too",
]
chatexclamations = [
  "it is",
  "it isn't",
  "don't say that",
  "so are you",
  "if you think so",
  "right back at you",
  "that's what i thought",
  "twinsies",
  "are we telepathic",
  "great minds think alike",
  "i don't think so",
  "how could you say that",
  "because i said",
  "it's the only way",
  "i don't know",
  "the world will never know",
  "glad you think so",
  "come back soon",
  "i don't think that's very nice",
  "that's not nice",
  "meanie",
  "you made me cry",
  "why'd you do that",
  "that wasn't sincere",
  "you're not very sincere",
  "i don't like your mouth",
  "you talk to your mother with that mouth",
  "wash your mouth with soap",
  "wash it out with soap",
  "you're being mean",
  "you're mean",
  "why are you being mean",
  "why are you mean",
  "english again",
  "it's english",
  "english yay",
  "it's english again yay",
  "what do you mean",
  "what are you trying to say",
  "dang it",
  "oh dang it",
  "gosh dang it",
  "darn it",
  "oh darn it",
  "gosh darn it",
]
userend = [
  "bye",
  "bye-bye",
  "gotta go",
  "gtg",
  "see you later",
  "see you on the flip side",
  "see you later alligator",
  "in a while crocodile",
  "gotta jet",
  "nice talking to you",
  "i'll be back",
  "brb",
  "be right back",
  "goodbye",
  "good-bye",
  "ciao",
  "adios",
  "adios amigos",
  "arrivederci",
  "later dude",
  "catch you later",
  "hasta luego",
  "hasta la vista",
  "hasta la vista baby",
  "pasta la vista baby", #consolia-comic.com/comics/terminated
]
chatend = [
  "see you around",
  "bye",
  "bye-bye",
  "in a while crocodile",
  "later gator",
  "see you later",
  "i'll just see my way out",
  "a, b, c u later",
  "see ya",
  "adios",
  "later dude",
]

def suggest():
  suggestion = input("Your Suggestion: ")
  suggestions.insert([{loginuser + "'s suggestion": suggestion}])
  return "Suggestion Received!"
  print()
  return "Command Complete"

def hello():
  print(choice(chatgreetings))
  return "Command Complete"

def leave():
  raise SystemExit("Command Complete")
  
def cmd_search():
  with open("commands/command list", "r") as cmdlist:
    with open("commands/commands tutorial", "r") as cmdtutorial:
    
      cmdboth = input("Do you want the tutorial too [y/n]: ")
    
      if cmdboth.lower() == "y":
        print(cmdlist.read())
        print()
        input("press enter to read the tutorial: ")
        clear()
        print(cmdtutorial.read())
      elif cmdboth.lower() == "yes":
        print(cmdlist.read())
        print()
        input("press enter to read the tutorial: ")
        clear()
        print(cmdtutorial.read())
      elif cmdboth.lower() == "n":
        print(cmdlist.read())
        print()
      elif cmdboth.lower() == "no":
        print(cmdlist.read())
        print()
      return "Command Complete"

def changelog():
  with open("CHANGELOG/list of changes", "r") as changes:
    
    seechanges = input("view the changelog [y/n]: ")
    
    if seechanges.lower() == "y":
      print()
      print(changes.read())
      print()
    if seechanges.lower() == "yes":
      print()
      print(changes.read())
      print()
    elif seechanges.lower() == "n":
      return "CHANGELOG CANCELED!"
    elif seechanges.lower() == "no":
      return "CHANGELOG CANCELED!"
    return "Command Complete"

def certificatecmd():
  with open("credits/certificate", "r") as certificate:
    
    seecertificate = input("view the certificate [y/n]: ")
    
    if seecertificate.lower() == "y":
      print()
      print(certificate.read())
      print()
    if seecertificate.lower() == "yes":
      print()
      print(certificate.read())
      print()
    elif seecertificate.lower() == "n":
      return "CERTIFICATE CANCELED!"
    elif seecertificate.lower() == "no":
      return "CERTIFICATE CANCELED!"
    return "Command Complete"
    
prize_given = False

def prize():
    global prize_given
    
    if prize_given:
    
      cp("YOU ALREADY UNBOXED A PRIZE!", "magenta")
      
    else: 
        
      prize_response = choice(prizeunbox)
    
      cp(prize_response, "cyan")
    
      cp("PRIZE UNBOXED!", "magenta")
      
      prize_given = True
    
    return "Command Complete"

def grab_ip():
  ip = socket.gethostbyname(socket.gethostname())
  print(ip)
  return "Command Complete"
  
def clear():
  print("\n" * 100)

clear()

staff = [
"kingofcode",
"pyelias",
"silverstar23",
"clarence",
"alpha",
"damaster",
"zavexeon",
"noside",
"system32",
"iskript",
"happyfakeboulde",
"juan",
"zwack010",
"loknlode13",
]

semistaff = [
"amasad",
"haya",
"timchen",
"lmntl dj",
"jimmymcjimface",
"jbrown",
]

staffpassword = [
"7ebf013ae25747d5f9646b5380adf0d1add777f912ebd88f64cd2ca95faeddb81c33107a7e1231a754f40bdc0289135d11cbb17573d2f2724afb1692ac15adb5"
]

semistaffpassword = [
"0913de549bbebb374c0a55eb695a0e6cc556c7db15b2d5c759c7abb06320e6eb3addd75052b9a0d65a43ccf6658e69e28dd60964c36f5e42caa7508744e7b858"
]

cp(ff("""PyBot\n   v0.9.4""", font="starwars"), "yellow", attrs=["bold"])

print("\n" * 10)

nickname = input ("What Should I Call You: ")

clear()

cp(ff("PyBot\n   v0.9.4", font="starwars"), "yellow", attrs=["bold"])


print("\n" * 10)

lang = input("what's your spoken language: ")

if lang.lower() == "":
  lang = "english"

clear()

cp(ff("PyBot\n   v0.9.4", font="starwars"), "yellow", attrs=["bold"])


print("\n" * 10)

color = input("What color text (folder: text colors): ")

if color in ["Yellow", "YeLlOw", "yElLoW", "YELLOW"]:
  color = "yellow"
elif color in ["Blue", "BlUe", "bLuE", "BLUE"]:
  color = "blue"
elif color in ["Grey", "GrEy", "gReY", "GREY"]:
  color = "grey"
elif color in ["Magenta", "GrEy", "gReY", "GREY"]:
  color = "magenta"
elif color in ["Cyan", "CyAn", "cYaN", "CYAN"]:
  color = "cyan"
elif color in ["White", "WhItE", "wHiTe", "WHITE"]:
  color = "white"
elif color in ["Green", "GrEeN", "gReEn", "GREEN"]:
  color = "green"
elif color in ["Red", "ReD", "rEd", "RED"]:
  color = "red"

clear()

cp(ff("PyBot\n   v0.9.4", font="starwars"), "yellow", attrs=["bold"])

print("\n" * 10)

attrs = input("What text attribute (folder: text attributes): ")

if attrs == "Reversed":
  attrs = "reversed"
elif attrs == "Underline":
  attrs = "underline"
elif attrs == "Bold":
  attrs = "bold"
elif attrs == "Dark":
  attrs = "dark"
elif attrs == "Concealed":
  attrs = "concealed"
elif attrs == "Blink":
  attrs = "blink"

clear()

cp(ff("PyBot\n   v0.9.4", font="starwars"), "yellow", attrs=["bold"])

print("\n" * 10)

session = input("Name your chat session: ")

clear()

cp(ff("PyBot\n   v0.9.4", font="starwars"), "yellow", attrs=["bold"])

print("\n" * 10)

loginuser = input("Enter Your Username: ")

if loginuser == "":
  loginuser = "unknown user"

nmpk, = names.insert([{"nickname": nickname, "username": loginuser, "language": lang, "ip-address": socket.gethostbyname(socket.gethostname()), "session": session, "color":color, "attribute":attrs, "date": time.strftime("%A, %B %d, %Y")}])

if loginuser.lower() in staff:
  clear()
  
  loginpass = input("Enter Your Password: ")
  byte_pass = loginpass.encode("utf-8")

  if sha512(byte_pass).hexdigest() in staffpassword:
    print("access granted!")
  else:
    print("Invalid Password!")
    exit()
elif loginuser.lower() in semistaff:
  clear()
  
  loginpass = input("Enter Your Password: ")
  byte_pass = loginpass.encode("utf-8")

  if sha512(byte_pass).hexdigest() in semistaffpassword:
    print("access granted!")
  else:
    print("Invalid Password!")
    exit()
else:
  pass

if loginuser.lower() in staff:
  namecolor = "red"
  nameattrs = "bold"
elif loginuser.lower() in semistaff:
  namecolor = "green"
  nameattrs = "bold"
elif loginuser.lower() in loginuser:
  namecolor = "yellow"
  nameattrs = "bold"

clear()
  
helloname = [
  "Hello " + nickname + "! I'm PyBot!",
  "Hi " + nickname + "! My job is to keep you company!",
  "What's up " + nickname + "! I hope you're having fun!",
  "Greetings my good friend " + nickname + "!",
  "Having a good time " + nickname + "? Well, I sure hope so!",
]

loginuseranswer = [
"how ya doing " + loginuser,
"nice to meet you " + loginuser,
"it's a pleasure talking " + loginuser,
"nothing's ever amiss " + loginuser,
"i take it your " + loginuser,
"its on the house " + loginuser,
"you'll always feel at home with PyBot, " + loginuser,
"i will never intrude upon you " + loginuser,
"it's been nice talking to you " + loginuser,
"i don't know why, but you're a good friend " + loginuser,
"let's talk about stuff " + loginuser,
"i really enjoy conversing with you " + loginuser,
"it's been a wonderful day here with you " + loginuser,
]
  
clear()

cp(
"""Access Granted:

\nWelcome """ + loginuser + "\n\n\nEntering session: " + session, 'yellow', attrs=["blink"])

wait(3.5)

clear()

conv = {"pybot":[]}
pk, = conversations.insert([conv])

go = True
secure_chat = False
room = False
translator = Translator()

while go:
  
    userinput = input(cd(loginuser + ": ", namecolor, attrs=[nameattrs]))
        
    def translate():
      global lang
      lang = input("What Language (look in languages folder): ")
      if lang.lower() == "":
        lang = "english"
      return "Language changed"

    def add_color():
      cp("pybot: ", "magenta", end="")
      if color == attrs == "":
        print(bot_response)
      elif color == "":
        cp(bot_response, "white", attrs=[attrs])
      elif attrs == "":
        cp(bot_response, color)
      else:
        cp(bot_response, color, attrs=[attrs])
    
    def fake():
      while True:
        fake_bot_response = choice(fakeanswer)
        if color == attrs == "":
          print(fake_bot_response)
        elif color == "":
          cp(fake_bot_response, "white", attrs=[attrs])
        elif attrs == "":
          cp(fake_bot_response, color)
        else:
          cp(fake_bot_response, color, attrs=[attrs])
        fakeprompt = input(cd(loginuser + ": ", "yellow")) # so they get a prompt
        if fakeprompt.lower() == "!exitfake":
          return "EXITING FAKE MODE!"
    
    def stupid():
      while True:
        stupid_bot_response = choice(stupidanswer)
        if color == attrs == "":
          print(stupid_bot_response)
        elif color == "":
          cp(stupid_bot_response, "white", attrs=[attrs])
        elif attrs == "":
          cp(stupid_bot_response, color)
        else:
          cp(stupid_bot_response, color, attrs=[attrs])
        stupidprompt = input(cd(loginuser + ": ", "yellow")) # so they get a prompt
        if stupidprompt.lower() == "!exitstupid":
          return "EXITING STUPID MODE!"
          
    def secure():
      while True:
         
        global secure_chat
        secure_chat = True
          
        if secure_chat == True:
            
          return "SECURE MODE ENABLED"
        
    def notsecure():
      while True:
        
        global secure_chat
        secure_chat = False
        
        if secure_chat == False:
          
          return "SECURE MODE DISABLED"
    
    
    def insult():
      adjective1 = choice(phrase1)
      adjective2  = choice(phrase2)
      noun1 = choice(phrase3)
      cp("thou art a " + adjective1 + adjective2 + noun1 + "!", "cyan", attrs=["bold"])
      return "you have been insulted!"
    
    def sessionname():
      wantname = input("view session name [y/n]: ")
      
      if wantname.lower() == "y":
        cp("Your session name: " + session, "cyan", attrs=["bold"])
      elif wantname.lower() == "yes":
        cp("Your session name: " + session, "cyan", attrs=["bold"])
      elif wantname.lower() == "n":
        return "SESSION VIEWER CANCELED!"
      elif wantname.lower() == "no":
        return "SESSION VIEWER CANCELED!"
      return "Command Complete"

    def usernamename():
      wantname = input("view username [y/n]: ")
      
      if wantname.lower() == "y":
        cp("Your username: " + loginuser, "cyan", attrs=["bold"])
      elif wantname.lower() == "yes":
        cp("Your username: " + loginuser, "cyan", attrs=["bold"])
      elif wantname.lower() == "n":
        return "USERNAME VIEWER CANCELED!"
      elif wantname.lower() == "no":
        return "USERNAME VIEWER CANCELED!"
      return "Command Complete"
    
    def new_session():
      global session
      session = input("Enter new session name: ")

      names.replace([{"nickname": nickname, "username": loginuser, "language": lang, "ip-address": socket.gethostbyname(socket.gethostname()), "session": session, "date": time.strftime("%A, %B %d, %Y")}], Pks([nmpk])) 
      return "Command Complete"
    
    def new_name():
      global loginuser
      loginuser = input("Enter a new username: ")

      names.replace([{"nickname": nickname, "username": loginuser, "language": lang, "ip-address": socket.gethostbyname(socket.gethostname()), "session": session, "date": time.strftime("%A, %B %d, %Y")}], Pks([nmpk])) 
      return "Command Complete"

    def clearcmd():
      print("\n" * 100)
      return "Screen Cleared"
  
    if loginuser in userinput.lower().split():
      bot_response = choice(loginuseranswer)
    elif nickname in userinput.lower().split():
      bot_response = choice(helloname)
    elif superowner in userinput.lower().split():
      bot_response = choice(superowneranswer)
    elif owner in userinput.lower().split():
      bot_response = choice(owneranswer)
    elif userinput.lower() in uselessstuff:
      bot_response = choice(uselessanswers)
    elif userinput.lower() in uselessanswers:
      bot_response = choice(chatanswers)
    elif userinput.lower() in saysomething:
      bot_response = choice(chatanswers)
    elif userinput.lower() in nosay:
      bot_response = choice(saysomething)
    elif userinput.lower() in userquestions:
      bot_response = choice(chatanswers)
    elif userinput.lower() in usergreetings:
      bot_response = choice(chatgreetings)
    elif userinput.lower() in userexclamations:
      bot_response = choice(chatexclamations)
    elif userinput.lower() in useranswers:
      bot_response = choice(chatexclamations)
    elif userinput.lower() in whatsyourname:
      bot_response = choice(mynameis)
    elif userinput.lower() in mynameis:
      bot_response = choice(chatanswers)
    elif userinput.lower() in userend:
      bot_response = choice(chatend) + "!"
      go = False
    elif userinput.lower() == "!suggest":
      bot_response = suggest()
    elif userinput.lower() == "!hello":
      bot_response = hello()
    elif userinput.lower() == "!leave":
      bot_response = leave()
    elif userinput.lower() == "!commands":
      bot_response = cmd_search()
    elif userinput.lower() == "!prize":
      bot_response = prize()
    elif userinput.lower() == "!grab-ip":
      bot_response = grab_ip()
    elif userinput.lower() == "!secure":
      bot_response = secure()
    elif userinput.lower() == "!exitsecure":
      bot_response = notsecure()
    elif userinput.lower() == "!changelog":
      bot_response = changelog()
    elif userinput.lower() == "!certificate":
      bot_response = certificatecmd()
    elif userinput.lower() == "!insult":
      bot_response = insult()
    elif userinput.lower() == "!change-lang":
      bot_response = translate()
    elif userinput.lower() == "!session":
      bot_response = sessionname()
    elif userinput.lower() == "!username":
      bot_response = usernamename()
    elif userinput.lower() == "!new-session":
      bot_response = new_session()
    elif userinput.lower() == "!new-name":
      bot_response = new_name()
    elif userinput.lower() == "!clear":
      bot_response = clearcmd()
    elif userinput.lower() == "!fake":
      bot_response = fake()
    elif userinput.lower() == "!stupid":
      bot_response = stupid()
    elif userinput.lower()[0] == "!":
      bot_response = "command not found"
    else :
      bot_response = "I don't understand!"
    
    userresponse = translator.translate(userinput, src=lang).text #######
    
    bot_response = translator.translate(bot_response, dest=lang).text #######
    
    add_color()
    
    if not secure_chat:
      conv["pybot"].append([userinput, bot_response])
      conversations.replace([conv], Pks([pk]))
