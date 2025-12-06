

card_set = {
    "Harponneuse": {
        "type": "structure",
        "classe": "Kraken",
        "archetype": "tourelle",
        "cost": 3,
        "pv": 3,
        "row": "front",
        "effect": ["end turn"],
        "description": "fin de tour: inflige 3 dégats à un adversaire aléatoire en front line"
    },
    "Foreuse": {
        "type": "structure",
        "classe": "Kraken",
        "archetype": "tourelle",
        "cost": 3,
        "pv": 3,
        "row": "back",
        "effect": ["end turn"],
        "description": "fin de tour: inflige 2 dégats à l'avatar adverse"
    },
    "Gardienne": {
        "type": "structure",
        "classe": "Kraken",
        "archetype": "tourelle",
        "cost": 3,
        "pv": 3,
        "row": "front",
        "effect": ["end turn"],
        "description": "fin de tour: soigne de 1 vos combattants en front line"
    },
    "Bathyscaphe": {
        "type": "structure",
        "classe": "Kraken",
        "archetype": "tourelle",
        "cost": 3,
        "pv": 3,
        "row": "back",
        "effect": ["end turn"],
        "description": "fin de tour: donne 2 armure à votre avatar"
    },
    "Tactirelle": {
        "type": "structure",
        "classe": "Kraken",
        "archetype": "tourelle",
        "cost": 3,
        "pv": 3,
        "row": "front",
        "effect": ["start turn"],
        "description": "début de tour: repousse un combattant adverse aléatoire en back line"
    },
    "Chalutier": {
        "type": "structure",
        "classe": "Kraken",
        "archetype": "tourelle",
        "cost": 3,
        "pv": 3,
        "row": "back",
        "effect": ["start turn"],
        "description": "début de tour: pioche 1 carte"
    },

    # FIGHTER
    "Papillon enchanté": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 1,
        "effect": ["inv_ennemy"],
        "description": "inv: silence 1 combattant"
    },
    "Lutin des bois": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "elf",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: pioche 1 sort"
    },
    "Golem ancien": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 4,
        "atk": 4,
        "pv": 5,
        "effect": [],
        "description": ""
    },
    "Satyre mystique": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "elf",
        "cost": 4,
        "atk": 2,
        "pv": 4,
        "effect": ["inv"],
        "description": "inv: réduit le cout du premier sort de votre main de 1"
    },
    "Druide de la griffe": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "elf",
        "cost": 5,
        "atk": 4,
        "pv": 6,
        "effect": ["protecteur"],
        "description": "protecteur"
    },
    "Drake émeraude": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "célestial",
        "cost": 6,
        "atk": 5,
        "pv": 7,
        "effect": ["puissance"],
        "description": "puissance"
    },
    "Gardien des bois": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "elf",
        "cost": 6,
        "atk": 5,
        "pv": 5,
        "effect": ["inv_ally"],
        "description": "inv: donne +2/+2 à un elf allié"
    },
    "Bastiosaure": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "bête",
        "cost": 7,
        "atk": 6,
        "pv": 6,
        "effect": ["charge"],
        "description": "charge"
    },
    "Archidruide": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "elf",
        "cost": 7,
        "atk": 6,
        "pv": 6,
        "effect": ["front"],
        "description": "front: invoque 2 tréants"
    },
    "Ancien de la forêt": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "elf",
        "cost": 8,
        "atk": 5,
        "pv": 8,
        "effect": ["front", "end turn"],
        "description": "front: pioche 1 carte, end turn: soigne 3 pv à votre avatar"
    },
    "Éclat glaciaire": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "élémentaire",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["inv_ennemy"],
        "description": "inv: paralyse un adversaire en frontline"
    },
    "Apprenti sorcier": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "mage",
        "cost": 1,
        "atk": 1,
        "pv": 2,
        "effect": ["puissance"],
        "description": "puissance"
    },
    "Lancier": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 3,
        "effect": [],
        "description": ""
    },
    "Friselame": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["inv_ennemy"],
        "description": "inv: paralyse un advsersaire. s'il est déja paralysé, détruit le"
    },
    "Hacheur nain": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 2,
        "effect": ["mort"],
        "description": "mort: gagne 2 armure"
    },
    "Troll des neiges": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 4,
        "atk": 3,
        "pv": 4,
        "effect": ["inv_ennemy"],
        "description": "inv: paralyse un advsersaire"
    },
    "Griffon": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "bête",
        "cost": 4,
        "atk": 2,
        "pv": 4,
        "effect": ["insaisissable"],
        "description": "insaisissable"
    },
    "Antonidas": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "mage",
        "cost": 5,
        "atk": 3,
        "pv": 5,
        "effect": ["puissance", "inv"],
        "description": "puissance, inv: place 2 torche dans ton deck"
    },
    "Colosse rocheux": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "élémentaire",
        "cost": 7,
        "atk": 7,
        "pv": 7,
        "effect": ["protecteur"],
        "description": "protecteur"
    },
    "Écuyer": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 2,
        "effect": ["avant-garde"],
        "description": "avant-garde"
    },
    "Archer d'élite": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 1,
        "effect": ["inv_ennemy"],
        "description": "inv: inflige 2 dégats à une unité"
    },
    "Robot blindé": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "méca",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["bouclier"],
        "description": "bouclier"
    },
    "Aventurier": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: si offrande Enlil>=2, pioche 1 carte"
    },
    "Entraineur": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 2,
        "atk": 1,
        "pv": 1,
        "effect": ["front"],
        "description": "donne +1/+0 aux combattants alliés en frontline"
    },
    "Milicien antique": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 2,
        "effect": ["bouclier"],
        "description": "bouclier"
    },
    "Sentinelle": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 3,
        "atk": 1,
        "pv": 5,
        "effect": ["avant-garde"],
        "description": "avant-garde"
    },
    "Silencieux": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 4,
        "atk": 4,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: silence la frontline adverse"
    },
    "Roi de Fondor": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 4,
        "atk": 3,
        "pv": 4,
        "effect": ["inv"],
        "description": "inv: inflige 4 dégats à ton avatar et lui donne 8 d'armure"
    },
    "Garde lumière": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 5,
        "atk": 5,
        "pv": 3,
        "effect": ["bouclier"],
        "description": "bouclier"
    },
    "Gnome Maléfique": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: défausse la premiere carte du deck adverse"
    },
    "Albatros": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 2,
        "atk": 3,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: les 2 joueurs piochent 1 carte"
    },
    "Démon inférieur": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 2,
        "atk": 3,
        "pv": 2,
        "effect": [],
        "description": ""
    },
    "Chat noir": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["puissance"],
        "description": "puissance"
    },
    "Corbeau pourpre": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["mort"],
        "description": "mort: pioche 1 sort"
    },
    "Destrier de la mort": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 3,
        "atk": 2,
        "pv": 1,
        "effect": ["charge", "mort"],
        "description": "charge, mort: donne +1/+1 à un allié aléatoire en frontline"
    },
    "Ombre cosmique": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "célestial",
        "cost": 4,
        "atk": 2,
        "pv": 2,
        "effect": ["mort"],
        "description": "mort: offrande"
    },
    "Invocateur du vide": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 4,
        "atk": 3,
        "pv": 4,
        "effect": ["inv"],
        "description": "inv: invoque un démon aléatoire à max 2 mana mort pendant cette partie"
    },
    "Archer elf": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "elf",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["inv_ennemy"],
        "description": "inv: inflige 1 dégat à une unité"
    },
    "Tofu": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "tofu",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["rapide"],
        "description": "frappe rapide"
    },
    "Diablotin des abimes": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "démon",
        "cost": 1,
        "atk": 2,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: inflige 2 dégats à ton avatar"
    },
    "Tofu mélanique": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "tofu",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["insaisissable"],
        "description": "insaisissable"
    },
    "Bouftou noir": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "bête",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["robuste"],
        "description": "robuste"
    },
    "Boufmouth": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "bête",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["end turn"],
        "description": "fin tour : soigne 1 PV à un allié aléatoire en frontline"
    },
    "Rampante": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "",
        "cost": 2,
        "atk": 1,
        "pv": 2,
        "effect": ["mort"],
        "description": "mort: invoque 2 araignée"
    },
    "Tofu royal": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "tofu",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["attaque"],
        "description": "après qu'il ait attaqué, revient en backline"
    },
    "Bouftou blanc": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "bête",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["protecteur"],
        "description": "protecteur"
    },
    "Élise": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "",
        "cost": 3,
        "atk": 2,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: invoque 2 araignée"
    },
    "Tofu ventripotent": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "tofu",
        "cost": 4,
        "atk": 4,
        "pv": 3,
        "effect": ["front"],
        "description": "front: repousse un adversaire en backline"
    },
    "Bouftou de guerre": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "bête",
        "cost": 4,
        "atk": 2,
        "pv": 5,
        "effect": ["inv_ally"],
        "description": "inv : donne charge à un allié"
    },
    "Seigneur des abimes": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "démon",
        "cost": 4,
        "atk": 5,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: inflige 4 dégats à ton avatar"
    },
    "Bouftou primitif": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "bête",
        "cost": 5,
        "atk": 3,
        "pv": 4,
        "effect": ["inv_ennemy"],
        "description": "inv : inflige 2 dmg à un combattant"
    },
    "Ereshkigal": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "démon",
        "cost": 5,
        "atk": 4,
        "pv": 4,
        "effect": ["inv"],
        "description": "inv: donne +2/+2 aux démons alliés"
    },
    "Terreur du vide": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "démon",
        "cost": 6,
        "atk": 5,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: inflige 1 dégats à toutes les unités adverses"
    },
    "Boucanier": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "pirate",
        "cost": 1,
        "atk": 1,
        "pv": 2,
        "effect": [],
        "description": ""
    },
    "Bricoleur": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 2,
        "atk": 1,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: pioche 1 carte"
    },
    "Vigie pirate": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "pirate",
        "cost": 2,
        "atk": 1,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: ajoute un crochet à votre main"
    },
    "Canon du navire": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 3,
        "effect": ["end turn"],
        "description": "fin tour: si vous controlez un pirate, infligez 1 dégat à l'adv"
    },
    "Capitaine pirate": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "pirate",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["front"],
        "description": "donne +1/+1 à un pirate allié"
    },
    "Flibustier": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "pirate",
        "cost": 4,
        "atk": 3,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: pioche 1 pirate"
    },
    "Capitaine Krag": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "pirate",
        "cost": 5,
        "atk": 3,
        "pv": 6,
        "effect": ["charge"],
        "description": "charge"
    },
    "Porcass": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["charge"],
        "description": "charge"
    },
    "Marcheur du vide": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "démon",
        "cost": 1,
        "atk": 1,
        "pv": 2,
        "effect": ["protecteur"],
        "description": "protecteur"
    },
    "Gobelin infecté": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "",
        "cost": 1,
        "atk": 2,
        "pv": 1,
        "effect": ["mort"],
        "description": "mort: inflige 1 dégat à l'avatar adverse"
    },
    "Matelot": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "pirate",
        "cost": 1,
        "atk": 2,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: gagne charge si vous controlez un autre pirate"
    },
    "Sergent Cruel": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["inv_ally"],
        "description": "inv: inflige 1 dégats à un combattant allié et lui donne 2 atk"
    },
    "Berger porcass": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "porcass",
        "cost": 2,
        "atk": 2,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: invoque un porcass 1/1 avec charge"
    },
    "Corsaire furtif": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "pirate",
        "cost": 2,
        "atk": 3,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: retire 1 armure à l'adversaire"
    },
    "Chevaucheur de porcass": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "porcass",
        "cost": 3,
        "atk": 3,
        "pv": 1,
        "effect": ["charge"],
        "description": "charge"
    },
    "Maitre blessé": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "",
        "cost": 3,
        "atk": 4,
        "pv": 6,
        "effect": ["inv"],
        "description": "inv: s'inflige 4 dégats"
    },
    "Chargeur orc": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "orc",
        "cost": 4,
        "atk": 4,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: si votre main est vide, piochez 3 cartes"
    },
    "Berserker porcass": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "porcass",
        "cost": 4,
        "atk": 3,
        "pv": 4,
        "effect": ["end turn"],
        "description": "fin de tour: blessé: gagne 2 atk"
    },
    "Manieur de sabre": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "pirate",
        "cost": 4,
        "atk": 4,
        "pv": 2,
        "effect": ["inv_ennemy"],
        "description": "inv: si vous controlez un pirate, infligez 2 dégats à un combattant"
    },
    "Le Découpeur": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "orc",
        "cost": 5,
        "atk": 4,
        "pv": 6,
        "effect": ["robuste"],
        "description": "robuste"
    },
    "Ogre glouton": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "orc",
        "cost": 6,
        "atk": 6,
        "pv": 6,
        "effect": ["percant"],
        "description": "dégats percants"
    },
    "Archer squelette": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 2,
        "atk": 3,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: inflige 1 dégat à l'avatar adverse"
    },
    "Spectre": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 2,
        "atk": 2,
        "pv": 1,
        "effect": ["mort"],
        "description": "mort: pioche 1 carte"
    },
    "Esprit déchainé": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 2,
        "atk": 4,
        "pv": 4,
        "effect": ["inv_ally"],
        "description": "nécessite 1 sacrifice"
    },
    "Sombre cultiste": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mage",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: soigne votre avatar de 3"
    },
    "Momie infestée": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 4,
        "atk": 2,
        "pv": 4,
        "effect": ["mort"],
        "description": "mort: invoque une goule 2/2"
    },
    "Chevalier spectral": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 5,
        "atk": 4,
        "pv": 6,
        "effect": [""],
        "description": ""
    },
    "Vampyro": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 7,
        "atk": 5,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: réduit le cout des cartes de ta main de 1"
    },  

    # à trier
    "Prêtresse corrompue": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 6,
        "atk": 4,
        "pv": 5,
        "effect": ["inv_ennemy"],
        "description": "inv: détruit un combattant adverse avec 2 atk ou moins"
    },
    "Robot de soin": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "méca",
        "cost": 4,
        "atk": 3,
        "pv": 4,
        "effect": ["inv", "inv_ally"],
        "description": "inv: soigne 3 (avatar ou allié)"
    },
    "Grande prêtresse de Ninlil": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 6,
        "atk": 4,
        "pv": 6,
        "effect": ["inv"],
        "description": "inv: soigne vos combattants de 2"
    },
    "Champion de Fondor": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 8,
        "atk": 5,
        "pv": 5,
        "effect": ["protecteur", "inv_ennemy"],
        "description": "protecteur. inv: détruit un combattant adverse"
    },
    "Chasseuse vorace": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "",
        "cost": 3,
        "atk": 2,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: rage: inflige 1 dégats à tous les ennemis"
    },
    "Drake ancestral": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "célestial",
        "cost": 8,
        "atk": 4,
        "pv": 8,
        "effect": ["end turn"],
        "description": "fin du tour: invoque un drake primitif"
    },
    "Gardien de la porte": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 4,
        "atk": 0,
        "pv": 6,
        "effect": ["avant-garde", "start turn"],
        "description": "avant-garde, début de tour: se soigne jusquà ses PV max"
    },
    "Combattant sauvage": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "bête",
        "cost": 4,
        "atk": 4,
        "pv": 4,
        "effect": ["attaque"],
        "description": "lorsqu'il attaque, inflige 1 dégats à l'avatar adverse"
    },
    "Chevalier gemme": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 4,
        "atk": 3,
        "pv": 3,
        "effect": ["bouclier", "percant"],
        "description": "bouclier, dégats percants"
    },
    "Bébé phorreur": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: renvoie la première carte de ta main dans ton deck puis pioche 1"
    },
    "Phorreur cuirassé": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 5,
        "atk": 5,
        "pv": 5,
        "effect": ["front"],
        "description": "front: donne 2 armure à ton avatar"
    },
    "Phorreur camouflé": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 4,
        "atk": 4,
        "pv": 3,
        "effect": ["rapide", "inv"],
        "description": "frappe rapide, surcharge"
    },
    "Garde tortue": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 3,
        "atk": 1,
        "pv": 4,
        "effect": ["protecteur", "inv_ally"],
        "description": "protecteur, inv: donne protecteur à un allié"
    },
    
    "Pazuzu": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "démon",
        "cost": 5,
        "atk": 3,
        "pv": 5,
        "effect": ["insaisissable", "vol de vie"],
        "description": "insaisissable, vol de vie"
    },
    "Diablotin ardent": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 1,
        "atk": 3,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: défaussez une carte aléatoire"
    },
    "Serviteur de Caor": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "démon",
        "cost": 2,
        "atk": 1,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: si vous controlez un démon, pioche 1 démon"
    },
    "Caor": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "démon",
        "cost": 6,
        "atk": 5,
        "pv": 5,
        "effect": ["puissance", "inv"],
        "description": "puissance, inv: réduit le cout des sorts de votre main de 1"
    },
    "Saccagueur démoniaque": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 3,
        "atk": 3,
        "pv": 5,
        "effect": ["protecteur", "inv"],
        "description": "protecteur, inv: détruit un cristal de mana"
    },
    "Maitresse succube": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "démon",
        "cost": 3,
        "atk": 2,
        "pv": 4,
        "effect": ["inv"],
        "description": "inv: rage: gagne vol de vie"
    },
    "Empereur du vide": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 5,
        "atk": 4,
        "pv": 5,
        "effect": ["avant-garde", "inv", "mort"],
        "description": "avant-garde, surcharge 2, mort: invoque 2 démon inférieur"
    },

    "Dragarde": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "célestial",
        "cost": 5,
        "atk": 3,
        "pv": 6,
        "effect": ["inv"],
        "description": "inv: pioche 1 carte"
    },
    "Mortamor": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "démon",
        "cost": 5,
        "atk": 4,
        "pv": 4,
        "effect": ["rapide"],
        "description": "frappe rapide"
    },
    "Tofukaz": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "tofu",
        "cost": 0,
        "atk": 1,
        "pv": 1,
        "effect": ["attaque"],
        "description": "se détruit lorsqu'il attaque"
    },
    "Berserkoffre": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["mort"],
        "description": "mort: ajoute une rune contrefaite à votre main"
    },
    "Acolyte de la souffrance": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "",
        "cost": 3,
        "atk": 1,
        "pv": 3,
        "effect": ["end turn"],
        "description": "fin de tour: blessé: pioche une carte"
    },
    "Rejeton de lumière": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 1,
        "atk": 2,
        "pv": 2,
        "effect": ["mort"],
        "description": "mort: soigne l'adversaire de 3"
    },
    "Pacificateur": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["front"],
        "description": "front: passe l'atk d'un adv a 1"
    },
    "Clown mystique": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["inv_ally", "inv_ennemy"],
        "description": "inv: inverse l'atk et les pv d'un combattant"
    },

    "Dévoreur des abysses": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "abyssal",
        "cost": 8,
        "atk": 6,
        "pv": 6,
        "effect": ["percant", "vol de vie"],
        "description": "dégats percant, vol de vie"
    },
    "Rampant des profondeurs": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "abyssal",
        "cost": 10,
        "atk": 6,
        "pv": 8,
        "effect": ["inv"],
        "description": "inv: réduit le cout des autres rampant des profondeurs de 2"
    },
    "Khalamar géant": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "abyssal",
        "cost": 9,
        "atk": 4,
        "pv": 8,
        "effect": ["inv"],
        "description": "inv: passent vos tentacules à 4/4"
    },
    "Oeil des abysses": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "abyssal",
        "cost": 5,
        "atk": 3,
        "pv": 3,
        "effect": ["insaisissable"],
        "description": "insaisissable"
    },
    "Pêcheur légendaire": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": ["inv"],
        "description": "inv: pioche 1 abyssal, réduit son cout de 1"
    },
    "Wyrm aquatique": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "abyssal",
        "cost": 6,
        "atk": 3,
        "pv": 6,
        "effect": ["inv"],
        "description": "inv: réduit le cout des abyssaux dans votre main de 1"
    },
    "Technomage": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 3,
        "atk": 2,
        "pv": 4,
        "effect": ["inv_ally"],
        "description": "inv: donne 1 durabilité à une structure"
    },
    "Maitre des rouages": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 2,
        "atk": 1,
        "pv": 3,
        "effect": ["front"],
        "description": "front: si vous controlez une tourelle, gagne +2/+0"
    },
    "Automate en bronze": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "méca",
        "cost": 3,
        "atk": 3,
        "pv": 4,
        "effect": [""],
        "description": ""
    },

    "Luminotron": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "méca",
        "cost": 1,
        "atk": 1,
        "pv": 2,
        "effect": ["magnétisme"],
        "description": "magnétisme"
    },
    "Minibot": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "méca",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["mort"],
        "description": "mort: invoque un méca 1/1"
    },
    "Robot artificié": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "méca",
        "cost": 2,
        "atk": 2,
        "pv": 1,
        "effect": ["inv"],
        "description": "inv: inflige 1 dmg sur un adv aléatoire"
    },
    "Méca téléporteur": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "méca",
        "cost": 4,
        "atk": 2,
        "pv": 4,
        "effect": ["end turn"],
        "description": "fin de tour : invoque un méca 1/1"
    },
    "Engin de guerre": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "méca",
        "cost": 6,
        "atk": 5,
        "pv": 5,
        "effect": ["magnétisme"],
        "description": "magnétisme"
    },
    "Ziliax": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "méca",
        "cost": 5,
        "atk": 3,
        "pv": 2,
        "effect": ["magnétisme", "bouclier", "vol de vie"],
        "description": "magnétisme, bouclier, vol de vie"
    },

    "Flammetin": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "élémentaire",
        "cost": 1,
        "atk": 1,
        "pv": 2,
        "effect": ["inv"],
        "description": "inv: ajoute un élémentaire de flamme à votre main"
    },
    "Élémentaire de lave": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "élémentaire",
        "cost": 5,
        "atk": 5,
        "pv": 5,
        "effect": ["start turn"],
        "description": "start turn: inflige 1 dégats aux 2 avatars"
    },
    "Malygos": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "célestial",
        "cost": 8,
        "atk": 6,
        "pv": 8,
        "effect": ["inv"],
        "description": "inv: donne puissance à ton avatar jusqu'à la fin du combat"
    },
    "Pyrus": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "élémentaire",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": ["mort"],
        "description": "mort: place Pyrus 2 dans votre deck"
    },
    "Requin marteau": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 5,
        "atk": 4,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: place un gros boulet dans la main de l'adversaire"
    },
    "Prêtresse maléfique": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 4,
        "atk": 3,
        "pv": 5,
        "effect": ["soin"],
        "description": "soigné : inflige 1 dégats à toutes les unités adverses"
    },
    "Horreb": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 6,
        "atk": 5,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: les cartes dans la main adverse coutent 1 de plus"
    },
    "Gobelin à sarbacane": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": ["end turn"],
        "description": "fin de tour : ajoute une Infection dans le deck adverse"
    },
    "Sylvenier": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 3,
        "atk": 2,
        "pv": 3,
        "effect": ["inv"],
        "description": "inspiration : donne 1 cristal de mana vide"
    },
    "Maitre vaudou": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 5,
        "atk": 5,
        "pv": 4,
        "effect": ["inv"],
        "description": "inv: ajoute une Infection dans le deck adverse, inspiration : 2 Infection"
    },
    "Kin gael": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 6,
        "atk": 6,
        "pv": 5,
        "effect": ["inv"],
        "description": "inv: pour le reste de la partie, les Infections adverses coutent 2"
    },
    "Protecteur runique": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 9,
        "atk": 8,
        "pv": 8,
        "effect": ["inv"],
        "description": "inv: donne 8 armure"
    },

    ## INVOC
    "Araignée": {
        "type": "fighter",
        "classe": "Ishtar",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Recrue": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Tentacule": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Squelette": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Tréant": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": [],
        "description": ""
    },
    "Goule": {
        "type": "fighter",
        "classe": "Thot",
        "archetype": "mort-vivant",
        "cost": 2,
        "atk": 2,
        "pv": 2,
        "effect": [],
        "description": ""
    },
    "Grenouille": {
        "type": "fighter",
        "classe": "Inconnu",
        "archetype": "",
        "cost": 1,
        "atk": 0,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Drake primitif": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "",
        "cost": 4,
        "atk": 4,
        "pv": 4,
        "effect": [],
        "description": ""
    },
    "Gobelin bagarreur": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "",
        "cost": 3,
        "atk": 3,
        "pv": 3,
        "effect": [],
        "description": ""
    },
    "Microbot": {
        "type": "fighter",
        "classe": "Kraken",
        "archetype": "méca",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    "Élémentaire de flamme": {
        "type": "fighter",
        "classe": "Marduk",
        "archetype": "élémentaire",
        "cost": 1,
        "atk": 1,
        "pv": 1,
        "effect": [],
        "description": ""
    },
    # la 2/2 charge
    "Incarnation de Ra": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 3,
        "atk": 1,
        "pv": 5,
        "effect": ["attaque"],
        "description": "lorsqu'il attaque, invoque une recrue"
    },
    "Incarnation d'Anubis": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 5,
        "atk": 3,
        "pv": 6,
        "effect": ["attaque"],
        "description": "lorsqu'il attaque, vol 2 vie à l'avatar adverse"
    },
    "Incarnation de Sobek": {
        "type": "fighter",
        "classe": "Enlil",
        "archetype": "",
        "cost": 6,
        "atk": 5,
        "pv": 5,
        "effect": ["percant", "end turn"],
        "description": "dégats percant, fin de tour: gagne +1/+1"
    },
    "Pyrus 2": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "élémentaire",
        "cost": 4,
        "atk": 4,
        "pv": 4,
        "effect": ["mort", "puissance"],
        "description": "puissance, mort: place Pyrus 3 dans votre deck"
    },
    "Pyrus 3": {
        "type": "fighter",
        "classe": "Enki",
        "archetype": "élémentaire",
        "cost": 8,
        "atk": 8,
        "pv": 8,
        "effect": ["inv"],
        "description": "inv: inflige 4 fois 1 dégats sur un adversaire aléatoire"
    },
    "Colosse de jade": {
        "type": "fighter",
        "classe": "Alchimiste",
        "archetype": "",
        "cost": 5,
        "atk": 4,
        "pv": 5,
        "effect": ["avant-garde"],
        "description": "avant-garde"
    },

    ## SORTS
    "Inspiration": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 0,
        "target": ["none"],
        "description": "rafraichit 2 mana"
    },
    "Comète": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 1,
        "target": ["ennemy", "none"],
        "description": "inflige 2 dégats"
    },
    "Floraison": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 2,
        "target": ["none"],
        "description": "donne 1 cristal de mana vide"
    },
    "Marque de la forêt": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 2,
        "target": ["ally"],
        "description": "donne +2/+2 et protecteur à un combattant allié"
    },
    "Régénération": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 3,
        "target": ["none"],
        "description": "soigne votre avatar de 6"
    },
    "Fiole explosive": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 3,
        "target": ["ennemy"],
        "description": "inflige 5 dégats à un combattant"
    },
    "Ronces paralysantes": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 5,
        "target": ["none"],
        "description": "applique -1/-1 et paralyse les combattants adverses"
    },
    "Force de la nature": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 6,
        "target": ["none"],
        "description": "donne 4 armure à votre avatar et pioche 2 cartes"
    },
    "Potion de fer": {
        "type": "spell",
        "classe": "Enki",
        "cost": 1,
        "target": ["ally"],
        "description": "donne +0/+2 à un combattant allié"
    },
    "Coup de bouclier": {
        "type": "spell",
        "classe": "Enki",
        "cost": 1,
        "target": ["ennemy"],
        "description": "inflige des dégats à un combattant équivalent à votre armure"
    },
    "Engelure": {
        "type": "spell",
        "classe": "Enki",
        "cost": 2,
        "target": ["ennemy"],
        "description": "réduit au silence et paralyse un combattant"
    },
    "Salve de flèches": {
        "type": "spell",
        "classe": "Enki",
        "cost": 2,
        "target": ["none"],
        "description": "inflige 1 dégats aux combattants adverses"
    },
    "Sortilège de mort": {
        "type": "spell",
        "classe": "Enki",
        "cost": 2,
        "target": ["ennemy"],
        "description": "détruit un combattant avec max 3 atk"
    },
    "Nova de givre": {
        "type": "spell",
        "classe": "Enki",
        "cost": 3,
        "target": ["none"],
        "description": "paralyse les combattants adverses"
    },
    "Intelligence": {
        "type": "spell",
        "classe": "Enki",
        "cost": 3,
        "target": ["none"],
        "description": "pioche 2 cartes"
    },
    "Punition divine": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 8,
        "target": ["none"],
        "description": "inflige 8 dégats à l'avatar adverse"
    },
    "Humilité": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 2,
        "target": ["none"],
        "description": "les combattants adverses en front line passent à 1 atk"
    },
    "Renfort de l'armée": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 3,
        "target": ["none"],
        "description": "invoque 3 recrues en front line"
    },
    "Marteau divin": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 4,
        "target": ["ennemy"],
        "description": "inflige 3 dégats à un combattant et soigne votre avatar de 3"
    },
    "Bénédiction d'Enlil": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 4,
        "target": ["none"],
        "description": "2 offrandes"
    },
    "Surpuissance": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 5,
        "target": ["ally"],
        "description": "double l'attaque d'un combattant allié"
    },
    "Rune contrefaite": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 0,
        "target": ["none"],
        "description": "donne 1 mana"
    },
    "Rayon ténèbreux": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 2,
        "target": ["ennemy", "none"],
        "description": "inflige 3 dégats"
    },
    "Chapardage": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 2,
        "target": ["none"],
        "description": "pioche 1 carte dans le deck adverse"
    },
    "Tarot": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 3,
        "target": ["none"],
        "description": "replace les 2 dernières cartes de votre défausse dans votre main"
    },
    "Métamorphose": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 4,
        "target": ["ennemy"],
        "description": "transforme un combattant en grenouille (0/1)"
    },
    "Cataclysme": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 5,
        "target": ["none"],
        "description": "infligez 3 dégats à toutes les unités adversaires, surcharge 2"
    },
    "Crane de Nergal": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 6,
        "target": ["none"],
        "description": "pioche 3 démons, réduit leur cout de 1"
    },
    "Controle mental": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 8,
        "target": ["ennemy"],
        "description": "prend le controle d'un combattant adverse en frontline"
    },
    "Serres de vautour": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 1,
        "target": ["ennemy"],
        "description": "inflige 2 dégats à un combattant"
    },
    "Fouet d'Ishtar": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 1,
        "target": ["ally", "ennemy"],
        "description": "déplace un combattant d'une ligne à l'autre"
    },
    "Lien bestial": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 1,
        "target": ["ally"],
        "description": "donne +1/+1 à une bête alliée, ou +2/+2 si rage"
    },
    "Rugissement sauvage": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 3,
        "target": ["none"],
        "description": "donne +2/+0 à vos unités ce tour"
    },
    "Tir reflexe": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 3,
        "target": ["ennemy"],
        "description": "inflige 3 dégats à un combattant. s'il meurt, pioche 1 carte"
    },
    "Furie d'Ishtar": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 4,
        "target": ["none"],
        "description": "inflige 4 dégats à l'avatar adverse, ou 6 si rage"
    },
    "Tir de barrage": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 5,
        "target": ["ennemy"],
        "description": "inflige 5 dégats à un combattant en front line et 2 au reste de la ligne"
    },
    "Pluie de balles": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 2,
        "target": ["none"],
        "description": "inflige 1 dégat aux combattants en frontline. pioche 1 carte"
    },
    "Sur la planche": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 3,
        "target": ["none"],
        "description": "détruit un combattant adverse en frontline aléatoire"
    },
    "Corrosion": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 4,
        "target": ["none"],
        "description": "retire 3 d'armure à l'avatar adverse et lui inflige 3 dégats"
    },
    "Cri de guerre": {
        "type": "spell",
        "classe": "Marduk",
        "cost": 2,
        "target": ["none"],
        "description": "donne +1/+0 aux alliés"
    },
    "Sang brulant": {
        "type": "spell",
        "classe": "Marduk",
        "cost": 2,
        "target": ["none"],
        "description": "inflige 1 dégat aux combattants ou 3 dégats s'il sont blessés"
    },
    "Boule de feu": {
        "type": "spell",
        "classe": "Marduk",
        "cost": 3,
        "target": ["ennemy", "none"],
        "description": "inflige 4 dégats"
    },
    "Flammes des enfers": {
        "type": "spell",
        "classe": "Marduk",
        "cost": 6,
        "target": ["none"],
        "description": "infligez 4 dégats à toutes les unités sauf les démons"
    },
    "Vision de l'au-delà": {
        "type": "spell",
        "classe": "Thot",
        "cost": 1,
        "target": ["ally"],
        "description": "sacrifice: pioche 2 cartes"
    },
    "Éclair foudroyant": {
        "type": "spell",
        "classe": "Thot",
        "cost": 2,
        "target": ["ennemy"],
        "description": "inflige 3 dégats à un combattant et le paralyse"
    },
    "Aspiration d'âme": {
        "type": "spell",
        "classe": "Thot",
        "cost": 5,
        "target": ["ennemy"],
        "description": "retire un combattant du jeu"
    },
    "Néant": {
        "type": "spell",
        "classe": "Thot",
        "cost": 7,
        "target": ["none"],
        "description": "détruit tous les combattants"
    },

    # A TRIER
    "Pluie torrentielle": {
        "type": "spell",
        "classe": "Enki",
        "cost": 4,
        "target": ["none"],
        "description": "inflige 2 fois 1 dégats à toutes les unités adverses"
    },
    "Formation de combat": {
        "type": "spell",
        "classe": "Enki",
        "cost": 6,
        "target": ["none"],
        "description": "invoque 4 Lancier en front line"
    },
    "Déplumage": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 3,
        "target": ["ally"],
        "description": "sacrifie un tofu et inflige des dégats équivalents à son attaque à toutes les unités adverses"
    },
    "Descente dans les abysses": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 5,
        "target": ["none"],
        "description": "réduit le cout des abyssaux de 1 (deck ou main)"
    },
    "Apaisement": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 1,
        "target": ["none"],
        "description": "si rage: soigne votre avatar de 5 (et consomme l'état rage)"
    },
    "Déchirement": {
        "type": "spell",
        "classe": "Ishtar",
        "cost": 2,
        "target": ["none"],
        "description": "inflige 2 dégats à ton avatar pour piocher 2 cartes"
    },
    "Éclat sysmique": {
        "type": "spell",
        "classe": "Enlil",
        "cost": 3,
        "target": ["ennemy"],
        "description": "détruit une structure"
    },
    "Pack d'assemblage": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 2,
        "target": ["none"],
        "description": "pioche un tourelle, réduit son cout de 1 et augmente sa durabilité de 1"
    },
    "Mort proche": {
        "type": "spell",
        "classe": "Marduk",
        "cost": 2,
        "target": ["ally"],
        "description": "donne +3/+3 à un allié blessé"
    },
    "Sournoiserie": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 3,
        "target": ["ennemy"],
        "description": "défausse une carte pour détruire un combattant"
    },
    "Laché de dominos": {
        "type": "spell",
        "classe": "Inconnu",
        "cost": 2,
        "target": ["none"],
        "description": "inflige 1 dégat à toutes les unités, repete si en tue une"
    },
    "Idole de jade": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 1,
        "target": ["none"],
        "description": "ajoute un Colosse de jade à ta main, si ton maximum de mana est de 9, en ajoute 3"
    },
    "Écorce": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 2,
        "target": ["none"],
        "description": "pioche 1 carte, si c'est un sort, gagne 3 armure"
    },
    "Revanche de la forêt": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 6,
        "target": ["ennemy"],
        "description": "détruit une unité, inspiration : invoque un tréant en frontline"
    },

    # EXTRA
    "Crochet": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 1,
        "target": ["ally"],
        "description": "donne +1/+0 a un pirate"
    },
    "Torche enflammée": {
        "type": "spell",
        "classe": "Enki",
        "cost": 2,
        "target": ["none"],
        "description": "inflige 3 dégats à l'avatar adverse"
    },
    "Infection": {
        "type": "spell",
        "classe": "Alchimiste",
        "cost": 1,
        "target": ["none", "hand"],
        "description": "start turn : inflige 1 dégat à ton avatar"
    },
    "Gros boulet": {
        "type": "spell",
        "classe": "Kraken",
        "cost": 5,
        "target": ["none"],
        "description": ""
    },



}
