from card_class.structure import Structure
from card_class.unit import Unit
from card_class.spell import Spell
import random


class Fighter(Unit):
    def __init__(self, name, cost, atk, pv, effect, classe, archetype, description):
        super().__init__(name, cost, pv, effect, classe, archetype, description)
        self.atk = atk
        self.atk_ori = atk

    def activate_inv_target(self, ally_player, ennemy_player, target):
        if self.name == "Éclat glaciaire":
            target.paralyse = True
        elif self.name == "Papillon enchanté":
            target.silence()
        elif self.name == "Archer elf":
            target.take_damage(1)
        elif self.name == "Archer d'élite":
            target.take_damage(2)
        elif self.name == "Garde Tortue":
            target.protecteur = True
        elif self.name == "Troll des neiges":
            target.paralyse = True
        elif self.name == "Gardien des bois":
            target.buff(2, 2)
        elif self.name == "Friselame":
            if target.paralyse:
                target.pv = 0
            else:
                target.paralyse = True
        elif self.name == "Prêtresse corrompue":
            if target.atk <= 2:
                target.pv = 0
        elif self.name == "Bouftou de guerre":
            target.charge = True
            target.actionable = True
        elif self.name == "Bouftou primitif":
            target.take_damage(2)
        elif self.name == "Sergent cruel":
            target.take_damage(1)
            target.buff(2, 0)
        elif self.name == "Manieur de sabre":
            if ally_player.is_archetype_on_board("pirate"):
                target.take_damage(2)
        elif self.name == "Esprit déchainé":
            target.pv = 0
        elif self.name == "Champion de fondor":
            target.pv = 0
        elif self.name == "Robot de soin":
            target.heal(3)
        elif self.name == "Technomage":
            if isinstance(target, Structure):
                target.buff(0, 1)
        elif self.name == "Clown mystique":
            target.atk, target.pv = target.pv, target.atk

    def activate_inv(self, ally_player, ennemy_player):
        if self.name == "Matelot":
            if ally_player.is_archetype_on_board("pirate"):
                self.charge = True
        elif self.name == "Lutin des bois":
            ally_player.draw_card(1, Spell)
        elif self.name == "Bricoleur":
            ally_player.draw_card(1)
        elif self.name == "Flibustier":
            ally_player.draw_card(1, Fighter, "pirate")
        elif self.name == "Archer squelette":
            ennemy_player.take_damage(1)
        elif self.name == "Sombre cultiste":
            ally_player.heal(3)
        elif self.name == "Albatros":
            ally_player.draw_card(1)
            ennemy_player.draw_card(1)
        elif self.name == "Gnome maléfique":
            card = ennemy_player.deck.pop(0)
            ennemy_player.discard.append(card)
        elif self.name == "Satyre mystique":
            for card in ally_player.hand:
                if isinstance(card, Spell):
                    card.reduce_cost(1)
                    break
        elif self.name == "Élise":
            ally_player.summon_unit("Araignée", "back")
            ally_player.summon_unit("Araignée", "back")
        elif self.name == "Chargeur orc":
            if len(ally_player.hand) == 0:
                ally_player.draw_card(3)
        elif self.name == "Silencieux":
            for card in ennemy_player.frontrow:
                card.silence()
        elif self.name == "Antonidas":
            ally_player.deck.append(ally_player.create_card("Torche enflammée"))
            ally_player.deck.append(ally_player.create_card("Torche enflammée"))
            random.shuffle(ally_player.deck)
        elif self.name == "Roi de Fondor":
            ally_player.take_damage(4)
            ally_player.gain_armor(8)
        elif self.name == "Diablotin des abimes":
            ally_player.take_damage(2, active=True)
        elif self.name == "Seigneur des abimes":
            ally_player.take_damage(4, active=True)
        elif self.name == "Invocateur du vide":
            random.shuffle(ally_player.discard)
            for card in ally_player.discard:
                if isinstance(card, Fighter) and card.cost <= 2:
                    if card.archetype == "démon":
                        ally_player.discard.remove(card)
                        ally_player.backrow.append(card)
                        card.atk = card.atk_ori
                        card.pv = card.pv_ori
                        card.pv_max = card.pv_ori
                        card.actionable = False
                        break
        elif self.name == "Aventurier":
            if ally_player.avatar["Enlil"].level >= 2:
                ally_player.draw_card(1)
        elif self.name == "Grande prêtresse de Ninlil":
            for unit in ally_player.frontrow:
                unit.heal(2)
            for unit in ally_player.backrow:
                unit.heal(2)
        elif self.name == "Robot de soin":
            ally_player.heal(3)
        elif self.name == "Bébé phorreur":
            card = ally_player.hand.pop(0)
            self.deck.append(card)
            ally_player.draw_card(1)
            random.shuffle(ally_player.deck)
        elif self.name == "Phorreur camouflé":
            ally_player.surcharge += 1
        elif self.name == "Diablotin ardent":
            pass
        elif self.name == "Saccagueur démoniaque":
            ally_player.max_mana_turn -= 1
        elif self.name == "Empereur du vide":
            ally_player.surcharge += 2
        elif self.name == "Chasseuse vorace":
            if ally_player.rage_ishtar:
                for unit in ennemy_player.frontrow:
                    unit.take_damage(1)
                for unit in ennemy_player.backrow:
                    unit.take_damage(1)
        elif self.name == "Maitresse succube":
            if ally_player.rage_ishtar:
                self.vol_vie = True
        elif self.name == "Ereshkigal":
            for unit in ally_player.frontrow:
                if unit.archetype == "démon":
                    unit.buff(2, 2)
            for unit in ally_player.backrow:
                if unit.archetype == "démon":
                    unit.buff(2, 2)
        elif self.name == "Terreur du vide":
            for unit in ennemy_player.frontrow:
                unit.take_damage(1)
            for unit in ennemy_player.backrow:
                unit.take_damage(1)
        elif self.name == "Vigie pirate":
            ally_player.hand.append(ally_player.create_card("Crochet"))
        elif self.name == "Serviteur de Caor":
            if ally_player.is_archetype_on_board("démon"):
                ally_player.draw_card(1, Fighter, "démon")
        elif self.name == "Berger porcass":
            ally_player.summon_unit("Porcass", "back")
        elif self.name == "Corsaire furtif":
            ennemy_player.armor = max(0, ennemy_player.armor - 1)
        elif self.name == "Maitre blessé":
            self.take_damage(4)
        elif self.name == "Caor":
            for card in ally_player.hand:
                if isinstance(card, Spell):
                    card.reduce_cost(1)
        elif self.name == "Vampyro":
            for card in ally_player.hand:
                card.reduce_cost(1)
        elif self.name == "Rampant des profondeurs":
            for card in ally_player.deck:
                if card.name == "Rampant des profondeurs":
                    card.reduce_cost(2)
            for card in ally_player.hand:
                if card.name == "Rampant des profondeurs":
                    card.reduce_cost(2)
        elif self.name == "Khalamar géant":
            pass
        elif self.name == "Pêcheur légendaire":
            ally_player.draw_card(1, Fighter, "abyssal")
            # pour les buff de carte piochée, comment s'assurer qu'on les a bien piochée ?
        elif self.name == "Wyrm aquatique":
            for card in ally_player.hand:
                if isinstance(card, Fighter):
                    if card.archetype == "abyssal":
                        card.reduce_cost(1)
        elif self.name == "Dragarde":
            ally_player.draw_card(1)
        elif self.name == "Sylvenier":
            if ally_player.inspiration:
                ally_player.max_mana_turn += 1
        elif self.name == "Maitre vaudou":
            ennemy_player.deck.append(ennemy_player.create_card("Infection"))
            if ally_player.inspiration:
                ennemy_player.deck.append(ennemy_player.create_card("Infection"))
            random.shuffle(ennemy_player.deck)
        elif self.name == "Kin gael":
            pass
        elif self.name == "Protecteur runique":
            ally_player.gain_armor(8)
        elif self.name == "Flammetin":
            ally_player.hand.append(ally_player.create_card("Élémentaire de flamme"))
        elif self.name == "Malygos":
            ally_player.puissance += 1
        elif self.name == "Requin marteau":
            ennemy_player.hand.append(ennemy_player.create_card("Gros boulet"))
        elif self.name == "Horreb":
            pass
        elif self.name == "Robot artificié":
            pass
        elif self.name == "Pyrus 3":
            pass

    def activate_front(self, ally_player, ennemy_player, target=None):
        if self.name == "Entraineur":
            for card in ally_player.frontrow:
                card.buff(1, 0)
        elif self.name == "Capitaine pirate":
            if target:
                if target.archetype == "pirate":
                    target.buff(1, 1)
        elif self.name == "Tofu ventripotent":
            if target:
                ennemy_player.frontrow.remove(target)
                ennemy_player.backrow.append(target)
        elif self.name == "Phorreur cuirassé":
            ally_player.gain_armor(2)
        elif self.name == "Archidruide":
            ally_player.summon_unit("Tréant", "front")
            ally_player.summon_unit("Tréant", "front")
        elif self.name == "Ancien de la forêt":
            ally_player.draw_card(1)
        elif self.name == "Maitre des rouages":
            if ally_player.is_archetype_on_board("tourelle"):
                self.buff(2, 0)
        elif self.name == "Pacificateur":
            if target:
                target.atk = 1

    def activate_attaque(self, ally_player, ennemy_player):
        if self.name == "Tofukaz":
            self.pv = 0
        elif self.name == "Tofu royal":
            ally_player.frontrow.remove(self)
            ally_player.backrow.append(self)
        elif self.name == "Combattant sauvage":
            ennemy_player.take_damage(1)
        elif self.name == "Incarnation de Ra":
            ally_player.summon_unit("Recrue", "front")
        elif self.name == "Incarnation d'Anubis":
            ennemy_player.take_damage(2)
            ally_player.heal(2)

    def activate_soin(self, ally_player, ennemy_player):
        if self.name == "Prêtresse maléfique":
            for unit in ennemy_player.frontrow:
                unit.take_damage(1)
            for unit in ennemy_player.backrow:
                unit.take_damage(1)

    def activate_mort(self, ally_player, ennemy_player):
        if self.name == "Gobelin infecté":
            ennemy_player.take_damage(1)
        elif self.name == "Spectre":
            ally_player.draw_card(1)
        elif self.name == "Rampante":
            if self in ally_player.frontrow:
                ally_player.summon_unit("Araignée", "front")
                ally_player.summon_unit("Araignée", "front")
            else:
                ally_player.summon_unit("Araignée", "back")
                ally_player.summon_unit("Araignée", "back")
        elif self.name == "Hacheur nain":
            ally_player.gain_armor(2)
        elif self.name == "Corbeau pourpre":
            ally_player.draw_card(1, Spell)
        elif self.name == "Destrier de la mort":
            if len(ally_player.frontrow) > 0:
                target = random.choice(ally_player.frontrow)
                target.buff(1, 1)
        elif self.name == "Ombre cosmique":
            avatar = ally_player.avatar.get("Inconnu")
            if avatar.offering():
                avatar.activate_avatar_on_hit(ally_player, ennemy_player)
        elif self.name == "Momie infestée":
            if self in ally_player.frontrow:
                ally_player.summon_unit("Goule", "front")
            else:
                ally_player.summon_unit("Goule", "back")
        elif self.name == "Empereur du vide":
            if self in ally_player.frontrow:
                ally_player.summon_unit("Démon inférieur", "front")
                ally_player.summon_unit("Démon inférieur", "front")
            else:
                ally_player.summon_unit("Démon inférieur", "back")
                ally_player.summon_unit("Démon inférieur", "back")
        elif self.name == "Berserkoffre":
            ally_player.hand.append(ally_player.create_card("Rune contrefaite"))
        elif self.name == "Rejeton de lumière":
            ennemy_player.heal(3)
        elif self.name == "Pyrus":
            ally_player.deck.append(ally_player.create_card("Pyrus 2"))
            random.shuffle(ally_player.deck)
        elif self.name == "Pyrus 2":
            ally_player.deck.append(ally_player.create_card("Pyrus 3"))
            random.shuffle(ally_player.deck)
        elif self.name == "Minibot":
            if self in ally_player.frontrow:
                ally_player.summon_unit("Microbot", "front")
            else:
                ally_player.summon_unit("Microbot", "back")
    
    def activate_start_turn(self, ally_player, ennemy_player):
        if self.name == "Gardien de la porte":
            self.pv = self.pv_max
        elif self.name == "Élémentaire de lave":
            ally_player.take_damage(1)
            ennemy_player.take_damage(1)

    def activate_end_turn(self, ally_player, ennemy_player):
        if self.name == "Boufmouth":
            if len(ally_player.frontrow) > 0:
                target = random.choice(ally_player.frontrow)
                target.heal(1) 
        elif self.name == "Canon du navire":
            if ally_player.is_archetype_on_board("pirate"):
                ennemy_player.take_damage(1)
        elif self.name == "Berserker porcass":
            if self.pv < self.pv_max:
                self.buff(2,0)
        elif self.name == "Ancien de la forêt":
            ally_player.heal(3)
        elif self.name == "Drake ancestral":
            ally_player.summon_unit("Drake primitif", "back")
        elif self.name == "Acolyte de la souffrance":
            if self.pv < self.pv_max:
                ally_player.draw_card(1)
        elif self.name == "Gobelin à sarbacane":
            ennemy_player.deck.append(ennemy_player.create_card("Infection"))
            random.shuffle(ennemy_player.deck)
        elif self.name == "Méca téléporteur":
            if self in ally_player.frontrow:
                ally_player.summon_unit("Microbot", "front")
            else:
                ally_player.summon_unit("Microbot", "back")
        elif self.name == "Incarnation de Sobek":
            self.buff(1,1)

    def take_damage(self, value):
        if self.robuste:
                value -= 1
        if value > 0:
            if self.bouclier:
                self.bouclier = False
            else:
                self.pv -= value

    def heal(self, value):
        self.pv = min(self.pv + value, self.pv_max)

    def buff(self, atk, pv):
        self.atk += atk
        self.pv += pv
        self.pv_max += pv

    def silence(self):
        self.atk = self.atk_ori
        self.pv_max = self.pv_ori
        self.pv = min(self.pv, self.pv_max)

        self.paralyse = False

        self.inv = False
        self.inv_ennemy = False
        self.inv_ally = False
        self.front = False
        self.attaque = False
        self.soin = False
        self.mort = False
        self.start_turn = False
        self.end_turn = False
        self.avant_garde = False
        self.bouclier = False
        self.charge = False
        self.insaisissable = False
        self.magnetisme = False
        self.percant = False
        self.protecteur = False
        self.puissance = False
        self.rapide = False
        self.robuste = False
        self.vol_vie = False

