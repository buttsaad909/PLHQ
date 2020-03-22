import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'PLHQ.settings')
import django
django.setup()
from playerhq.models import Games,Reviews, Comments, Categories

def populate():
    
    #categories = [{'RPGs': ['The Witcher 3','The Last Of Us', 'Skyrim' , 'Mass Effect 2', 'Legend Of Zelda Breath of the Wild',
    #                       'Dark Souls III', 'Assassins Creed', 'God of War III']}, 
    #              {'Racing': ['Need For Speed Underground', 'Blur', 'Froza Horizon','Dirty Rally', 'Burnout']},
    #              {'SuperHero': ['Spiderman 2', 'Injustice', 'Batman Arkham Asylum', 'X Men Origins']}, 
    #              {'Others': ['Call Of Duty', 'Metal Gear Solid', 'GTA V', 'Mario', metal gear solid, battlefield, uncharted 4, wold among us]}]
    
    RPGs = [ {'gamename':'The Witcher 3', 'gamerating': 5, 'gamedescription': 'The Witcher 3: Wild Hunt is a 2015 action role-playing game developed and published by CD Projekt and based on The Witcher series of fantasy novels by Andrzej Sapkowski. It is the sequel to the 2011 game The Witcher 2: Assassins of Kings, played in an open world with a third-person perspective.', 'gamecategory': 'RPGs'},
            {'gamename':'The Last Of Us', 'gamerating': 5, 'gamedescription': 'The Last of Us is a 2013 action-adventure survival horror video game developed by Naughty Dog and published by Sony Computer Entertainment. Players control Joel, a smuggler tasked with escorting a teenage girl, Ellie, across a post-apocalyptic United States. The Last of Us is played from a third-person perspective.', 'gamecategory': 'RPGs' },
           {'gamename':'The Elder Scrolls V: Skyrim', 'gamerating': 4, 'gamedescription': 'The Elder Scrolls V: Skyrim is an action role-playing game, playable from either a first or third-person perspective. The player may freely roam over the land of Skyrim which is an open world environment consisting of wilderness expanses, dungeons, cities, towns, fortresses, and villages.', 'gamecategory': 'RPGs'},
            {'gamename':'Mass Effect 3', 'gamerating': 3, 'gamedescription': 'Mass Effect 3 is an action role-playing game in which the player takes control of Commander Shepard from a third-person perspective. Shepards gender, appearance, military background, combat training, and first name are determined by the player before the game begins.', 'gamecategory': 'RPGs'},
            {'gamename':'Legend Of Zelda Breath of the Wild', 'gamerating': 3, 'gamedescription': 'Similar to the original Legend of Zelda (1986), players are given little instruction and can explore the open world freely. Tasks include collecting multipurpose items to aid in objectives or solving puzzles and side quests for rewards. The world is unstructured and designed to reward experimentation, and the story can be completed in a nonlinear fashion.', 'gamecategory': 'RPGs'},
            {'gamename':'Assassins Creed', 'gamerating': 4, 'gamedescription': 'The plot is set in a fictional history of real-world events and follows the centuries-old struggle between the Assassins, who fight for peace with free will, and the Templars, who desire peace through control. The game primarily takes place during the Third Crusade in the Holy Land in 1191, with the plot revolving around the Secret Order of Assassins, based upon the Hashshashin sect.', 'gamecategory': 'RPGs'},
            {'gamename':'God of War III', 'gamerating': 5, 'gamedescription': 'Loosely based on Greek mythology, the game is set in ancient Greece with vengeance as its central motif. The player controls the protagonist and former God of War Kratos, after his betrayal at the hands of his father Zeus, King of the Olympian gods. Reigniting the Great War, Kratos ascends Mount Olympus until he is abandoned by the Titan Gaia.', 'gamecategory': 'RPGs'},
            {'gamename':'Dark Souls III', 'gamerating': 3, 'gamedescription': 'Dark Souls III is an action role-playing game played in a third-person perspective, similar to previous games in the series. According to lead director and series creator Hidetaka Miyazaki, the games gameplay design followed "closely from Dark Souls II".[1] Players are equipped with a variety of weapons to fight against enemies, such as bows, throwable projectiles, and swords.', 'gamecategory': 'RPGs'},
           ]
    RPGreviews = [{'gamename': 'The Last Of Us','reviewername': 'Saad', 'review': 'Adolescents have it particularly tough in the zombie apocalypse. Everyone around them is obsessed with survival--which is certainly understandable--but every ounce of a teenagers instincts is pushing him or her toward goofing off.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                  {'gamename': 'The Witcher 3','reviewername': 'Areeb', 'review': 'unlike its predecessor, The Witcher 3: Wild Hunt doesnt exactly come screaming off the starting line. Compared to The Witcher 2, where you are immediately plunged headlong into a sexy story of intrigue and betrayal, this main quest can seem mundane, even perfunctory at times.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                  {'gamename': 'The Elder Scrolls V: Skyrim','reviewername': 'Daniyal', 'review': ' I was stacking books on a shelf in my house in Whiterun, one of Skyrims major cities, when I noticed a weapon rack right beside it. I set a sacrificial dagger in one slot, an Orcish mace in the other. They were on display for nobody but me and my computer-controlled housecarl, Lydia, who sat at a table patiently waiting for me to ask her to go questing.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'Mass Effect 3','reviewername': 'Faateh', 'review': ' I was stacking books on a shelf in my house in Whiterun, one of Skyrims major cities, when I noticed a weapon rack right beside it. I set a sacrificial dagger in one slot, an Orcish mace in the other. They were on display for nobody but me and my computer-controlled housecarl, Lydia, who sat at a table patiently waiting for me to ask her to go questing.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'Legend Of Zelda Breath of the Wild','reviewername': 'Ali', 'review': 'The Legend of Zelda: Breath of the Wild’s sheer freedom and sense of adventure is a remarkable achievement. Right from the start, the vast landscape of Hyrule is thrown completely open to you, and it constantly finds ways to pique your curiosity with mysterious landmarks, complex hidden puzzles, and enemy camps to raid for treasure and weapons. ', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'Assassins Creed','reviewername': 'Hamza', 'review': ' Ubisoft really was not joking around when it called the latest Assassins Creed game an Odyssey. Its not just in the Greek tragedy-inspired story, the vast, vast map or the sheer number of hours you are going to sink into it. Its the journey. The journey from one Greek island to another, with dolphins and whales cresting the waves alongside your boat.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                  {'gamename': 'God of War III','reviewername': 'Bazil', 'review': ' God of War 3 is a great end to Kratos console trilogy. Its not perfect, with some uneven storytelling and progression here and there, but it is still a fantastic overall package. The combat is stellar once again, it is bloodier than ever, and it is one of the best looking game ever released.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                  {'gamename': 'Dark Souls III','reviewername': 'Asim', 'review': ' Dark Souls 3 does suffer from occasional framerate dips and a few underwhelming boss fights, but beyond that, its epic scale, aggressive obstacles, and rich development of existing lore make it the grandest and fiercest Dark Souls adventure yet.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                 ]
    
    RPGcomments = [{'gamename': 'The Last Of Us', 'commentname':'Lewis', 'comment':'The Last of Us is a masterpiece, every single detail and part of it. The story, gameplay, musical score, and voice acting are all incredible. Recently voted PlayStation’s Game of the Decade. The fact that nearly a decade.'},
                    {'gamename': 'The Last Of Us', 'commentname':'Faisal', 'comment':'Several things were running through my head as I was playing the game: 1. Man, I hope this game never ends - and it does not end for around 15-16 hours; 2. How many GOTY awards this game is going to get; '}, 
                   {'gamename': 'The Witcher 3','commentname':'Naomi', 'comment':'It took three tries to get into it, and, many moments when I felt like I should drop it because of wonky movement and combat and a few UI issues, but I persisted and I am so glad I did.'},
                   {'gamename': 'The Elder Scrolls V: Skyrim','commentname':'Chris', 'comment':'Let me start by saying that the game is very good in terms of graphics, gameplay and first and foremost the general idea, story and open-world it offers.'},
                   {'gamename': 'Mass Effect 3','commentname':'Shaq', 'comment':'As I played through the game I was in gaming Nirvana. This was the apotheosis of gamers game. The choices I faced, bringing the galaxy together, loosing dear friends along the way and the humor, all of this felt right. '},
                   {'gamename': 'Legend Of Zelda Breath of the Wild','commentname':'Owen', 'comment':'As I played through the game I was in gaming Nirvana. This was the apotheosis of gamers game. The choices I faced, bringing the galaxy together, loosing dear friends along the way and the humor, all of this felt right'},
                   {'gamename': 'Assassins Creed','commentname':'Mathew', 'comment':'Full disclosure; I could not finish this game. I played for around 20 hours before I threw in the towel and decided that I did not want to play it anymore. The game is absolutely enormous, but the sidequests are so repetitive'},
                   {'gamename': 'God of War III','commentname':'Karen', 'comment':'This game was the fatuous game for this series because the game is EMPTY form the brutal fight like the previous series except the fight between the sun and his old manso please in the next time do not do the same mistake.'},
                   {'gamename': 'Dark Souls III','commentname':'Scarlet', 'comment':'This was my first Souls game, and wow..... it is extremely good. Like good. Very good. Good good. OST, movement, look, style. Fantastic.The last DLC seemed like a nice way to tie up the series, and I thoroughly enjoyed it.'},
                  ]
    
    Racing = [{'gamename':'Need For Speed Underground', 'gamerating': 4, 'gamedescription': 'Underground rebooted the franchise, ignoring the previous Need for Speed games which featured sports cars and exotics. It was the first game in the series to offer a career mode featuring a storyline, and a garage mode that allowed players to fully customize their cars with a large variety of brand-name performance and visual upgrades.', 'gamecategory': 'Racing'},
              {'gamename':'Forza Horizon', 'gamerating': 3, 'gamedescription': 'Forza Horizon 4 is a racing video game set in an open world environment based in a fictionalised Great Britain, with regions that include condensed representations of Edinburgh, the Lake District (including Derwentwater), and the Cotswolds (including Broadway), among others, and features currently over 670 licensed cars.', 'gamecategory': 'Racing'}, 
             {'gamename':'Blur', 'gamerating': 3, 'gamedescription': 'In Blurs career mode, the player will encounter numerous characters and many licensed cars ranging from Dodge Vipers to Lotus Exiges to Ford Transit and vans fitted with F1 engines, all of which have full damage modeling and separate traits such as Acceleration, Speed, Drift, Grip and Stability. Some special car models have been designed by Bizarre Creations themselves.', 'gamecategory': 'Racing'}, 
              {'gamename':'Burnout', 'gamerating': 2, 'gamedescription': 'The most notable feature that the series is known for is its crash mode. This series is well known for its emphasis on aggressive driving and high speed. In-race rewards are given to a player if they take risks such as driving towards oncoming traffic or deliberately attempting to make their opponents crash.', 'gamecategory': 'Racing'},
              {'gamename':'Dirty Rally', 'gamerating': 2, 'gamedescription': 'Dirt Rally 2.0 is focused on rallying and rallycross. Players compete in timed stage events on tarmac and off-road terrain in varying weather conditions. The game features stages in Argentina, Australia, New Zealand, Poland, Spain and the United States. Codemasters also announced plans to expand the game through the release of downloadable content, and released stages in Finland, Germany, Greece, Monte Carlo, Sweden and Wales. ', 'gamecategory': 'Racing'}, 
             ]
    
    Racingreview = [{'gamename': 'Need For Speed Underground','reviewername': 'Aaron', 'review': 'It is not as exciting as the drag racing, but it makes for a nice change of pace. The main mode features more than 100 different races, but you will see the same tracks time and time again. The career mode is called "go underground," and it lets you engage in all of the games race types in its 111 races.', 'graphics': 4, 'storyline':4, 'gameplay':4},
                    {'gamename': 'Forza Horizon','reviewername': 'Marko', 'review': 'Evocative, surprising, varied, free-flowing: Forza Horizon is a lot of things that Forza Motorsport never has been." Some will decry the move 60 to 30 frames per second, but its been handled flawlessly, with perfectly smooth visuals and low-latency controls.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                   {'gamename': 'Blur','reviewername': 'Maroo', 'review': 'The single-player Career mode in Blur features some brutal A.I. While I was desperately trying to master my drifting skills and just maneuver the games treacherous tracks, the A.I. was busy launching attack after attack on me at the most inopportune moments.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                    {'gamename': 'Burnout','reviewername': 'Georgia', 'review': 'Look, it is really simple, Burnout Paradise Remastered is essential for fans of racing games everywhere. They just do not make them like this anymore (but they really, really should).', 'graphics': 2, 'storyline': 2, 'gameplay': 2},
                    {'gamename': 'Dirty Rally','reviewername': 'Alex', 'review': 'Dirty Rall is more than just the best Codemasters rally game to date; it’s arguably the best racing game Codemasters has produced in at least a decade. Perhaps ever. It’s certainly the best crack at a hard-core rally game since 2004’s heavily-worshiped Richard Burns Rally from Warthog Games. It’s brilliant.', 'graphics': 2, 'storyline': 2, 'gameplay': 2},
                   ]
    
    Racingcomments = [{'gamename': 'Need For Speed Underground','commentname':'Jen', 'comment':'The first Underground is a very good racer!Arcade,fun and It was under the ground if I can say so.Top tuner cars,cool customization options,awesome soundtrack-that are some of the coolest things about the game.'}, 
                      {'gamename': 'Forza Horizon','commentname':'Roxxane', 'comment':'Ever heard of the phrase drop a gear and disappear, well if you have then you know what it means, and that’s exactly what turn 10 studios, playground games and Microsoft studios has done to the competition'},
                      {'gamename': 'Blur','commentname':'Anne', 'comment':'Blur is the perfect blend of arcade racer and a kart racer. I have always wondered what would happen when those two genres combined, and I was seriously impressed with the results.'},
                      {'gamename': 'Burnout','commentname':'Dwayne', 'comment':'Burnout made my childhood and I still love it whenever I play it!'},
                      {'gamename': 'Dirty Rally','commentname':'Kevin', 'comment':'Not the best of games I have ever played and would not recommended.'},
                     ]
    
    Others = [{'gamename':'Call Of Duty', 'gamerating': 4, 'gamedescription': 'Call of Duty is a first-person shooter video game franchise published by Activision. Starting out in 2003, it first focused on games set in World War II, but over time, the series has seen games set in modern times, the midst of the Cold War, futuristic worlds, and outer space.', 'gamecategory': 'Others'},
             {'gamename':'GTA V', 'gamerating': 4, 'gamedescription': 'Grand Theft Auto V is a 2013 action-adventure game developed by Rockstar North and published by Rockstar Games. It is the first main entry in the Grand Theft Auto series since 2008s Grand Theft Auto IV. Set within the fictional state of San Andreas, based on Southern California, the single-player story follows three criminals and their efforts to commit heists while under pressure from a government agency and powerful crime figures.', 'gamecategory': 'Others'},
              {'gamename':'Uncharted 4', 'gamerating': 5, 'gamedescription': 'Uncharted 4: A Thiefs End is a 2016 action-adventure game developed by Naughty Dog and published by Sony Computer Entertainment. It is the fourth main entry in the Uncharted series. Players control Nathan Drake, a former treasure hunter coaxed out of retirement by his estranged brother Samuel. With Nathans longtime partner, Sullivan, they search for clues for the location of Henry Averys long-lost treasure.', 'gamecategory': 'Others'},
              {'gamename':'Battlefield V', 'gamerating': 3, 'gamedescription': 'Battlefield V is focused extensively on party-based features and mechanics, scarcity of resources, and removing "abstractions" from game mechanics to increase realism. There is an expanded focus on player customization through the new Company system, where players can create multiple characters with cosmetic and weapon options. Cosmetic items, and currency used to purchase others, are earned by completing in-game objectives.', 'gamecategory': 'Others'},
              {'gamename':'Metal Gear Solid V', 'gamerating': 2, 'gamedescription': 'Metal Gear Solid V: The Phantom Pain is a stealth game in which players take the role of Punished "Venom" Snake from a third-person perspective in an open world.[1] The gameplay elements were largely unchanged from Ground Zeroes, meaning that players will have to sneak from several points in the game world, avoiding enemy guards, and remaining undetected. Included in Snakes repertoire are binoculars, maps, a variety of weapons, explosives, and stealth-based items such as cardboard boxes and decoys.', 'gamecategory': 'Others'},
              {'gamename':'Super Mario', 'gamerating':1 , 'gamedescription': 'The Super Mario games follow Marios adventures, typically in the fictional Mushroom Kingdom with Mario as the player character. He is often joined by his brother, Luigi, and occasionally by other members of the Mario cast. As in platform video games, the player runs and jumps across platforms and atop enemies in themed levels.', 'gamecategory': 'Others'},
             ]
    
    othersreview = [{'gamename': 'Call Of Duty','reviewername': 'Bers', 'review': 'Call all of Duty’s return to World War II is surprisingly a fast-paced take on the classic setting. It provides for a good campaign, a great new mode in multiplayer among other good changes, and a creepier, dense version of Nazi Zombies.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                   {'gamename': 'GTA V','reviewername': 'Abdullah', 'review': 'For me, Grand Theft Auto V’s extraordinary scope is summed up in two favourite moments. One is from a mid-game mission in which I flew a plane into another plane, fought the crew, hijacked the thing, and then parachuted out and watched it crash into the sea to escape death at the hands of incoming military fighter jets.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                    {'gamename': 'Uncharted 4','reviewername': 'Humza', 'review': 'In amongst its frantic combat, slick parkour, and outrageous action choreography, Uncharted 4: A Thief’s End achieves something wonderful: maturity. This is less a breezy lad’s tale revelling in fortune and glory and more a story about the lads when they’re all grown up, bolstered by an equally developed graphics engine and career-high performances from its cast. A surprisingly assured set of multiplayer modes ices the cake.', 'graphics': 5, 'storyline': 5, 'gameplay':5},
                    {'gamename': 'Battlefield V','reviewername': 'Shaz', 'review': 'Welcome, Battlefield fans! Now that we’ve taken in-depth looks at the single-player and multiplayer sides of Battlefield V, it’s time for our final overview and verdict. For the full picture, make sure to check out each part.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                    {'gamename': 'Metal Gear Solid V','reviewername': 'Rauf', 'review': 'I had planned it all very carefully. There were way too many guards still looking for me, and with sunrise coming shortly, I had almost no chance of making it out to the nearest safe landing zone with an injured prisoner on my shoulders. But I wouldn’t have to. During the night, I planted some C4 on this outpost’s radio communication equipment, the anti-aircraft battery, and most importantly, their AA radar.', 'graphics': 2, 'storyline': 2, 'gameplay':2},
                    {'gamename': 'Super Mario','reviewername':'Hammad', 'review': 'Its amazing how every element comes together for a thoroughly refined platforming experience. The level design is nothing short of genius, and the flawless controls make every leap more joyous than the last. Everyone who has not already played through the Wii U version should pick this up immediately.', 'graphics': 1, 'storyline':1, 'gameplay':1},
                   ]
    
    Otherscomments = [{'gamename': 'Call Of Duty', 'commentname':'Dani','comment':'Call of Duty: Black Ops is yet another beginning of a line of games in the Call of Duty series, which in this case is Black Ops. is a game that many people like, I think a game very good, but I find it tiring in many mom'}, 
                      {'gamename': 'GTA V','commentname':'Marc', 'comment':'TA V is exactly what you would expect it to be: an open world where you can do anything your heart desires, from sleeping with hookers to flying airplanes to just aimlessly running around.'},
                      {'gamename': 'Uncharted 4','commentname':'GabarSingh', 'comment':'This game is funny, action-packed, emotional, BEAUTIFUL to look at, and straight-up a blast to play. I have replayed it so many times, and never get tired of it. The action and combat scenes are incredible'},
                      {'gamename': 'Battlefield V','commentname':'UrtaJujjar', 'comment':'This game is EPIC. Truly a collection of masterfully rendered set of battlefields with game modes that encourage intense combat that pushes into every area of the maps.'},
                      {'gamename': 'Metal Gear Solid V','commentname':'WehshiVadera', 'comment':'Wow, obviously not sure how this is so high rated. Super repetitive being that so many of the story missions occur in the same open world places that you may have just decimated one day ago.'},
                      {'gamename': 'Super Mario','commentname':'BataRang', 'comment':'With every new, full-fledged 3D Mario game comes a certain set of expectations, and those are generally that it&rsquo;s going to be one of the generation&rsquo;s highlights.'},
                     ]
    
    SuperHero = [{'gamename':'Batman Arkham Asylum', 'gamerating': 4, 'gamedescription': 'Arkham Asylum is set in the fictional Arkham Asylum, a facility on Arkham Island off the coast of Gotham City that houses criminally insane supervillains. The game features a large ensemble of characters from the history of Batman comics.', 'gamecategory': 'SuperHero'},
                {'gamename':'Spiderman 2', 'gamerating': 3, 'gamedescription': 'Spider-Man 2 is in most versions, an open-world action-adventure video game, with a few role-playing elements and takes place from a third-person perspective. The Treyarch version of the game allow the player to freely roam around Manhattan, Roosevelt, Ellis, and Liberty Islands.', 'gamecategory': 'SuperHero'},
                {'gamename':'Injustice 2', 'gamerating': 2, 'gamedescription': 'Injustice 2 is a fighting game in which players compete in one-on-one combat using characters from the DC Universe and other third-party franchises. Using different combinations of directional inputs and button presses, players must perform basic attacks, special moves, and combos to try to damage and knock out the opposing fighter.', 'gamecategory': 'SuperHero'},
                 {'gamename':'X Men Origins', 'gamerating': 1, 'gamedescription': 'X-Men Origins takes influences from games such as God of War and Devil May Cry with a third person perspective. The Uncaged Edition also features a large amount of blood and gore. Enemies can be dismembered in several ways in addition to the graphic display of Wolverines healing factor.', 'gamecategory': 'SuperHero'},
                 {'gamename':'Green Lantern', 'gamerating': 1, 'gamedescription': 'At the funeral of Green Lantern Abin Sur on the Green Lantern Corps headquarters on Oa, the corrupted robotic predecessors of the Corps, the Manhunters, attack. You control Green Lantern Hal Jordan as he joins the fight to defend Oa against this menace, armed with the might of the power ring.', 'gamecategory': 'SuperHero'},
                ]
    
    SuperHeroreview = [{'gamename': 'Batman Arkham Asylum','reviewername': 'Max', 'review': 'Its not often that I am conflicted about a game. Do not get me wrong, review scores are in the eye of the beholder so I am sure there are plenty of times that you have read something I have written and not agreed with me. I mean that it is rare for me to play a game during a demo and not have a solid idea of what the final product is going to be.', 'graphics': 4, 'storyline': 4, 'gameplay':4},
                      {'gamename': 'Spiderman 2','reviewername': 'Boris', 'review': 'Generally speaking, the Marvel Comics legend Spider-Man has always done reasonably well for himself in the world of video games. That trend continues with the latest team-up from Activision and Treyarch in Spider-Man 2.', 'graphics': 3, 'storyline': 3, 'gameplay':3},
                       {'gamename': 'Injustice 2','reviewername': 'Huzaifa', 'review': 'Like its cast of heroes, Injustice 2 is exceptional. The fight mechanics have been guided in the right direction following 2013’s Injustice: Gods Among Us. The hours of play potential in the new Multiverse mode alone is impressive. The heroes and villains of the DC Universe look better here than they have in any game before, even as they star in a grim and joyless “what-if” storyline.', 'graphics': 2, 'storyline': 2, 'gameplay':2},
                       {'gamename': 'X Men Origins','reviewername': 'Iyan', 'review': 'Oh, videogames based on movies based on comic books. To the casual consumer, you are a "must buy" because the movie was awesome, so clearly the game will be even better. To the seasoned gamer, you are a title with more potential for a train wreck than Miley Cyrus at 18.', 'graphics': 1, 'storyline': 1, 'gameplay':1},
                       {'gamename': 'Green Lantern','reviewername': 'Roots', 'review': 'If the fact that I am always in a Superman shirt when I am on camera did not clue you in, I am a DC Comics nerd. As such, I have learned to steel myself when it comes to DC video games. I go in expecting to be supremely disappointed so as not to get my heart broken once again. (Burn in hell, Superman 64.) Green Lantern: Rise of the Manhunters didn ot disappoint me but that is not to say it wowed me in any respect.', 'graphics': 1, 'storyline': 1, 'gameplay':1},
                      ]
    
    SuperHerocomments = [{'gamename': 'Batman Arkham Asylum', 'commentname':'Tory', 'comment':'You know, with this game being out for 10 years now, I really didn’t feel the experience I had with it before was good enough (I sucked). So I took my Xbox 360 and started playing and, wow. '}, 
                         {'gamename': 'Spiderman 2','commentname':'Ben', 'comment':'Spider-Man 2 is undoubtedly one of the best game Spider and one of the best games based on film, it is impressive the evolution of the first of the PS2 for this, starting now that Web-Swing is more fluid'},
                         {'gamename': 'X Men Origins','commentname':'Cook', 'comment':'It is the BEST MOVIE GAME ever made and one of the best super hero game of all time and one of the best games I played this year. PROS = It is true to the Wolverine formula, Game is brutal and fits the nature of wolveri.'},
                         {'gamename': 'Injustice 2','commentname':'Aresha', 'comment':'If you are looking for great left to right fighting game similar to Mortal Combat and Street Fighter but with your favorite DC characters, look no further.'},
                         {'gamename': 'Green Lantern','commentname':'Maryam', 'comment':'Movie-based games often go wrong, based on bad movies are often even worse, and unfortunately Green Lantern: Rise of the Manhunters did not escape, the game is bad, '},
                        ]
    
    categories = {'Racing' : {'game': Racing, 'review': Racingreview, 'comments': Racingcomments},
                  'RPGs' : {'game': RPGs, 'review': RPGreviews, 'comments':RPGcomments },
                  'SuperHero': {'game': SuperHero, 'review': SuperHeroreview, 'comments':SuperHerocomments},
                  'Others': {'game': Others, 'review': othersreview, 'comments': Otherscomments},
                  }
    
    for cat, cat_data in categories.items():
        add_category(cat)
        for p in cat_data['game']:

            add_game(p['gamename'], p['gamerating'], p['gamedescription'], p['gamecategory'])
            
            for x in cat_data['review']:
                if x['gamename'] == p['gamename']:
                    d = add_game(p['gamename'], p['gamerating'], p['gamedescription'], p['gamecategory'])
                    add_review(d,x['gamename'], x['reviewername'], x['review'],x['graphics'], x['storyline'], x['gameplay'])
                    
                    for z in cat_data['comments']:
                        
                        if z['gamename'] == x['gamename']:
                            a = add_review(d,x['gamename'], x['reviewername'], x['review'],x['graphics'], x['storyline'], x['gameplay'])
                            add_comment(a,z['gamename'],z['commentname'], z['comment'] )

def add_category(catName):
    c = Categories.objects.get_or_create(catName=catName)[0]
    c.catName = catName
    c.save()
    return c

    
def add_review(cat, GameName, ReviewerName, Review, Graphics,Storyline,Gameplay):
    a = Reviews.objects.get_or_create(games=cat, GameName=GameName)[0]
    a.ReviewerName = ReviewerName
    a.Review = Review
    a.Graphics = Graphics
    a.Storyline = Storyline
    a.Gameplay = Gameplay
    a.save()
    return a
    
def add_game( title, rating, des, GameCategory):
    p = Games.objects.get_or_create( GameName=title)[0]
    p.GameRating=rating
    p.Gamedescription=des
    p.GameCategory = GameCategory
    p.save()
    return p

def add_comment(a, gamename, commentername, comment):
    z = Comments.objects.get_or_create( reviews=a)[0]
    z.GameName = gamename
    z.CommentName=commentername
    z.Comments=comment
    z.save()
    return z

#def add_category(name):
#    if name == 'RPGs':
#        c = Categories.objects.get_or_create(RPGs=name)[0]
#    elif name == 'Racing':
#        c = Categories.objects.get_or_create(Racing=name)[0]
#    elif name == 'SuperHero':
#        c = Categories.objects.get_or_create(SuperHero=name)[0]
#    elif name == 'Others':
#        c = Categories.objects.get_or_create(Others=name)[0]
#    c.save()
#    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

