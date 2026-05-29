
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from card_class.fighter import Fighter
    from card_class.structure import Structure

from card_class.card import Card
import random

class Spell(Card):
    def __init__(self, name, cost, target_type, classe, description):
        super().__init__(name, cost, classe, description)
        self.target_type = target_type

    def activate_spell(self, ally_player, ennemy_player, target=None):

        # Marduk
        if self.name == "Cri de guerre":
            for card in ally_player.backrow:
                card.buff(1,0)
            for card in ally_player.frontrow:
                card.buff(1,0)
        elif self.name == "Sang brulant":
            pui = ally_player.get_puissance()
            for row in [ally_player.backrow, ally_player.frontrow, ennemy_player.backrow, ennemy_player.frontrow]:
                for card in row:
                    dmg = (3 if card.pv < card.pv_max else 1) + pui
                    card.take_damage(dmg)
        elif self.name == "Mort proche":
            if target.pv < target.pv_max:
                target.buff(3,3)
        elif self.name == "Boule de feu":
            dmg = 4 + ally_player.get_puissance()
            if target:
                target.take_damage(dmg)
            else:
                ennemy_player.take_damage(dmg)
        elif self.name == "Brevage de la sorcière":
            target.actionable = True
        elif self.name == "Flammes des enfers":
            dmg = 4 + ally_player.get_puissance()
            for row in [ally_player.backrow, ally_player.frontrow, ennemy_player.backrow, ennemy_player.frontrow]:
                for card in row:
                    if card.archetype != "démon":
                        card.take_damage(dmg)

        # Enlil
        elif self.name == "Humilité":
            for card in ennemy_player.frontrow:
                if isinstance(card, Fighter):
                    card.atk = 1
        elif self.name == "Renfort de l'armée":
            ally_player.summon_unit("Recrue", "front")
            ally_player.summon_unit("Recrue", "front")
            ally_player.summon_unit("Recrue", "front")
        elif self.name == "Éclat sysmique":
            if isinstance(target, Structure):
                target.kill()
        elif self.name == "Marteau divin":
            target.take_damage(3 + ally_player.get_puissance())
            ally_player.heal(3)
        elif self.name == "Bénédiction d'Enlil":
            avatar = ally_player.avatar.get("Enlil")
            if avatar.offering():
                _ = avatar.offering()
        elif self.name == "Tempête du désert":
            for row in [ally_player.frontrow, ally_player.backrow, ennemy_player.frontrow, ennemy_player.backrow]:
                for unit in row:
                    if isinstance(unit, Fighter):
                        if unit.atk >= 4:
                            unit.kill()
        elif self.name == "Surpuissance":
            if isinstance(target, Fighter):
                target.atk *= 2
        elif self.name == "Avarice":
            ally_player.draw_card(3)
        elif self.name == "Punition divine":
            ennemy_player.take_damage(8 + ally_player.get_puissance())
        
        # Enki
        elif self.name == "Potion de fer":
            target.buff(0, 2)
        elif self.name == "Coup de bouclier":
            target.take_damage(ally_player.armor)
        elif self.name == "Engelure":
            target.silence()
            target.paralyse = True
        elif self.name == "Salve de flèches":
            dmg = 1 + ally_player.get_puissance()
            for card in ennemy_player.backrow:
                card.take_damage(dmg)
            for card in ennemy_player.frontrow:
                card.take_damage(dmg)
        elif self.name == "Sortilège de mort":
            if target.atk <= 3:
                target.kill()
        elif self.name == "Nova de givre":
            for card in ennemy_player.backrow:
                card.paralyse = True
            for card in ennemy_player.frontrow:
                card.paralyse = True
        elif self.name == "Intelligence":
            ally_player.draw_card(2)
        elif self.name == "Pluie torrentielle":
            for row in [ennemy_player.backrow, ennemy_player.frontrow]:
                for card in row:
                    for _ in range(2 + ally_player.get_puissance()):
                        card.take_damage(1)
        elif self.name == "Soufle d'Absu":
            pass
        elif self.name == "Formation de combat":
            for _ in range(4):
                ally_player.summon_unit("Lancier", "front")
        
        # Ishtar
        elif self.name == "Serres de vautour":
            target.take_damage(2 + ally_player.get_puissance())
        elif self.name == "Fouet d'Ishtar":
            pass
        elif self.name == "Lien bestial":
            if target.archetype == "bête":
                if ally_player.rage_ishtar:
                    target.buff(2, 2)
                else:
                    target.buff(1, 1)
        elif self.name == "Apaisement":
            if ally_player.rage_ishtar:
                ally_player.heal(5)
                ally_player.rage_ishtar = False
        elif self.name == "Déchirement":
            ally_player.take_damage(2, active=True)
            ally_player.draw_card(2)
        elif self.name == "Instinct bestial":
            for _ in range(2):
                if len(ally_player.deck) > 0:
                    if isinstance(ally_player.deck[0], Fighter):
                        ally_player.draw_card(1, reduce_cost=1)
                    else:
                        ally_player.discard.append(ally_player.deck.pop(0))
        elif self.name == "Rugissement sauvage":
            pass
        elif self.name == "Tir reflexe":
            target.take_damage(3 + ally_player.get_puissance())
            if target.pv <= 0:
                ally_player.draw_card(1)
        elif self.name == "Déplumage":
            pass
        elif self.name == "Furie d'Ishtar":
            if ally_player.rage_ishtar:
                ennemy_player.take_damage(4 + ally_player.get_puissance())
            else:
                ennemy_player.take_damage(6 + ally_player.get_puissance())
        elif self.name == "Tir de barrage":
            pass
        

        # Alchimiste
        elif self.name == "Concentration":
            used_mana = ally_player.max_mana_turn - ally_player.basic_mana
            ally_player.extra_mana += min(2, used_mana)
        elif self.name == "Comète":
            dmg = 2 + ally_player.get_puissance()
            if target:
                target.take_damage(dmg)
            else:
                ennemy_player.take_damage(dmg)
        elif self.name == "Idole de jade":
            ally_player.hand.append(ally_player.create_card("Colosse de jade"))
            if ally_player.max_mana_turn < 8:
                ally_player.hand.append(ally_player.create_card("Colosse de jade"))
                ally_player.hand.append(ally_player.create_card("Colosse de jade"))
        elif self.name == "Floraison":
            ally_player.max_mana_turn += 1
        elif self.name == "Marque de la forêt":
            target.buff(2, 2)
            target.protecteur = True
        elif self.name == "Écorce":
            if len(ally_player.deck) > 0:
                if isinstance(ally_player.deck[0], Spell):
                    ally_player.gain_armor(3)
            ally_player.draw_card(1)
        elif self.name == "Régénération":
            ally_player.heal(6)
        elif self.name == "Fiole explosive":
            target.take_damage(5 + ally_player.get_puissance())
        elif self.name == "Ronces paralysantes":
            for card in ennemy_player.backrow:
                card.paralyse = True
                card.buff(-1, -1)
            for card in ennemy_player.frontrow:
                card.paralyse = True
                card.buff(-1, -1)
        elif self.name == "Force de la nature":
            ally_player.gain_armor(4)
            ally_player.draw_card(2)
        elif self.name == "Revanche de la forêt":
            target.kill()
            if ally_player.inspiration:
                ally_player.summon_unit("Tréant", "front")

        # Kraken
        elif self.name == "Pluie de balles":
            dmg = 1 + ally_player.get_puissance()
            for card in ally_player.frontrow:
                card.take_damage(dmg)
            for card in ennemy_player.frontrow:
                card.take_damage(dmg)
            ally_player.draw_card(1)
        elif self.name == "Pack d'assemblage":
            ally_player.draw_car(1, Structure, "tourelle", 1)
        elif self.name == "Sur la planche":
            if len(ennemy_player.frontrow) > 0:
                target = random.choice(ennemy_player.frontrow)
                target.kill()
        elif self.name == "Tentacules déchainées":
            pass
        elif self.name == "Corrosion":
            ennemy_player.armor = max(0, ennemy_player.armor - 3)
            ennemy_player.take_damage(3 + ally_player.get_puissance())
        elif self.name == "Descente dans les abysses":
            pass

        # Inconnu
        elif self.name == "Rune contrefaite":
            ally_player.gain_mana(1)
        elif self.name == "Rayon ténébreux":
            dmg = 3 + ally_player.get_puissance()
            if target:
                target.take_damage(dmg)
            else:
                ennemy_player.take_damage(dmg)
        elif self.name == "Chapardage":
            pass
        elif self.name == "Laché de dominos":
            pass
        elif self.name == "Rebondissement":
            pass
        elif self.name == "Tarot":
            pass
        elif self.name == "Sournoiserie":
            target.kill()
            if len(ally_player.hand) > 0:
                card = random.choice(ally_player.hand)
                ally_player.hand.remove(card)
                ally_player.discard.append(card)
        elif self.name == "Métamorphose":
            if target in ennemy_player.backrow:
                ennemy_player.backrow.remove(target)
                ennemy_player.summon_unit("Grenouille", "back")
            elif target in ennemy_player.frontrow:
                ennemy_player.frontrow.remove(target)
                ennemy_player.summon_unit("Grenouille", "front")
        elif self.name == "Spores":
            pass
        elif self.name == "Cataclysme":
            pass
        elif self.name == "Crane de Nergal":
            ally_player.draw_car(3, Fighter, "démon", 1)
        elif self.name == "Controle mental":
            pass

        # Thot
        elif self.name == "Écran de fumée":
            pass
        elif self.name == "Vision de l'au-delà":
            target.kill()
            ally_player.draw_card(2)
        elif self.name == "Dague tranchante":
            target.buff(2, 0)
        elif self.name == "Clepsydre":
            ally_player.clepsydre = True
        elif self.name == "Éclair foudroyant":
            target.take_damage(3 + ally_player.get_puissance())
            target.paralyse = True
        elif self.name == "Piège à ressort":
            pass
        elif self.name == "Poussière temporelle":
            target.take_damage(2 + ally_player.get_puissance())
            if target.pv <= 0:
                ally_player.gain_mana(2)
        elif self.name == "Baton du magicien":
            if target.archetype == "mage":
                target.buff(1,1)
                ally_player.hand.append(ally_player.create_card(target.name))
        elif self.name == "Trait de la mort":
            if target in ennemy_player.backrow:
                for unit in ennemy_player.backrow:
                    unit.take_damage(3 + ally_player.get_puissance())
            elif target in ennemy_player.frontrow:
                for unit in ennemy_player.frontrow:
                    unit.take_damage(3 + ally_player.get_puissance())
        elif self.name == "Aspiration d'âme":
            if target in ennemy_player.backrow:
                ennemy_player.backrow.remove(target)
            elif target in ennemy_player.frontrow:
                ennemy_player.frontrow.remove(target)
        elif self.name == "Rembobinage":
            pass
        elif self.name == "Néant":
            for row in [ally_player.frontrow, ally_player.backrow, ennemy_player.frontrow, ennemy_player.backrow]:
                for unit in row:
                    unit.kill()
        elif self.name == "Tablette de la destinée":
            ally_player.heal(10)

        # Extra
        elif self.name == "Crochet":
            if target.archetype == "pirate":
                target.buff(1, 0)
        elif self.name == "Torche enflammée":
            ennemy_player.take_damage(3 + ally_player.get_puissance())
        
