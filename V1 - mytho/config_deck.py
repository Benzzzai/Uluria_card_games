from avatar import *

deck_set = {

    "Alchimiste ramp" : {
        "avatar" : {"Alchimiste" : Alchimiste(4)},
        "main_deck" : {"Papillon enchanté" : 2, "Lutin des bois" : 3, "Golem ancien" : 3, "Satyre mystique" : 3, "Druide de la griffe" : 3,
                    "Drake émeraude" : 2, "Gardien des bois" : 2, "Bastiosaure" : 1, "Archidruide" : 1, "Ancien de la forêt" : 2,
                    "Inspiration" : 3, "Comète" : 2, "Floraison" : 3, "Marque de la forêt" : 2, "Régénération" : 2,
                    "Fiole explosive" : 2, "Ronces paralysantes" : 2, "Force de la nature" : 2},
    },

    "Pirate aggro" : {
        "avatar" : {"Marduk" : Marduk(3), "Kraken" : Kraken(3)},
        "main_deck" :{"Boucanier" : 3, "Vigie pirate" : 3, "Canon du navire" : 3, "Capitaine pirate" : 3, "Flibustier" : 3, "Capitaine Krag" : 1, 
                    "Matelot" : 3, "Corsaire furtif" : 3, "Manieur de sabre" : 3, "Chargeur orc" : 1, 
                    "Gobelin infecté" : 2, "Chevaucheur de porcass" : 2, "Le Découpeur" : 1,  
                    # "Fizz" : 1,
                    "Cri de guerre" : 2, "Boule de feu" : 2, "Sur la planche" : 2, "Corrosion" : 2,}
    },

    "Enki base" : {
        "avatar" : {"Enki" : Enki(4)},
        "main_deck" :{"Éclat glaciaire" : 2, "Apprenti sorcier" : 2, "Lancier" : 3, "Garde tortue" : 2, "Friselame" : 1, "Hacheur nain" : 3, 
                    "Gardien de la porte" : 1, "Griffon" : 2, "Troll des neiges" : 3, "Antonidas" : 1, "Prêtresse corrompue" : 2, "Colosse rocheux" : 2, "Drake ancestral" : 2,
                    "Coup de bouclier" : 2, "Sortilège de mort" : 2, "Salve de flèches" : 3, "Engelure" : 1,
                    "Nova de givre" : 2, "Intelligence" : 3, "Punition divine" : 1}
    },

    "Démon Marduk-Ishtar" : {
        "avatar" : {"Marduk" : Marduk(3), "Ishtar" : Ishtar(3)},
        "main_deck" :{"Diablotin des abimes" : 3, "Maitresse succube" : 3, "Seigneur des abimes" : 3, "Pazuzu" : 1, "Ereshkigal" : 1, "Terreur du vide" : 3, 
                    "Marcheur du vide" : 3, "Serviteur de Caor" : 3, "Caor" : 1, "Ereshkigal" : 1, "Terreur du vide" : 3,
                    "Apaisement" : 2, "Déchirement" : 2, "Tir reflexe" : 2, "Furie d'Ishtar" : 2,
                    "Cri de guerre" : 2, "Boule de feu" : 2, "Mort proche" : 2, "Flammes des enfers" : 1,
                    }
    },

    "Abyssal ramp" : {
        "avatar" : {"Kraken" : Kraken(3), "Alchimiste" : Alchimiste(3)},
        "main_deck" :{"Dévoreur des abysses" : 3, "Rampant des profondeurs" : 3, "Khalamar géant" : 1, "Oeil des abysses" : 3, "Pêcheur légendaire" : 1, "Wyrm aquatique" : 3,
                    # "Fizz" : 1,
                    "Papillon enchanté" : 1, "Lutin des bois" : 3, "Golem ancien" : 2, "Satyre mystique" : 2, "Druide de la griffe" : 2,
                    "Inspiration" : 3, "Comète" : 2, "Floraison" : 3, "Régénération" : 1, "Ronces paralysantes" : 1, "Force de la nature" : 1,
                    "Sur la planche" : 2, "Pluie de balles" : 2}
    },

    "Abyssal tourelle" : {
        "avatar" : {"Kraken" : Kraken(4)},
        "main_deck" :{"Dévoreur des abysses" : 3, "Rampant des profondeurs" : 3, "Khalamar géant" : 1, "Oeil des abysses" : 3, "Pêcheur légendaire" : 1, "Wyrm aquatique" : 3,
                      "Foreuse" : 3, "Bathyscaphe" : 3, "Chalutier" : 3, "Maitre des rouages" : 3, "Technomage" : 3, "Bricoleur" : 3
                      }
    },

    "Enlil base" : {
        "avatar" : {"Enlil" : Enlil(4)},
        "main_deck" :{"Écuyer" : 2, "Rejeton de lumière" : 2, "Entraineur" : 2, "Robot blindé" : 2, "Archer d'élite" : 2, "Aventurier" : 2,
                    "Milicien antique" : 3, "Pacificateur" : 3, "Sentinelle" : 2, "Roi de Fondor" : 1, "Robot de soin" : 2, "Chevalier gemme" : 2, "Silencieux" : 2,
                    "Garde lumière" : 2, "Grande prêtresse de Ninlil" : 1, "Champion de Fondor" : 2, 
                    "Renfort de l'armée" : 2, "Marteau divin" : 2, "Bénédiction d'Enlil" : 2, "Surpuissance" : 2}
    },

    "Alchimiste ramp 2" : {
        "avatar" : {"Alchimiste" : Alchimiste(4)},
        "main_deck" : {"Papillon enchanté" : 2, "Lutin des bois" : 3, "Sylvenier" : 2, "Golem ancien" : 2, "Satyre mystique" : 2, "Druide de la griffe" : 3,
                    "Drake émeraude" : 1, "Gardien des bois" : 1, "Bastiosaure" : 1, "Archidruide" : 1, "Ancien de la forêt" : 2, "Malygos" : 1, "Protecteur runique" : 1,
                    "Inspiration" : 3, "Comète" : 2, "Floraison" : 3, "Marque de la forêt" : 2, "Régénération" : 2,
                    "Fiole explosive" : 2, "Ronces paralysantes" : 1, "Revanche de la forêt" : 1, "Force de la nature" : 2},
    },

}

