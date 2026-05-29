

fighter_set = {

    "Bouftou noir": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 2,
        "effect": ["robuste"],
        "description": "Robuste"
    },
    "Bouftou blanc": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["robuste"],
        "description": "Robuste"
    },
    "Bouftou céleste": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 3,
        "atk": 2,
        "strike": 2,
        "pv": 3,
        "effect": ["soutien", "on_soutien"],
        "description": "Soutien (Bouftou). Soigne l'allié soutenu de 2"
    },
    "Bouftou de guerre": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 4,
        "atk": 3,
        "strike": 2,
        "pv": 4,
        "effect": ["on_inv_target"],
        "description": "Apparition : donnez +1 Atk à une Bête"
    },
    "Bouftou primitif": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 5,
        "atk": 3,
        "strike": 2,
        "pv": 5,
        "effect": ["on_inv_target"],
        "description": "Apparition : infligez 2 dégats à un combattant"
    },
    "Boufmouth": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["end_turn"],
        "description": "A la fin de votre tour, Bénédiction 1"
    },
    "Royalmouth": {
        "color": "Zéphyr",
        "archetype": ["Bête", "Bouftou"],
        "cost": 5,
        "atk": 5,
        "strike": 1,
        "pv": 5,
        "effect": ["action"],
        "description": "Action : soignez entièrement un Bouftou allié et donnez lui +1/1/1"
    },
    "Sanglier Porcass": {
        "color": "Pourpre",
        "archetype": ["Porcass"],
        "cost": 1,
        "atk": 1,
        "strike": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Berger Porcass": {
        "color": "Pourpre",
        "archetype": ["Porcass"],
        "cost": 2,
        "atk": 2,
        "strike": 0,
        "pv": 1,
        "effect": ["on_inv"],
        "description": "Apparition : invoquez un Sanglier Porcass"
    },
    "Chevaucheur de Porcass": {
        "color": "Pourpre",
        "archetype": ["Porcass"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 1,
        "effect": ["rapide"],
        "description": "Frappe rapide"
    },
    "Samurai Porcass": {
        "color": "Pourpre",
        "archetype": ["Porcass"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv_target"],
        "description": "Apparition : redressez un combattant adverse en mode blocage"
    },
    "Berserker Porcass": {
        "color": "Pourpre",
        "archetype": ["Porcass"],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 5,
        "effect": ["end_turn"],
        "description": "A la fin de votre tour, donner 2 Atk à ce combattant s'il est blessé"
    },
    "Flammetin": {
        "color": "Pourpre",
        "archetype": ["Élémentaire", "Lave"],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : ajoutez un Élémentaire de flamme à votre main"
    },
    "Tortue de lave": {
        "color": "Pourpre",
        "archetype": ["Élémentaire", "Lave"],
        "cost": 3,
        "atk": 1,
        "strike": 1,
        "pv": 3,
        "effect": ["on_mort"],
        "description": "Dernier souffle : appelez une Tortue de lave (engagée)"
    },
    "Élémentaire de lave": {
        "color": "Pourpre",
        "archetype": ["Élémentaire", "Lave"],
        "cost": 5,
        "atk": 5,
        "strike": 3,
        "pv": 5,
        "effect": ["on_strike"],
        "description": "Lorsqu'il strike, strikez 1 sur votre héros"
    },
    "Acolyte de la souffrance": {
        "color": "Pourpre",
        "archetype": [],
        "cost": 3,
        "atk": 1,
        "strike": 1,
        "pv": 4,
        "effect": ["end_turn"],
        "description": "A la fin de votre tour, piochez une carte s'il est blessé"
    },
    "Sergent cruel": {
        "color": "Pourpre",
        "archetype": [],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv_target"],
        "description": "Apparition : infligez 1 dégats à un combattant et donnez lui 2 Atk"
    },
    "Singe féroce": {
        "color": "Pourpre",
        "archetype": ["Bête"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 4,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Gobelin malade": {
        "color": "Pourpre",
        "archetype": [],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 1,
        "effect": ["on_mort"],
        "description": "Dernier souflle : strike 2"
    },
    "Maitre blessé": {
        "color": "Pourpre",
        "archetype": [],
        "cost": 3,
        "atk": 4,
        "strike": 1,
        "pv": 6,
        "effect": ["on_inv"],
        "description": "Apparition : infligez 4 dégats à ce combattant"
    },
    "Chargeur orc": {
        "color": "Pourpre",
        "archetype": ["Orc"],
        "cost": 4,
        "atk": 4,
        "strike": 2,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : si votre main est vide, piochez 3 cartes"
    },
    "Le Découpeur": {
        "color": "Pourpre",
        "archetype": ["Orc"],
        "cost": 6,
        "atk": 5,
        "strike": 2,
        "pv": 6,
        "effect": ["robuste"],
        "description": "Robuste"
    },
    "Ogre glouton": {
        "color": "Pourpre",
        "archetype": ["Orc"],
        "cost": 7,
        "atk": 6,
        "strike": 3,
        "pv": 6,
        "effect": ["overkill"],
        "description": "Overkill : strike 2"
    },

    "Tofukaz": {
        "color": "Zéphyr",
        "archetype": ["Tofu"],
        "cost": 1,
        "atk": 0,
        "strike": 2,
        "pv": 1,
        "effect": ["on_strike"],
        "description": "Après avoir striké, ce combattant est détruit"
    },
    "Tofu mélanique": {
        "color": "Zéphyr",
        "archetype": ["Tofu"],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 1,
        "effect": ["rapide"],
        "description": "Frappe rapide"
    },
    "Tofu royal": {
        "color": "Zéphyr",
        "archetype": ["Tofu"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["end_turn"],
        "description": "A la fin de votre tour, redressez ce combattant"
    },
    "Tofu ventripotent": {
        "color": "Zéphyr",
        "archetype": ["Tofu"],
        "cost": 4,
        "atk": 4,
        "strike": 2,
        "pv": 3,
        "effect": ["action"],
        "description": "Action : renvoyez un combattant adverse dans sa main"
    },
    "Écuyer": {
        "color": "Ocre",
        "archetype": [],
        "cost": 1,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Porte bouclier": {
        "color": "Ocre",
        "archetype": [],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 4,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Guetteur d'argent": {
        "color": "Ocre",
        "archetype": [],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 6,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Garde antique": {
        "color": "Ocre",
        "archetype": [],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 2,
        "effect": ["bouclier"],
        "description": "Bouclier divin"
    },
    "Robot blindé": {
        "color": "Ocre",
        "archetype": ["Méca"],
        "cost": 2,
        "atk": 2,
        "strike": 0,
        "pv": 2,
        "effect": ["bouclier"],
        "description": "Bouclier divin"
    },
    "Luminotron": {
        "color": "Ocre",
        "archetype": ["Méca"],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 2,
        "effect": ["soutien"],
        "description": "Soutien"
    },
    "Engin de guerre": {
        "color": "Ocre",
        "archetype": ["Méca"],
        "cost": 6,
        "atk": 6,
        "strike": 2,
        "pv": 6,
        "effect": ["soutien"],
        "description": "Soutien (Méca)"
    },
    "Robot de soin": {
        "color": "Ocre",
        "archetype": ["Méca"],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 5,
        "effect": ["on_inv_target"],
        "description": "Apparition : soigne un allié de 3"
    },
    "Ziliax": {
        "color": "Ocre",
        "archetype": ["Méca"],
        "cost": 5,
        "atk": 4,
        "strike": 2,
        "pv": 2,
        "effect": ["bouclier", "soutien", "on_soutien"],
        "description": "Bouclier divin. Soutien. Donnez bouclier divin à l'allié soutenu"
    },
    "Rejeton de lumière": {
        "color": "Ocre",
        "archetype": [],
        "cost": 1,
        "atk": 2,
        "strike": 1,
        "pv": 2,
        "effect": ["on_mort"],
        "description": "Dernier souffle : Bénédiction 3 chez l'adversaire"
    },
    "Pacificateur": {
        "color": "Ocre",
        "archetype": [],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["action"],
        "description": "Action : passez l'Atk d'un combattant à 1"
    },
    "Silencieux": {
        "color": "Ocre",
        "archetype": [],
        "cost": 4,
        "atk": 4,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : réduisez au silence tous les combattants adverses"
    },
    "Chevalier gemme": {
        "color": "Ocre",
        "archetype": [],
        "cost": 4,
        "atk": 4,
        "strike": 1,
        "pv": 3,
        "effect": ["bouclier", "overkill"],
        "description": "Bouclier divin. Overkill : Bénédiction 1"
    },
    "Cavalier d'argent": {
        "color": "Ocre",
        "archetype": [],
        "cost": 3,
        "atk": 3,
        "strike": 2,
        "pv": 2,
        "effect": ["soutien"],
        "description": "Soutien"
    },
    "Entraineur": {
        "color": "Ocre",
        "archetype": [],
        "cost": 2,
        "atk": 1,
        "strike": 2,
        "pv": 1,
        "effect": ["action"],
        "description": "Action : donnez 1 Strike à tous vos autres combattants"
    },
    "Archer d'élite": {
        "color": "Ocre",
        "archetype": [],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 1,
        "effect": ["on_inv_target"],
        "description": "Apparition : infligez 2 dégats"
    },

    "Archère elf": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 1,
        "effect": ["on_inv_target"],
        "description": "Apparition : infligez 1 dégat"
    },
    "Lutin des bois": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 2,
        "atk": 2,
        "strike": 0,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : piochez un sort"
    },
    "Papillon enchanté": {
        "color": "Verdant",
        "archetype": [],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv_target"],
        "description": "Apparition : réduisez au silence un combattant"
    },
    "Sylvenier": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : vous pouvez encrer une carte supplémentaire ce tour"
    },
    "Druide du sabre": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv_target"],
        "description": "Inspiration : infligez 2 dégats"
    },
    "Elf de guerre": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 3,
        "atk": 2,
        "strike": 2,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : si vous possédez min 8 mana, gagne +1/0/1 et robuste"
    },
    "Dryade": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["action"],
        "description": "Action : ajoutez un Elf de votre défausse à votre main"
    },
    "Satyre mystique": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 4,
        "atk": 2,
        "strike": 1,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Apparition : réduisez le cout en mana d'un sort de 2"
    },
    "Golem ancien": {
        "color": "Verdant",
        "archetype": [],
        "cost": 4,
        "atk": 4,
        "strike": 1,
        "pv": 5,
        "effect": [],
        "description": ""
    },
    "Gardien du bosquet": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 4,
        "effect": ["on_mort"],
        "description": "Dernier souffle : se place dans votre pile de mana engagé"
    },
    "Bête de la griffe": {
        "color": "Verdant",
        "archetype": ["Bête"],
        "cost": 5,
        "atk": 4,
        "strike": 2,
        "pv": 6,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Combattant sauvage": {
        "color": "Verdant",
        "archetype": ["Bête"],
        "cost": 5,
        "atk": 5,
        "strike": 2,
        "pv": 4,
        "effect": ["overkill"],
        "description": "Overkill : strike 1"
    },
    "Gardienne des bois": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 6,
        "atk": 5,
        "strike": 1,
        "pv": 6,
        "effect": ["on_inv_target"],
        "description": "Apparition : donnez +2/0/2 à un Elf allié"
    },
    "Ancien de la foret": {
        "color": "Verdant",
        "archetype": [],
        "cost": 6,
        "atk": 6,
        "strike": 1,
        "pv": 6,
        "effect": ["action"],
        "description": "Action : Bénédiction 2 ou piochez 2 cartes"
    },
    "Bastiosaure": {
        "color": "Verdant",
        "archetype": ["Dinosaure"],
        "cost": 7,
        "atk": 6,
        "strike": 4,
        "pv": 6,
        "effect": [],
        "description": ""
    },
    "Drake emeraude": {
        "color": "Verdant",
        "archetype": ["Dragon"],
        "cost": 7,
        "atk": 6,
        "strike": 2,
        "pv": 7,
        "effect": ["overkill"],
        "description": "Overkill : Bénédiction 2"
    },
    "Protecteur runique": {
        "color": "Verdant",
        "archetype": [],
        "cost": 8,
        "atk": 6,
        "strike": 2,
        "pv": 6,
        "effect": ["on_inv"],
        "description": "Apparition : gagnez 5 armure"
    },
    "Archidruide": {
        "color": "Verdant",
        "archetype": ["Elf"],
        "cost": 8,
        "atk": 5,
        "strike": 2,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Apparition : invoquez 2 Tréant"
    },
    "Maitresse de la ménagerie": {
        "color": "Verdant",
        "archetype": [],
        "cost": 7,
        "atk": 4,
        "strike": 1,
        "pv": 4,
        "effect": ["on_inv"],
        "description": "Apparition : appelez une Bête de max 4 mana"
    },
    "Boucanier": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 1,
        "atk": 2,
        "strike": 0,
        "pv": 1,
        "effect": ["on_inv"],
        "description": "Apparition : donnez +1 Atk à ce combattant si vous controlez un autre Pirate"
    },
    "Matelot des mers": {
        "color": "Pourpre",
        "archetype": ["Pirate"],
        "cost": 1,
        "atk": 0,
        "strike": 2,
        "pv": 1,
        "effect": [],
        "description": "Ne peut etre actioné que si vous vous controlez un autre Pirate"
    },
    "Forban": {
        "color": "Pourpre",
        "archetype": ["Pirate"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : réduisez la durabilité de l'Artefact adverse de 1"
    },
    "Vigie pirate": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : ajoutez un Crochet à votre main"
    },
    "Capitaine pirate": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["action"],
        "description": "Action : donnez +1/1/1 à vos autres Pirates"
    },
    "Corsaire furtif": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 3,
        "atk": 4,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : retirez 2 armure à l'adversaire"
    },
    "Manieur de sabre": {
        "color": "Pourpre",
        "archetype": ["Pirate"],
        "cost": 4,
        "atk": 4,
        "strike": 2,
        "pv": 2,
        "effect": ["on_inv_target"],
        "description": "Apparition : si vous controlez un autre Pirate, infligez 2 dégats"
    },
    "Face de poulpe": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 4,
        "atk": 4,
        "strike": 1,
        "pv": 4,
        "effect": ["on_inv_target"],
        "description": "Apparition : donnez +1 Strike à un Pirate"
    },
    "Brigande du navire": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 2,
        "atk": 1,
        "strike": 2,
        "pv": 1,
        "effect": [],
        "description": "Coute 1 de moins si vous controlez 2 autres Pirates"
    },
    "Capitaine double crochet": {
        "color": "Azur",
        "archetype": ["Pirate"],
        "cost": 5,
        "atk": 4,
        "strike": 2,
        "pv": 5,
        "effect": ["on_inv_target"],
        "description": "Apparition : engagez tous les combattants adverses"
    },
    "Jeteur d'encre": {
        "color": "Pourpre",
        "archetype": ["Pirate"],
        "cost": 5,
        "atk": 6,
        "strike": 1,
        "pv": 5,
        "effect": ["overkill"],
        "description": "Overkill : appelez un pirate à 1 mana"
    },

    "Explorateur téméraire": {
        "color": "Ocre",
        "archetype": [],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : si vous controlez un Enchantement, piochez une carte"
    },
    "Zapomatic": {
        "color": "Ocre",
        "archetype": ["Méca"],
        "cost": 3,
        "atk": 2,
        "strike": 2,
        "pv": 2,
        "effect": ["rapide"],
        "description": "Frappe rapide"
    },
    "Élémentaire de poussière": {
        "color": "Ocre",
        "archetype": ["Élémentaire"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["action"],
        "description": "Action : infligez 1 dégats à tous les combattants adverses"
    },
    "Dragon d'argent": {
        "color": "Ocre",
        "archetype": ["Dragon"],
        "cost": 5,
        "atk": 5,
        "strike": 2,
        "pv": 5,
        "effect": [],
        "description": ""
    },
    "Lion du désert": {
        "color": "Ocre",
        "archetype": ["Bête"],
        "cost": 6,
        "atk": 6,
        "strike": 2,
        "pv": 4,
        "effect": ["bouclier"],
        "description": "Bouclier divin"
    },
    "Murozong": {
        "color": "Ocre",
        "archetype": ["Dragon"],
        "cost": 8,
        "atk": 6,
        "strike": 1,
        "pv": 6,
        "effect": ["on_inv"],
        "description": "Apparition : votre héros est insensible au prochain tour adverse"
    },
    "Grand dragon d'or": {
        "color": "Ocre",
        "archetype": ["Dragon"],
        "cost": 8,
        "atk": 8,
        "strike": 3,
        "pv": 8,
        "effect": [],
        "description": ""
    },
    "Garde lumière": {
        "color": "Ocre",
        "archetype": [],
        "cost": 6,
        "atk": 5,
        "strike": 2,
        "pv": 5,
        "effect": ["on_inv_target"],
        "description": "Apparition : soignez un allié de 2 et donnez lui 2 PV"
    },
    "Roi de Fondor": {
        "color": "Ocre",
        "archetype": [],
        "cost": 7,
        "atk": 4,
        "strike": 2,
        "pv": 6,
        "effect": ["on_inv"],
        "description": "Apparition : strike 5 sur votre héros puis donnez lui 10 armure"
    },
    "Géode lumineuse": {
        "color": "Ocre",
        "archetype": ["Élémentaire"],
        "cost": 2,
        "atk": 2,
        "strike": 0,
        "pv": 3,
        "effect": ["action"],
        "description": "Action : soignez un allié de 1"
    },
    "Prêtresse corrompue": {
        "color": "Ocre",
        "archetype": [],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 5,
        "effect": ["on_soin"],
        "description": "Lorsque ce combattant est soigné, infligez 1 dégat à tous les combattants adverses"
    },
    "Clerc du royaume": {
        "color": "Ocre",
        "archetype": [],
        "cost": 3,
        "atk": 2,
        "strike": 1,
        "pv": 4,
        "effect": ["on_soin"],
        "description": "Lorsque ce combattant est soigné, donnez lui +2 Atk"
    },
    "Dragon cactus": {
        "color": "Ocre",
        "archetype": ["Dragon"],
        "cost": 4,
        "atk": 4,
        "strike": 1,
        "pv": 4,
        "effect": ["on_mort"],
        "description": "Dernier Souffle : strike 1"
    },
    "Grande prêtresse Ninlil": {
        "color": "Ocre",
        "archetype": [],
        "cost": 7,
        "atk": 4,
        "strike": 2,
        "pv": 7,
        "effect": ["on_inv", "action"],
        "description": "Apparition : soignez tous vos combattants de 2. Action : Bénédiction 2"
    },
    "Alchimiste des étoiles": {
        "color": "Verdant",
        "archetype": [],
        "cost": 5,
        "atk": 4,
        "strike": 1,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Inspiration : ajoutez une Comète à votre main"
    },
    "Malygos": {
        "color": "Verdant",
        "archetype": ["Dragon"],
        "cost": 6,
        "atk": 3,
        "strike": 2,
        "pv": 6,
        "effect": [],
        "description": "Vos Comète strikent 3"
    },
    "Pillard gobelin": {
        "color": "Pourpre",
        "archetype": [],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : piochez une carte"
    },
    "Gobelin effrayé": {
        "color": "Pourpre",
        "archetype": [],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 3,
        "effect": [],
        "description": "Vous ne pouvez pas mettre cette carte en mode blocage"
    },
    "Sisu, gardienne céleste": {
        "color": "Pourpre",
        "archetype": ["Dragon"],
        "cost": 7,
        "atk": 5,
        "strike": 1,
        "pv": 5,
        "effect": ["on_inv_target"],
        "description": "Apparition : détruisez un combattant adverse"
    },
    "Commandant du désert": {
        "color": "Ocre",
        "archetype": [],
        "cost": 3,
        "atk": 2,
        "strike": 1,
        "pv": 3,
        "effect": ["aura", "on_inv"],
        "description": "Apparition : invoquez une recrue. Vos recrues ont +1 Atk"
    },
    "Bricoleur": {
        "color": "Azur",
        "archetype": [],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 2,
        "effect": ["on_inv_target"],
        "description": "Apparition : piochez un Méca"
    },
    "Robot barbier": {
        "color": "Azur",
        "archetype": ["Méca", "Pirate"],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 1,
        "effect": ["on_inv_target"],
        "description": "Apparition : donnez +1 Strike à un Méca ou un Pirate"
    },
    "Apprenti sorcier": {
        "color": "Turquoise",
        "archetype": ["Mage"],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 1,
        "effect": ["puissance"],
        "description": "Puissance"
    },
    "Archimage Antonidas": {
        "color": "Turquoise",
        "archetype": ["Mage"],
        "cost": 5,
        "atk": 4,
        "strike": 1,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Apparition : placez 2 Torches dans votre deck"
    },
    "Éclat glaciaire": {
        "color": "Turquoise",
        "archetype": ["Élémentaire"],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 1,
        "effect": ["on_inv_target"],
        "description": "Apparition : paralysez un combattant engagé"
    },
    "Troll des neiges": {
        "color": "Turquoise",
        "archetype": [],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 4,
        "effect": ["on_inv_target"],
        "description": "Apparition : paralysez un combattant"
    },
    "Sindragosa": {
        "color": "Turquoise",
        "archetype": ["Dragon"],
        "cost": 3,
        "atk": 3,
        "strike": 0,
        "pv": 3,
        "effect": ["on_inv_target"],
        "description": "Apparition : paralysez un combattant. S'il est déjà paralysé, détruisez le"
    },
    "Colosse rocheux": {
        "color": "Turquoise",
        "archetype": ["Élémentaire"],
        "cost": 6,
        "atk": 5,
        "strike": 2,
        "pv": 7,
        "effect": ["on_inv"],
        "description": "Surcharge 1"
    },
    "Lancier du palais": {
        "color": "Turquoise",
        "archetype": [],
        "cost": 2,
        "atk": 2,
        "strike": 1,
        "pv": 3,
        "effect": [],
        "description": ""
    },
    "Dragon astral": {
        "color": "Turquoise",
        "archetype": ["Dragon"],
        "cost": 5,
        "atk": 3,
        "strike": 1,
        "pv": 6,
        "effect": ["on_inv"],
        "description": "Apparition : piochez 2 cartes"
    },
    "Kodo du désert": {
        "color": "Turquoise",
        "archetype": ["Bête"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 1,
        "effect": ["on_inv"],
        "description": "Apparition : donnez +1/1/1 aux Bête dans votre main"
    },
    "Kodo de livraison": {
        "color": "Turquoise",
        "archetype": ["Bête"],
        "cost": 3,
        "atk": 2,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : piochez une Bête, réduisez son cout en mana de 1"
    },
    "Kodo de pierre": {
        "color": "Turquoise",
        "archetype": ["Bête"],
        "cost": 4,
        "atk": 2,
        "strike": 1,
        "pv": 7,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Fabriquant d'armure": {
        "color": "Turquoise",
        "archetype": [],
        "cost": 4,
        "atk": 4,
        "strike": 1,
        "pv": 4,
        "effect": ["action"],
        "description": "Action : gagnez 2 armure"
    },
    "Hacheur Nimbos": {
        "color": "Turquoise",
        "archetype": ["Nain"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 2,
        "effect": ["on_mort"],
        "description": "Dernier souffle : gagnez 2 armure"
    },
    "Explomage gobelin": {
        "color": "Turquoise",
        "archetype": [],
        "cost": 6,
        "atk": 5,
        "strike": 2,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : infligez 6 dégats répartis aléatoirement entre les combattants ennemis"
    },
    "Esprit de l'air": {
        "color": "Zéphyr",
        "archetype": [],
        "cost": 0,
        "atk": 1,
        "strike": 0,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Moustique mutant": {
        "color": "Zéphyr",
        "archetype": ["Bête"],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 1,
        "effect": ["toxique"],
        "description": "Toxique"
    },
    "Garuda": {
        "color": "Zéphyr",
        "archetype": ["Bête"],
        "cost": 7,
        "atk": 5,
        "strike": 2,
        "pv": 4,
        "effect": ["on_mort"],
        "description": "Dernier souffle : invoquez 2 Vautours"
    },
    "Satyre du bois sombre": {
        "color": "Zéphyr",
        "archetype": [],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : piochez un combattant à 1 mana"
    },
    "Chasseresse vorace": {
        "color": "Zéphyr",
        "archetype": [],
        "cost": 4,
        "atk": 2,
        "strike": 1,
        "pv": 4,
        "effect": ["on_inv"],
        "description": "Apparition : si vous avez moins de point que l'adversaire, infligez 2 dégats à tous les combattants adverses"
    },
    "Hibou nocturne": {
        "color": "Zéphyr",
        "archetype": ["Bête"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv_target"],
        "description": "Apparition : réduisez au silence un combattant"
    },
    "Élise": {
        "color": "Zéphyr",
        "archetype": [],
        "cost": 3,
        "atk": 2,
        "strike": 2,
        "pv": 3,
        "effect": ["action"],
        "description": "Action : invoquez une Araignée"
    },
    "Élémentaire grondant": {
        "color": "Zéphyr",
        "archetype": ["Élémentaire"],
        "cost": 4,
        "atk": 4,
        "strike": 2,
        "pv": 4,
        "effect": [],
        "description": ""
    },
    "Automate en bronze": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 4,
        "effect": [],
        "description": ""
    },
    "Minibot": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 1,
        "effect": ["on_mort"],
        "description": "Dernier souffle: invoquez un Microbot"
    },
    "Robot artificié": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : infligez 2 dégats répartis aléatoirement entre les combattants ennemis"
    },
    "Méca téléporteur": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 4,
        "atk": 2,
        "strike": 1,
        "pv": 4,
        "effect": ["on_inv"],
        "description": "Apparition : réduissez le cout des Méca de votre main de 1"
    },
    "Hydre mécanique": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 7,
        "atk": 6,
        "strike": 1,
        "pv": 6,
        "effect": ["overkill"],
        "description": "Overkill : redressez ce combattant"
    },
    "Rover de sécurité": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 5,
        "atk": 4,
        "strike": 1,
        "pv": 5,
        "effect": ["on_atk"],
        "description": "Lorsque ce combattant attaque, invoquez un Microbot"
    },
    "Explomatic": {
        "color": "Azur",
        "archetype": ["Méca"],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 4,
        "effect": ["action"],
        "description": "Action : infligez 4 dégats répartis aléatoirement entre les combattants ennemis"
    },

    "Serviteur de Caor": {
        "color": "Pourpre",
        "archetype": ["Démon", "Diablotin"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 3,
        "effect": ["on_inv"],
        "description": "Apparition : si vous controlez un démon, piochez un sort"
    },
    "Caor, roi des enfers": {
        "color": "Pourpre",
        "archetype": ["Démon"],
        "cost": 6,
        "atk": 6,
        "strike": 2,
        "pv": 4,
        "effect": ["trigger"],
        "description": "Lorsque vous jouez un sort, Strike 1"
    },
    "enragé de magma": {
        "color": "Pourpre",
        "archetype": ["Démon"],
        "cost": 4,
        "atk": 5,
        "strike": 2,
        "pv": 2,
        "effect": ["puissance"],
        "description": "Puissance"
    },
    "Destrier funeste": {
        "color": "Pourpre",
        "archetype": ["Démon"],
        "cost": 3,
        "atk": 1,
        "strike": 1,
        "pv": 3,
        "effect": ["soutien", "end_turn"],
        "description": "Soutien. A la fin de votre tour, redressez ce combattant"
    },
    "Garde infernal": {
        "color": "Pourpre",
        "archetype": ["Démon"],
        "cost": 6,
        "atk": 5,
        "strike": 2,
        "pv": 6,
        "effect": ["on_inv"],
        "description": "Apparition : Strike 1 sur les 2 joueurs"
    },
    "Homoncule nonchalent": {
        "color": "Pourpre",
        "archetype": ["Démon"],
        "cost": 5,
        "atk": 5,
        "strike": 3,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Apparition : engagez ce combattant"
    },
    "Diablotin des abimes": {
        "color": "Zéphyr",
        "archetype": ["Démon", "Diablotin"],
        "cost": 1,
        "atk": 2,
        "strike": 1,
        "pv": 2,
        "effect": ["on_inv"],
        "description": "Apparition : strike 2 sur votre héros"
    },
    "Diablotin de service": {
        "color": "Zéphyr",
        "archetype": ["Démon", "Diablotin"],
        "cost": 2,
        "atk": 3,
        "strike": 1,
        "pv": 1,
        "effect": ["soutien"],
        "description": "Soutien (Démon)"
    },
    "Maitresse succube": {
        "color": "Zéphyr",
        "archetype": ["Démon"],
        "cost": 3,
        "atk": 1,
        "strike": 2,
        "pv": 4,
        "effect": ["trigger"],
        "description": "Lorsque vous subissez des strikes pendant votre tour, Bénédiction 1"
    },
    "Seigneur des abimes": {
        "color": "Zéphyr",
        "archetype": ["Démon"],
        "cost": 4,
        "atk": 5,
        "strike": 2,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Apparition : strike 4 sur votre héros"
    },
    "Pazuzu": {
        "color": "Zéphyr",
        "archetype": ["Démon"],
        "cost": 5,
        "atk": 3,
        "strike": 2,
        "pv": 4,
        "effect": ["rapide", "overkill"],
        "description": "Frappe rapide. Overkill : Bénédiction 1"
    },
    "Mortamor": {
        "color": "Zéphyr",
        "archetype": ["Démon"],
        "cost": 6,
        "atk": 5,
        "strike": 2,
        "pv": 5,
        "effect": ["end_turn"],
        "description": "A la fin du tour, défaussez une carte dans la main adverse"
    },
    "Marcheur du vide": {
        "color": "Nébuleux",
        "archetype": ["Démon", "Diablotin"],
        "cost": 1,
        "atk": 1,
        "strike": 0,
        "pv": 3,
        "effect": ["protecteur"],
        "description": "Protecteur"
    },
    "Diablotin ardent": {
        "color": "Nébuleux",
        "archetype": ["Démon", "Diablotin"],
        "cost": 1,
        "atk": 2,
        "strike": 1,
        "pv": 1,
        "effect": ["on_inv"],
        "description": "Apparition : défaussez une carte"
    },
    "Démon inférieur": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 2,
        "atk": 3,
        "strike": 0,
        "pv": 3,
        "effect": [],
        "description": ""
    },
    "Diablotin sournois": {
        "color": "Nébuleux",
        "archetype": ["Démon", "Diablotin"],
        "cost": 2,
        "atk": 2,
        "strike": 2,
        "pv": 2,
        "effect": ["enfoui"],
        "description": "Enfoui"
    },
    "Diablotin des bois": {
        "color": "Nébuleux",
        "archetype": ["Démon", "Diablotin"],
        "cost": 2,
        "atk": 1,
        "strike": 1,
        "pv": 2,
        "effect": ["trigger"],
        "description": "Lorsque vous défaussez une carte, piochez une carte"
    },
    "Saccagueur démoniaque": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 3,
        "atk": 3,
        "strike": 1,
        "pv": 5,
        "effect": ["on_inv"],
        "description": "Apparition : envoyez une carte de votre pile de mana dans votre défausse"
    },
    "Chef de gang des diablotins": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 3,
        "atk": 2,
        "strike": 1,
        "pv": 3,
        "effect": ["on_mort"],
        "description": "Dernier Souffle : invoquez un Diablotin depuis votre main"
    },
    "Invocateur du vide": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 4,
        "atk": 3,
        "strike": 1,
        "pv": 4,
        "effect": ["action"],
        "description": "Action : invoquez un Diablotin depuis votre défausse"
    },
    "Terreur du vide": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 5,
        "atk": 4,
        "strike": 1,
        "pv": 5,
        "effect": ["on_strike"],
        "description": "Lorsqu'il strike, inflige 1 dégat à tous les combattants adverses"
    },
    "Dévoreur effroyable": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 4,
        "atk": 3,
        "strike": 3,
        "pv": 4,
        "effect": ["on_strike"],
        "description": "Lorsqu'il strike, défaussez une carte"
    },
    "Seigneur déchainé des enfers": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 6,
        "atk": 6,
        "strike": 3,
        "pv": 5,
        "effect": ["aura", "on_inv"],
        "description": "Vos autres Démons ont +2/1/2. Apparition : envoyez 2 cartes de votre pile de mana dans votre défausse."
    },
    "Empereur du vide": {
        "color": "Nébuleux",
        "archetype": ["Démon"],
        "cost": 7,
        "atk": 3,
        "strike": 1,
        "pv": 8,
        "effect": ["protecteur", "on_mort"],
        "description": "Protecteur. Dernier souffle : invoquez 2 Marcheur du vide"
    },

}


   