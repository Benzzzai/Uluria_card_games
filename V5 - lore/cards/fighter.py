from cards.card import Card
from config.config_fighter import fighter_set
import copy

class Fighter(Card):
    def __init__(self, name):
        stats = copy.deepcopy(fighter_set[name])
        super().__init__(name, stats["cost"])
        self.atk = stats["atk"]
        self.atk_ori = stats["atk"]
        self.strike = stats["strike"]
        self.strike_ori = stats["strike"]
        self.pv = stats["pv"]
        self.pv_max = stats["pv"]
        self.pv_ori = stats["pv"]
        self.effect = stats["effect"]

        self.status = "actionable" # "actionable", "engagé", "blocage"
        self.paralyse = False

        self.action = ("action" in self.effect)
        self.on_inv = ("on_inv" in self.effect)
        self.on_inv_target = ("on_inv_target" in self.effect)
        self.on_soutien = ("on_soutien" in self.effect)
        self.on_atk = ("on_atk" in self.effect)
        self.on_strike = ("on_strike" in self.effect)
        self.overkill = ("overkill" in self.effect)
        self.on_mort = ("on_mort" in self.effect)
        self.start_turn = ("start turn" in self.effect)
        self.end_turn = ("end turn" in self.effect)

        self.bouclier = ("bouclier" in self.effect)
        self.protecteur = ("protecteur" in self.effect)
        self.puissance = ("puissance" in self.effect)
        self.rapide = ("rapide" in self.effect)
        self.robuste = ("robuste" in self.effect)
        self.soutien = ("soutien" in self.effect)


    def take_damage(self, value):
        if self.robuste:
                value -= 1
        if value > 0:
            if self.bouclier:
                self.bouclier = False
            else:
                self.pv -= value

    def kill(self):
        self.pv = 0

    def heal(self, value):
        self.pv = min(self.pv + value, self.pv_max)

    def buff(self, atk, strike, pv):
        self.atk += atk
        self.strike += strike
        self.pv += pv
        self.pv_max += pv

    def silence(self):
        self.atk = self.atk_ori
        self.strike = self.strike_ori
        self.pv_max = self.pv_ori
        self.pv = min(self.pv, self.pv_max)

        self.paralyse = False

        self.on_inv = False
        self.on_inv_target = False
        self.on_atk = False
        self.on_strike = False
        self.overkill = False
        self.on_mort = False
        self.start_turn = False
        self.end_turn = False

        self.bouclier = False
        self.protecteur = False
        self.puissance = False
        self.rapide = False
        self.robuste = False


    def activate_inv_target(self, ally_player, ennemy_player, target):
        if self.name == "":
            pass

    def activate_inv(self, ally_player, ennemy_player):
        if self.name == "Sombre cultiste":
            ally_player.heal(2)
        elif self.name == "":
            pass

    def activate_attaque(self, ally_player, ennemy_player):
        if self.name == "":
            pass
    
    def activate_strike(self, ally_player, ennemy_player):
        if self.name == "Tofukaz":
            self.kill()
        elif self.name == "Élémentaire de lave":
            ally_player.take_damage(1)
        elif self.name == "":
            pass
        
    def activate_overkill(self, ally_player, ennemy_player):
        if self.name == "Chevalier gemme":
            ally_player.heal(1)
        elif self.name == "Combattant sauvage":
            ennemy_player.take_damage(1)
        elif self.name == "Drake emeraude":
            ally_player.heal(2)
        elif self.name == "Ogre glouton":
            ennemy_player.take_damage(2)
        elif self.name == "Jeteur d'encre":
            pass
        elif self.name == "Hydre mécanique":
            self.status = "actionable"
        elif self.name == "Pazuzu":
            ally_player.heal(1)
        elif self.name == "":
            pass
        
    def activate_soutien(self, ally_player, ennemy_player, target):
        if self.name == "Bouftou céleste":
            target.heal(2)
        elif self.name == "Ziliax":
            target.bouclier = True
        elif self.name == "":
            pass
        
    def activate_soin(self, ally_player, ennemy_player):
        if self.name == "Clerc du royaume":
            self.buff(2, 0, 0)
        elif self.name == "Prêtresse corrompue":
            for fighter in ennemy_player.board:
                fighter.take_damage(1)
        elif self.name == "":
            pass
        
    def activate_action(self, ally_player, ennemy_player):
        if self.name == "":
            pass

    def activate_action_target(self, ally_player, ennemy_player, target):
        if self.name == "":
            pass

    def activate_mort(self, ally_player, ennemy_player):
        if self.name == "Rejeton de lumière":
            ennemy_player.heal(3)
        elif self.name == "Gobelin malade":
            ennemy_player.take_damage(2)
        elif self.name == "Tortue de lave":
            pass
        elif self.name == "Dragon cactus":
            ennemy_player.take_damage(1)
        elif self.name == "Gardien du bosquet":
            pass
        elif self.name == "":
            pass

    def activate_start_turn(self, ally_player, ennemy_player):
        if self.name == "":
            pass

    def activate_end_turn(self, ally_player, ennemy_player):
        if self.name == "Boufmouth":
            ally_player.heal(1)
        elif self.name == "Tofu royal":
            self.status = "actionable"
        elif self.name == "Acolyte de la souffrance":
            if self.pv < self.pv_max:
                ally_player.draw_card(1)
        elif self.name == "Berserker Porcass":
            if self.pv < self.pv_max:
                self.buff(2, 0, 0)
        elif self.name == "Destrier funeste":
            self.status = "actionable"
        elif self.name == "":
            pass
        
      
