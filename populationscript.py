import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'PLHQ.settings')
import django
django.setup()
from playerhq.models import Games,Reviews, Categories

def populate():

    # Games in the RPGs category
    RPGs = [ {'gamename':'The Witcher 3', 'gamerating': 5, 'gamedescription': 'The Witcher 3: Wild Hunt is a 2015 action role-playing game developed and published by CD Projekt and based on The Witcher series of fantasy novels by Andrzej Sapkowski. It is the sequel to the 2011 game The Witcher 2: Assassins of Kings, played in an open world with a third-person perspective.', 'gamecategory': 'RPGs', 'image': 'TheWitcher3.jpg'},
            {'gamename':'The Last Of Us', 'gamerating': 5, 'gamedescription': 'The Last of Us is a 2013 action-adventure survival horror video game developed by Naughty Dog and published by Sony Computer Entertainment. Players control Joel, a smuggler tasked with escorting a teenage girl, Ellie, across a post-apocalyptic United States. The Last of Us is played from a third-person perspective.', 'gamecategory': 'RPGs', 'image': 'TLOU.jpg' },
           {'gamename':'The Elder Scrolls V: Skyrim', 'gamerating': 4, 'gamedescription': 'The Elder Scrolls V: Skyrim is an action role-playing game, playable from either a first or third-person perspective. The player may freely roam over the land of Skyrim which is an open world environment consisting of wilderness expanses, dungeons, cities, towns, fortresses, and villages.', 'gamecategory': 'RPGs', 'image': 'skyrim.jpg'},
            {'gamename':'Mass Effect 3', 'gamerating': 3, 'gamedescription': 'Mass Effect 3 is an action role-playing game in which the player takes control of Commander Shepard from a third-person perspective. Shepards gender, appearance, military background, combat training, and first name are determined by the player before the game begins.', 'gamecategory': 'RPGs', 'image': 'masseffect3.jpg'},
            {'gamename':'Legend Of Zelda Breath of the Wild', 'gamerating': 3, 'gamedescription': 'Similar to the original Legend of Zelda (1986), players are given little instruction and can explore the open world freely. Tasks include collecting multipurpose items to aid in objectives or solving puzzles and side quests for rewards. The world is unstructured and designed to reward experimentation, and the story can be completed in a nonlinear fashion.', 'gamecategory': 'RPGs', 'image': 'TLOZ.jpg'},
            {'gamename':'Assassins Creed', 'gamerating': 4, 'gamedescription': 'The plot is set in a fictional history of real-world events and follows the centuries-old struggle between the Assassins, who fight for peace with free will, and the Templars, who desire peace through control. The game primarily takes place during the Third Crusade in the Holy Land in 1191, with the plot revolving around the Secret Order of Assassins, based upon the Hashshashin sect.', 'gamecategory': 'RPGs', 'image': 'assassinscreed.jpg'},
            {'gamename':'God of War III', 'gamerating': 5, 'gamedescription': 'Loosely based on Greek mythology, the game is set in ancient Greece with vengeance as its central motif. The player controls the protagonist and former God of War Kratos, after his betrayal at the hands of his father Zeus, King of the Olympian gods. Reigniting the Great War, Kratos ascends Mount Olympus until he is abandoned by the Titan Gaia.', 'gamecategory': 'RPGs', 'image': 'GOW4.jpg'},
            {'gamename':'Dark Souls III', 'gamerating': 3, 'gamedescription': 'Dark Souls III is an action role-playing game played in a third-person perspective, similar to previous games in the series. According to lead director and series creator Hidetaka Miyazaki, the games gameplay design followed "closely from Dark Souls II".[1] Players are equipped with a variety of weapons to fight against enemies, such as bows, throwable projectiles, and swords.', 'gamecategory': 'RPGs', 'image': 'darksouls.jpg'},
           ]

    # Reviews for Games in the RPGs category
    RPGreviews = [{'gamename': 'The Last Of Us','reviewername': 'Saad', 'review': 'Adolescents have it particularly tough in the zombie apocalypse. Everyone around them is obsessed with survival--which is certainly understandable--but every ounce of a teenagers instincts is pushing him or her toward goofing off.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                  {'gamename': 'The Witcher 3','reviewername': 'Areeb', 'review': 'unlike its predecessor, The Witcher 3: Wild Hunt doesnt exactly come screaming off the starting line. Compared to The Witcher 2, where you are immediately plunged headlong into a sexy story of intrigue and betrayal, this main quest can seem mundane, even perfunctory at times.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                  {'gamename': 'The Elder Scrolls V: Skyrim','reviewername': 'Daniyal', 'review': ' I was stacking books on a shelf in my house in Whiterun, one of Skyrims major cities, when I noticed a weapon rack right beside it. I set a sacrificial dagger in one slot, an Orcish mace in the other. They were on display for nobody but me and my computer-controlled housecarl, Lydia, who sat at a table patiently waiting for me to ask her to go questing.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'Mass Effect 3','reviewername': 'Faateh', 'review': ' I was stacking books on a shelf in my house in Whiterun, one of Skyrims major cities, when I noticed a weapon rack right beside it. I set a sacrificial dagger in one slot, an Orcish mace in the other. They were on display for nobody but me and my computer-controlled housecarl, Lydia, who sat at a table patiently waiting for me to ask her to go questing.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'Legend Of Zelda Breath of the Wild','reviewername': 'Ali', 'review': 'The Legend of Zelda: Breath of the Wild’s sheer freedom and sense of adventure is a remarkable achievement. Right from the start, the vast landscape of Hyrule is thrown completely open to you, and it constantly finds ways to pique your curiosity with mysterious landmarks, complex hidden puzzles, and enemy camps to raid for treasure and weapons. ', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'Assassins Creed','reviewername': 'Hamza', 'review': ' Ubisoft really was not joking around when it called the latest Assassins Creed game an Odyssey. Its not just in the Greek tragedy-inspired story, the vast, vast map or the sheer number of hours you are going to sink into it. Its the journey. The journey from one Greek island to another, with dolphins and whales cresting the waves alongside your boat.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'God of War III','reviewername': 'Bazil', 'review': ' God of War 3 is a great end to Kratos console trilogy. Its not perfect, with some uneven storytelling and progression here and there, but it is still a fantastic overall package. The combat is stellar once again, it is bloodier than ever, and it is one of the best looking game ever released.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                  {'gamename': 'Dark Souls III','reviewername': 'Asim', 'review': ' Dark Souls 3 does suffer from occasional framerate dips and a few underwhelming boss fights, but beyond that, its epic scale, aggressive obstacles, and rich development of existing lore make it the grandest and fiercest Dark Souls adventure yet.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                 ]

    # Games in the Racing category
    Racing = [{'gamename':'Need For Speed Underground', 'gamerating': 4, 'gamedescription': 'Underground rebooted the franchise, ignoring the previous Need for Speed games which featured sports cars and exotics. It was the first game in the series to offer a career mode featuring a storyline, and a garage mode that allowed players to fully customize their cars with a large variety of brand-name performance and visual upgrades.', 'gamecategory': 'Racing', 'image': 'NFS.jpg'},
              {'gamename':'Forza Horizon', 'gamerating': 3, 'gamedescription': 'Forza Horizon 4 is a racing video game set in an open world environment based in a fictionalised Great Britain, with regions that include condensed representations of Edinburgh, the Lake District (including Derwentwater), and the Cotswolds (including Broadway), among others, and features currently over 670 licensed cars.', 'gamecategory': 'Racing', 'image': 'forza.jpg'}, 
             {'gamename':'Blur', 'gamerating': 3, 'gamedescription': 'In Blurs career mode, the player will encounter numerous characters and many licensed cars ranging from Dodge Vipers to Lotus Exiges to Ford Transit and vans fitted with F1 engines, all of which have full damage modeling and separate traits such as Acceleration, Speed, Drift, Grip and Stability. Some special car models have been designed by Bizarre Creations themselves.', 'gamecategory': 'Racing', 'image': 'blur.png'}, 
              {'gamename':'Burnout', 'gamerating': 2, 'gamedescription': 'The most notable feature that the series is known for is its crash mode. This series is well known for its emphasis on aggressive driving and high speed. In-race rewards are given to a player if they take risks such as driving towards oncoming traffic or deliberately attempting to make their opponents crash.', 'gamecategory': 'Racing', 'image': 'burnout.jpg'},
              {'gamename':'Dirty Rally', 'gamerating': 2, 'gamedescription': 'Dirt Rally 2.0 is focused on rallying and rallycross. Players compete in timed stage events on tarmac and off-road terrain in varying weather conditions. The game features stages in Argentina, Australia, New Zealand, Poland, Spain and the United States. Codemasters also announced plans to expand the game through the release of downloadable content, and released stages in Finland, Germany, Greece, Monte Carlo, Sweden and Wales. ', 'gamecategory': 'Racing', 'image': 'dirtyrally.jpg'}, 
             ]

    # Reviews for Games in the Racing category
    Racingreview = [{'gamename': 'Need For Speed Underground','reviewername': 'Aaron', 'review': 'It is not as exciting as the drag racing, but it makes for a nice change of pace. The main mode features more than 100 different races, but you will see the same tracks time and time again. The career mode is called "go underground," and it lets you engage in all of the games race types in its 111 races.', 'graphics': 4, 'storyline':4, 'gameplay':4},
                    {'gamename': 'Forza Horizon','reviewername': 'Marko', 'review': 'Evocative, surprising, varied, free-flowing: Forza Horizon is a lot of things that Forza Motorsport never has been." Some will decry the move 60 to 30 frames per second, but its been handled flawlessly, with perfectly smooth visuals and low-latency controls.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                   {'gamename': 'Blur','reviewername': 'Maroo', 'review': 'The single-player Career mode in Blur features some brutal A.I. While I was desperately trying to master my drifting skills and just maneuver the games treacherous tracks, the A.I. was busy launching attack after attack on me at the most inopportune moments.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                    {'gamename': 'Burnout','reviewername': 'Georgia', 'review': 'Look, it is really simple, Burnout Paradise Remastered is essential for fans of racing games everywhere. They just do not make them like this anymore (but they really, really should).', 'graphics': 2, 'storyline': 2, 'gameplay': 2},
                    {'gamename': 'Dirty Rally','reviewername': 'Alex', 'review': 'Dirty Rall is more than just the best Codemasters rally game to date; it’s arguably the best racing game Codemasters has produced in at least a decade. Perhaps ever. It’s certainly the best crack at a hard-core rally game since 2004’s heavily-worshiped Richard Burns Rally from Warthog Games. It’s brilliant.', 'graphics': 2, 'storyline': 2, 'gameplay': 2},
                   ]

    # Games in the Others category
    Others = [{'gamename':'Call Of Duty', 'gamerating': 4, 'gamedescription': 'Call of Duty is a first-person shooter video game franchise published by Activision. Starting out in 2003, it first focused on games set in World War II, but over time, the series has seen games set in modern times, the midst of the Cold War, futuristic worlds, and outer space.', 'gamecategory': 'Others', 'image': 'COD.jpg'},
             {'gamename':'GTA V', 'gamerating': 4, 'gamedescription': 'Grand Theft Auto V is a 2013 action-adventure game developed by Rockstar North and published by Rockstar Games. It is the first main entry in the Grand Theft Auto series since 2008s Grand Theft Auto IV. Set within the fictional state of San Andreas, based on Southern California, the single-player story follows three criminals and their efforts to commit heists while under pressure from a government agency and powerful crime figures.', 'gamecategory': 'Others', 'image': 'gta5.jpg'},
              {'gamename':'Uncharted 4', 'gamerating': 5, 'gamedescription': 'Uncharted 4: A Thiefs End is a 2016 action-adventure game developed by Naughty Dog and published by Sony Computer Entertainment. It is the fourth main entry in the Uncharted series. Players control Nathan Drake, a former treasure hunter coaxed out of retirement by his estranged brother Samuel. With Nathans longtime partner, Sullivan, they search for clues for the location of Henry Averys long-lost treasure.', 'gamecategory': 'Others', 'image': 'uncharted4.jpg'},
              {'gamename':'Battlefield V', 'gamerating': 3, 'gamedescription': 'Battlefield V is focused extensively on party-based features and mechanics, scarcity of resources, and removing "abstractions" from game mechanics to increase realism. There is an expanded focus on player customization through the new Company system, where players can create multiple characters with cosmetic and weapon options. Cosmetic items, and currency used to purchase others, are earned by completing in-game objectives.', 'gamecategory': 'Others', 'image': 'battlefield.jpg'},
              {'gamename':'Metal Gear Solid V', 'gamerating': 2, 'gamedescription': 'Metal Gear Solid V: The Phantom Pain is a stealth game in which players take the role of Punished "Venom" Snake from a third-person perspective in an open world.[1] The gameplay elements were largely unchanged from Ground Zeroes, meaning that players will have to sneak from several points in the game world, avoiding enemy guards, and remaining undetected. Included in Snakes repertoire are binoculars, maps, a variety of weapons, explosives, and stealth-based items such as cardboard boxes and decoys.', 'gamecategory': 'Others', 'image': 'metalgear.jpg'},
              {'gamename':'Super Mario', 'gamerating':1 , 'gamedescription': 'The Super Mario games follow Marios adventures, typically in the fictional Mushroom Kingdom with Mario as the player character. He is often joined by his brother, Luigi, and occasionally by other members of the Mario cast. As in platform video games, the player runs and jumps across platforms and atop enemies in themed levels.', 'gamecategory': 'Others', 'image': 'supermario.jpg'},
             ]

    # Reviews for Games in the Others category
    othersreview = [{'gamename': 'Call Of Duty','reviewername': 'Bers', 'review': 'Call all of Duty’s return to World War II is surprisingly a fast-paced take on the classic setting. It provides for a good campaign, a great new mode in multiplayer among other good changes, and a creepier, dense version of Nazi Zombies.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                   {'gamename': 'GTA V','reviewername': 'Abdullah', 'review': 'For me, Grand Theft Auto V’s extraordinary scope is summed up in two favourite moments. One is from a mid-game mission in which I flew a plane into another plane, fought the crew, hijacked the thing, and then parachuted out and watched it crash into the sea to escape death at the hands of incoming military fighter jets.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                    {'gamename': 'Uncharted 4','reviewername': 'Humza', 'review': 'In amongst its frantic combat, slick parkour, and outrageous action choreography, Uncharted 4: A Thief’s End achieves something wonderful: maturity. This is less a breezy lad’s tale revelling in fortune and glory and more a story about the lads when they’re all grown up, bolstered by an equally developed graphics engine and career-high performances from its cast. A surprisingly assured set of multiplayer modes ices the cake.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                    {'gamename': 'Battlefield V','reviewername': 'Shaz', 'review': 'Welcome, Battlefield fans! Now that we’ve taken in-depth looks at the single-player and multiplayer sides of Battlefield V, it’s time for our final overview and verdict. For the full picture, make sure to check out each part.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                    {'gamename': 'Metal Gear Solid V','reviewername': 'Rauf', 'review': 'I had planned it all very carefully. There were way too many guards still looking for me, and with sunrise coming shortly, I had almost no chance of making it out to the nearest safe landing zone with an injured prisoner on my shoulders. But I wouldn’t have to. During the night, I planted some C4 on this outpost’s radio communication equipment, the anti-aircraft battery, and most importantly, their AA radar.', 'graphics': 2, 'storyline': 2, 'gameplay':2},
                    {'gamename': 'Super Mario','reviewername':'Hammad', 'review': 'Its amazing how every element comes together for a thoroughly refined platforming experience. The level design is nothing short of genius, and the flawless controls make every leap more joyous than the last. Everyone who has not already played through the Wii U version should pick this up immediately.', 'graphics': 1, 'storyline':1, 'gameplay':1},
                   ]

    # Games in the Superhero Category
    SuperHero = [{'gamename':'Batman Arkham Asylum', 'gamerating': 4, 'gamedescription': 'Arkham Asylum is set in the fictional Arkham Asylum, a facility on Arkham Island off the coast of Gotham City that houses criminally insane supervillains. The game features a large ensemble of characters from the history of Batman comics.', 'gamecategory': 'SuperHero', 'image': 'batman.jpg'},
                {'gamename':'Spiderman 2', 'gamerating': 3, 'gamedescription': 'Spider-Man 2 is in most versions, an open-world action-adventure video game, with a few role-playing elements and takes place from a third-person perspective. The Treyarch version of the game allow the player to freely roam around Manhattan, Roosevelt, Ellis, and Liberty Islands.', 'gamecategory': 'SuperHero', 'image': 'spiderman.jpg'},
                {'gamename':'Injustice 2', 'gamerating': 2, 'gamedescription': 'Injustice 2 is a fighting game in which players compete in one-on-one combat using characters from the DC Universe and other third-party franchises. Using different combinations of directional inputs and button presses, players must perform basic attacks, special moves, and combos to try to damage and knock out the opposing fighter.', 'gamecategory': 'SuperHero', 'image': 'injustice.jpg'},
                 {'gamename':'X Men Origins', 'gamerating': 1, 'gamedescription': 'X-Men Origins takes influences from games such as God of War and Devil May Cry with a third person perspective. The Uncaged Edition also features a large amount of blood and gore. Enemies can be dismembered in several ways in addition to the graphic display of Wolverines healing factor.', 'gamecategory': 'SuperHero', 'image': 'xmen.jpg'},
                 {'gamename':'Green Lantern', 'gamerating': 1, 'gamedescription': 'At the funeral of Green Lantern Abin Sur on the Green Lantern Corps headquarters on Oa, the corrupted robotic predecessors of the Corps, the Manhunters, attack. You control Green Lantern Hal Jordan as he joins the fight to defend Oa against this menace, armed with the might of the power ring.', 'gamecategory': 'SuperHero', 'image': 'greenlantern.jpg'},
                ]

    # Reviews for Games in the Superhero Category
    SuperHeroreview = [{'gamename': 'Batman Arkham Asylum','reviewername': 'Max', 'review': 'Its not often that I am conflicted about a game. Do not get me wrong, review scores are in the eye of the beholder so I am sure there are plenty of times that you have read something I have written and not agreed with me. I mean that it is rare for me to play a game during a demo and not have a solid idea of what the final product is going to be.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                      {'gamename': 'Spiderman 2','reviewername': 'Boris', 'review': 'Generally speaking, the Marvel Comics legend Spider-Man has always done reasonably well for himself in the world of video games. That trend continues with the latest team-up from Activision and Treyarch in Spider-Man 2.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                       {'gamename': 'Injustice 2','reviewername': 'Huzaifa', 'review': 'Like its cast of heroes, Injustice 2 is exceptional. The fight mechanics have been guided in the right direction following 2013’s Injustice: Gods Among Us. The hours of play potential in the new Multiverse mode alone is impressive. The heroes and villains of the DC Universe look better here than they have in any game before, even as they star in a grim and joyless “what-if” storyline.', 'graphics': 2, 'storyline': 2, 'gameplay':2},
                       {'gamename': 'X Men Origins','reviewername': 'Iyan', 'review': 'Oh, videogames based on movies based on comic books. To the casual consumer, you are a "must buy" because the movie was awesome, so clearly the game will be even better. To the seasoned gamer, you are a title with more potential for a train wreck than Miley Cyrus at 18.', 'graphics': 1, 'storyline': 1, 'gameplay':1},
                       {'gamename': 'Green Lantern','reviewername': 'Roots', 'review': 'If the fact that I am always in a Superman shirt when I am on camera did not clue you in, I am a DC Comics nerd. As such, I have learned to steel myself when it comes to DC video games. I go in expecting to be supremely disappointed so as not to get my heart broken once again. (Burn in hell, Superman 64.) Green Lantern: Rise of the Manhunters didn ot disappoint me but that is not to say it wowed me in any respect.', 'graphics': 1, 'storyline': 1, 'gameplay':1},
                      ]

    # Categories map to a dictionary of dictionaries of the above lists
    categories = {'Racing' : {'game': Racing, 'review': Racingreview},
                  'RPGs' : {'game': RPGs, 'review': RPGreviews },
                  'SuperHero': {'game': SuperHero, 'review': SuperHeroreview},
                  'Others': {'game': Others, 'review': othersreview},
                  }

    # From the categories dictionary, the key is a category to be added
    # Games and Reviews are subsequently added
    for cat, cat_data in categories.items():
        add_category(cat)
        for p in cat_data['game']:

            add_game(p['gamename'], p['gamerating'], p['gamedescription'], p['gamecategory'], p['image'])
            
            for x in cat_data['review']:
                if x['gamename'] == p['gamename']:
                    d = add_game(p['gamename'], p['gamerating'], p['gamedescription'], p['gamecategory'], p['image'])
                    add_review(x['gamename'], x['reviewername'], x['review'],x['graphics'], x['storyline'], x['gameplay'])

# Methods to get or create objects in each of the models, assigning their values to the given values
def add_category(catName):
    c = Categories.objects.get_or_create(catName=catName)[0]
    c.catName = catName
    c.save()
    return c

    
def add_review( GameName, ReviewerName, Review, Graphics,Storyline,Gameplay):
    a = Reviews.objects.get_or_create(GameName=GameName)[0]
    a.ReviewerName = ReviewerName
    a.Review = Review
    a.Graphics = Graphics
    a.Storyline = Storyline
    a.Gameplay = Gameplay
    a.save()
    return a
    
def add_game( title, rating, des, GameCategory, image):
    p = Games.objects.get_or_create( GameName=title)[0]
    p.GameRating=rating
    p.GameImage=image
    p.Gamedescription=des
    p.GameCategory = GameCategory
    p.save()
    return p

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()


