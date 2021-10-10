# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define org = Character("Mr MakeUC")
define player = Character("[povname]")
define A = Character("Momo")
define B = Character("Shizuku")
define C = Character("Yagami")


# The game starts here.

label start:
    play music "audio/daily.mp3" volume 1.0
    scene outside1
    show organizer
    org "Hello, there! I am the organizer of this Hackathon."
    org "Glad to meet you! You can call me Mr MakeUC."
    hide organizer
    show player_happy
    "Player" "Hi Mr MakeUC!"
    hide player_happy
    show organizer
    org "Welcome to this game!"
    org "This is the game that lets the player experience the Hackathon journey."
    org "For some people, they haven't experience this kind of competition before."
    org "This is the great opportunity to experience it!"
    org "Before we start, tell me a little bit about yourself."
    org "What is your name?"

    hide organizer
    show player_happy
    python:
        player = renpy.input("Please enter a name:", length=32)
        player = player.strip()
        if not player:
            player= "Rinka"

    player "My name is [player]!"
    hide player_happy
    show organizer
    org "Ok [player], let's enjoy the game!"

label screen2_1:
    scene windows1
    "In the hallway of University of Cincinnati... "

    show player_wondering
    player "It is very boring now..."
    hide player_wondering
    show player_happy
    player "(My name is [player], I am an university student...)"
    hide player_happy
    show player_wondering
    player "(Because of the school holidays, I feel very boring now.)"
    player "(for now, let's see if there is something interesting in this event....)"
    scene makeucposter1
    show player_wondering
    player "Suddenly, there is a poster caught my attention."


    player "Hmm..Hackathon competition?"
    player "It sound good...And I will receive generous prizes if I win. Besides, I can get opportunity to learn something new!"

    scene windows1
    hide player_wondering
    show player_happy
    player "(At the end, I just sign up the competition.)"

label screen2_2:
    scene hall1
    show player_wondering
    player "This should be the venue for the game..."
    hide player_wondering
    show player_happy
    player "(This competition is organized by Make UC, although I ain't sure. But there are air conds in the playground, which is quite satisfying!)"
    player "(It was a bit lively there, so I decided to go forward and see what happened.)"
    hide player_happy
    show player_wondering
    player "Oh my god.."
    player "(There was a long line in front of the registration desk. It seems that it will take some time to line up.)"
    player "Hmmm..."

label screen3:
    screen hall1
    hide player_wondering
    show momo_happy
    A "Finally I found you, [player]!"
    hide momo_happy
    show player_happy
    player "Just relax [A], there is a long gap before the competition right?"
    player "([A], one of my teammates in this competition! She is the first one to reply my invitation as well.)"
    hide player_happy
    show momo_happy
    A "Forget it, how about others?"
    hide momo_happy
    show momo_happy:
        linear 1.0 xalign 1.0 yalign 0.0
    show player_happy:
        linear 1.0 xalign 0.0 yalign 0.0
    "(A happy conversation between [A] and player)"
    show shizuku_happy:
        linear 1.0 xalign 0.35 yalign 0.0
    show yagami_happy:
        linear 1.0 xalign 0.65 yalign 0.0
    player "(While we finish the talk, another two teammates slowly came close to us from behind.)"
    hide momo_happy
    hide player_happy
    hide yagami_happy
    hide shizuku_happy
    show shizuku_happy
    B "Looks like we are all here!"
    hide shizuku_happy
    show yagami_happy
    C "Yup! Fantasy Four Girls assemble!"
    hide yagami_happy
    show player_happy
    player "(They are [B] and [C], they are also my teammates in this hackathon!)"
    player "Let's do it together guys!"
    hide player_happy
    show player_happy:
        linear 1.0 xalign 1.0 yalign 0.0
    show momo_happy:
        linear 1.0 xalign 0.0 yalign 0.0
    show shizuku_happy:
        linear 1.0 xalign 0.35 yalign 0.0
    show yagami_happy:
        linear 1.0 xalign 0.65 yalign 0.0
    "All" "Yes!"

label screen3_1:
    scene hall1
    show player_happy:
        linear 1.0 xalign 1.0 yalign 0.0
    show momo_happy:
        linear 1.0 xalign 0.0 yalign 0.0
    show shizuku_happy:
        linear 1.0 xalign 0.35 yalign 0.0
    show yagami_happy:
        linear 1.0 xalign 0.65 yalign 0.0
    "(After a series hard work and project submission...)"
    hide player_happy
    hide momo_happy
    hide shizuku_happy
    hide yagami_happy
    show organizer
    org "Thank you so much for participating this hackathon, now we would like to announce the winner is ..."
    org "SuperMario! Congratulation!"
    show player_happy:
        linear 1.0 xalign 1.0 yalign 0.0
    show momo_cry:
        linear 1.0 xalign 0.0 yalign 0.0
    show shizuku_cry:
        linear 1.0 xalign 0.35 yalign 0.0
    show yagami_cry:
        linear 1.0 xalign 0.65 yalign 0.0
    player "Guys, don't be sad! Althought we lose the game, but more importantly, we learned somethings new in this hackathon experience!"

label ending:
    scene makeucposter1
    show organizer
    org "In a hackathon, it is okay if you did't complete it. Most importantly is you learn something throught this event."
    org "Technical skills maybe are the advantages in competing, but the teamwork and creativity are equally important."
    org "Now you have learn how a hackathon works, join one now!!"

    "--HYPERLINK TO DEVPOST--"

    scene outside1
    "MADE BY TRIPLE MARBLES FROM MALAYSIA!"
    "THANK YOU FOR PLAYING!"


return
