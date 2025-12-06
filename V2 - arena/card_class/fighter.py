from card_class.card import Card
from card_class.unit import Unit
import random


class Fighter(Unit):
    def __init__(self, name, cost, atk, pv, effect, race=""):
        super().__init__(name, cost, pv, effect)
        self.atk = atk
        self.atk_ori = atk
        self.race = race

    def activate_inv(self, ally_player, ennemy_player, target=None):
        if self.name == "Matelot":
            if len(ally_player.backrow) + len(ally_player.frontrow) > 1:
                self.buff(1, 0)
        elif self.name == "Eclat glaciaire":
            target.paralyse = True
        elif self.name == "Lutin":
            ally_player.draw_card(1, "spell")
        elif self.name == "Bricoleur":
            ally_player.draw_card(1)
        elif self.name == "Archer elf":
            target.take_damage(1)
        elif self.name == "Archer squelette":
            ennemy_player.take_damage(1)
        elif self.name == "Archer d'élite":
            target.take_damage(2)
        elif self.name == "Cultiste":
            ally_player.heal(2)
        elif self.name == "Tortue":
            ally_player.gain_armor(2)
        elif self.name == "Albatros":
            ally_player.draw_card(1)
            ennemy_player.draw_card(1)
        elif self.name == "Gnome maléfique":
            card = ennemy_player.deck.pop(0)
            ennemy_player.discard.append(card)
        elif self.name == "Troll des neiges":
            target.paralyse = True
        elif self.name == "Satyre":
            for card in ally_player.hand:
                if card.card_type == "spell":
                    card.cost = max(0, card.cost - 1)
                    break
        elif self.name == "Elise":
            # ally_player.summon_unit("Araignée", "back")
            # ally_player.summon_unit("Araignée", "back")
            ennemy_player.take_damage(1)
        elif self.name == "Chargeur":
            if len(ally_player.hand) == 0:
                ally_player.draw_card(3)
        elif self.name == "Silencieux":
            for card in ennemy_player.frontrow:
                card.silence()
        elif self.name == "Antonidas":
            ally_player.deck.append(ally_player.create_card("Torche enflammée"))
            ally_player.deck.append(ally_player.create_card("Torche enflammée"))
        elif self.name == "Archidruide":
            ally_player.summon_unit("Tréant", "back")
        elif self.name == "Main d'argent":
            for card in ally_player.backrow:
                card.buff(1, 1)
            for card in ally_player.frontrow:
                card.buff(1, 1)
        elif self.name == "Roi de Fondor":
            ally_player.take_damage(5)
            ally_player.gain_armor(10)
        elif self.name == "Friselame":
            if target.paralyse:
                target.pv = 0
            else:
                target.paralyse = True
        elif self.name == "Ashe":
            for card in ennemy_player.frontrow:
                if card.paralyse:
                    card.take_damage(2)
                else:
                    card.take_damage(1)
            for card in ennemy_player.backrow:
                if card.paralyse:
                    card.take_damage(2)
                else:
                    card.take_damage(1)
        elif self.name == "Osamodas":
            ally_player.summon_unit("Tofu", "front")
        elif self.name == "Diablotin des flammes":
            ally_player.take_damage(2)
        elif self.name == "Seigneur des abimes":
            ally_player.take_damage(4)
        elif self.name == "Invocateur du vide":
            random.shuffle(ally_player.discard)
            for card in ally_player.discard:
                if card.card_type == "fighter" and card.cost <= 2:
                    ally_player.discard.remove(card)
                    ally_player.backrow.append(card)
                    card.atk = card.atk_ori
                    card.pv = card.pv_ori
                    card.pv_max = card.pv_ori
                    card.actionable = False
                    break
        elif self.name == "Aventurier":
            if ally_player.inspiration:
                self.buff(1, 1)

    def activate_front(self, ally_player, ennemy_player, target=None):
        if self.name == "Capitaine pirate":
            if target != None:
                target.buff(1, 1)
        elif self.name == "Entraineur":
            for card in ally_player.frontrow:
                card.buff(1, 0)

    def activate_attaque(self, ally_player, ennemy_player):
        if self.name == "Tofu royal":
            ally_player.frontrow.remove(self)
            ally_player.backrow.append(self)
        elif self.name == "Combattant sauvage":
            ennemy_player.take_damage(1)

    def activate_mort(self, ally_player, ennemy_player):
        if self.name == "Gobelin":
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
        elif self.name == "Ombre du vide":
            ally_player.draw_card(1, "divine")
        elif self.name == "Goule infestée":
            if self in ally_player.frontrow:
                ally_player.summon_unit("Squelette", "front")
            else:
                ally_player.summon_unit("Squelette", "back")
        elif self.name == "Destrier de la mort":
            if len(ally_player.frontrow) > 0:
                target = random.choice(ally_player.frontrow)
                target.buff(1, 1)
        elif self.name == "Sylvanas":
            if len(ennemy_player.frontrow) > 0:
                target = random.choice(ennemy_player.frontrow)
                ennemy_player.frontrow.remove(target)
                ally_player.frontrow.append(target)
    
    def activate_start_turn(self, ally_player, ennemy_player):
        if self.name == "Gardien de la porte":
            self.pv = self.pv_max
        elif self.name == "Fizz":
            self.buff(1, 1)

    def activate_end_turn(self, ally_player, ennemy_player):
        if self.name == "Drake ancestral":
            ally_player.summon_unit("Drake", "back")
        elif self.name == "Illaoi":
            ally_player.summon_unit("Tentacule", "front")

    def activate_card_played(self, ally_player, ennemy_player, card):
        if self.name == "Canon du navire":
            if isinstance(card, Fighter):
                ennemy_player.take_damage(1)

    def take_damage(self, value):
        # interaction entre robuste et bouclier ?
        if value > 0:
            if self.robuste:
                value -= 1
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
        self.front = False
        self.mort = False
        self.start_turn = False
        self.end_turn = False
        self.bouclier = False
        self.defenseur = False
        self.insaisisable = False
        self.inciblable = False
        self.percant = False
        self.protecteur = False
        self.puissance = False
        self.rapide = False
        self.robuste = False
        self.rush = False
        self.vol_vie = False
