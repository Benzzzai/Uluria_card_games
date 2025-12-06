from card_class.card import Card
import random

class Spell(Card):
    def __init__(self, name, cost, target_type, element=""):
        super().__init__(name, cost)
        self.target_type = target_type
        self.element = element

    def activate_spell(self, active_player, ennemy_player, target=None):
        if self.name == "Inspiration":
            active_player.extra_mana += 1
        elif self.name == "Feu protecteur":
            active_player.summon_unit("Feu follet", "front")
        elif self.name == "Coup de bouclier":
            target.take_damage(active_player.armor)
        elif self.name == "Régénération":  
            active_player.heal(6)
        elif self.name == "Floraison":   
            active_player.ramp += 2
        elif self.name == "Marque de la foret":
            target.buff(2, 2)
        elif self.name == "Pluie de balles":
            dmg = 1 + active_player.get_puissance()
            for card in active_player.frontrow:
                card.take_damage(dmg)
            for card in ennemy_player.frontrow:
                card.take_damage(dmg)
            active_player.draw_card(1)
        elif self.name == "Salve de flèches":
            dmg = 1 + active_player.get_puissance()
            for card in ennemy_player.backrow:
                card.take_damage(dmg)
            for card in ennemy_player.frontrow:
                card.take_damage(dmg)
        elif self.name == "Intelligence":
            active_player.draw_card(2)
        elif self.name == "Maitrise du blocage":
            active_player.gain_armor(4)
            active_player.draw_card(1)
        elif self.name == "Griffes":
            target.take_damage(4 + active_player.get_puissance())
        elif self.name == "Boule de feu":
            target.take_damage(6 + active_player.get_puissance())
        elif self.name == "Nova de givre":
            for card in ennemy_player.backrow:
                card.paralyse = True
            for card in ennemy_player.frontrow:
                card.paralyse = True
        elif self.name == "Surpuissance":
            target.atk *= 2
        elif self.name == "Renfort de l'armée":
            active_player.summon_unit("Recrue", "front")
            active_player.summon_unit("Recrue", "front")
            active_player.summon_unit("Recrue", "front")
        elif self.name == "Marteau divin":
            target.take_damage(3 + active_player.get_puissance())
            active_player.heal(3)
        elif self.name == "Colère":
            ennemy_player.take_damage(4 + active_player.get_puissance())
        elif self.name == "Assassiner":
            target.pv = 0
        elif self.name == "Force de la nature":
            active_player.gain_armor(4)
            active_player.draw_card(2)
        elif self.name == "Néant":
            for card in active_player.backrow:
                card.pv = 0
            for card in active_player.frontrow:
                card.pv = 0
            for card in ennemy_player.backrow:
                card.pv = 0
            for card in ennemy_player.frontrow:
                card.pv = 0
        elif self.name == "Flamme infernale":
            dmg = 1 + active_player.get_puissance()
            for card in active_player.backrow:
                card.take_damage(dmg)
            for card in active_player.frontrow:
                card.take_damage(dmg)
            for card in ennemy_player.backrow:
                card.take_damage(dmg)
            for card in ennemy_player.frontrow:
                card.take_damage(dmg)
        elif self.name == "Plumeau d'Ihstar":
            for card in ennemy_player.backrow:
                card.pv = 0
        elif self.name == "Sur la planche":
            if len(ennemy_player.frontrow) > 0:
                target = random.choice(ennemy_player.frontrow)
                target.pv = 0
        elif self.name == "Zap":
            target.take_damage(2)
            if active_player.inspiration:
                ennemy_player.take_damage(2)
        elif self.name == "Poignard":
            target.buff(2, 0)
        elif self.name == "Potion de fer":
            target.buff(0, 2)
        elif self.name == "Engelure":
            target.silence()
            target.paralyse = True
        elif self.name == "Humilité":
            target.atk = 1

