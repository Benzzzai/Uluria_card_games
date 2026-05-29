from player import Player
from card_class.fighter import Fighter
from card_class.structure import Structure
from card_class.spell import Spell
from card_class.ritual import Ritual

class Game:
    def __init__(self, deck_name_1, deck_name_2):
        self.player_1 = Player(deck_name_1)
        self.player_2 = Player(deck_name_2)
        self.turn = 1
        self.active_player = self.player_1
        self.ennemy_player = self.player_2
        self.active_player.draw_card()

    def change_turn(self):
        self.active_player.end_turn(self.ennemy_player)

        if self.active_player == self.player_1:
            self.active_player = self.player_2
            self.ennemy_player = self.player_1
        else:
            self.active_player = self.player_1
            self.ennemy_player = self.player_2
        self.turn += 1

        self.active_player.start_turn(self.ennemy_player)

    def move_with_target(self, selected_card, target_card):
        if selected_card in self.active_player.hand and isinstance(selected_card, Fighter):
            if selected_card.inv_ennemy and (target_card in self.ennemy_player.backrow or target_card in self.ennemy_player.frontrow):
                row = "front" if selected_card.avant_garde else "back"
                self.active_player.play_unit(selected_card, self.ennemy_player, target=target_card, row=row)
            elif selected_card.inv_ally and target_card in self.active_player.frontrow:
                row = "front" if selected_card.avant_garde else "back"
                pos = self.active_player.frontrow.index(target_card) + 1 if selected_card.avant_garde else 0
                self.active_player.play_unit(selected_card, self.ennemy_player, target=target_card, row=row, pos=pos)
            elif selected_card.avant_garde and target_card in self.active_player.frontrow:
                pos = self.active_player.frontrow.index(target_card) + 1
                self.active_player.play_unit(selected_card, self.ennemy_player, row="front", pos=pos)
            elif target_card in self.active_player.backrow:
                pos = self.active_player.backrow.index(target_card) + 1
                self.active_player.play_unit(selected_card, self.ennemy_player, row="back", pos=pos)
        elif selected_card in self.active_player.backrow and isinstance(selected_card, Fighter) and target_card in self.active_player.frontrow:
            pos = self.active_player.frontrow.index(target_card) + 1
            self.active_player.front_fighter(selected_card, self.ennemy_player, target=target_card, pos=pos)
        elif selected_card in self.active_player.frontrow and isinstance(selected_card, Fighter) and target_card in self.ennemy_player.frontrow:
            self.fight(selected_card, target_card)
        elif selected_card in self.active_player.hand and isinstance(selected_card, Structure):
            if selected_card.row == "front" and target_card in self.active_player.frontrow:
                pos = self.active_player.frontrow.index(target_card) + 1
                self.active_player.play_unit(selected_card, self.ennemy_player, row="front", pos=pos)
            elif selected_card.row == "back" and target_card in self.active_player.backrow:
                pos = self.active_player.backrow.index(target_card) + 1
                self.active_player.play_unit(selected_card, self.ennemy_player, row="back", pos=pos)
        elif selected_card in self.active_player.hand and isinstance(selected_card, Spell):
            if "ally" in selected_card.target_type and (target_card in self.active_player.backrow or target_card in self.active_player.frontrow):
                self.active_player.play_spell(selected_card, self.ennemy_player, target=target_card)
            elif "ennemy" in selected_card.target_type and (target_card in self.ennemy_player.backrow or target_card in self.ennemy_player.frontrow):
                self.active_player.play_spell(selected_card, self.ennemy_player, target=target_card)
        elif selected_card in self.active_player.hand and isinstance(selected_card, Ritual) and target_card in self.active_player.backrow:
            self.active_player.play_ritual(selected_card, target_card, self.ennemy_player)

    def move_without_target(self, selected_card):
        if selected_card in self.active_player.hand and isinstance(selected_card, Fighter):
            row = "front" if selected_card.avant_garde else "back"
            self.active_player.play_unit(selected_card, self.ennemy_player, row=row)
        elif selected_card in self.active_player.backrow and isinstance(selected_card, Fighter):
            self.active_player.front_fighter(selected_card, self.ennemy_player)
        elif selected_card in self.active_player.frontrow and isinstance(selected_card, Fighter):
            self.fight_face(selected_card)
        elif selected_card in self.active_player.hand and isinstance(selected_card, Structure):
            self.active_player.play_unit(selected_card, self.ennemy_player, row=selected_card.row)
        elif selected_card in self.active_player.hand and isinstance(selected_card, Spell):
            if "none" in selected_card.target_type:
                self.active_player.play_spell(selected_card, self.ennemy_player)
        
    def move_back(self, selected_card):
        if selected_card in self.active_player.frontrow:
            self.active_player.back_fighter(selected_card)

    def offering(self, selected_card):
        if selected_card in self.active_player.hand:
            self.active_player.offering(selected_card, self.ennemy_player)

    def fight(self, off_card, def_card):
        if off_card.actionable and not off_card.paralyse:
            if off_card.attaque:
                off_card.activate_attaque(self.active_player, self.ennemy_player)
            def_card.take_damage(off_card.atk)
            if off_card.vol_vie:
                self.active_player.heal(off_card.atk)
            if off_card.percant and (def_card.pv < 0):
                self.ennemy_player.take_damage(-def_card.pv)
            if (off_card.rapide and def_card.pv <= 0) or isinstance(def_card, Structure):
                pass
            else:
                off_card.take_damage(def_card.atk)
            off_card.actionable = False

    def fight_face(self, off_card):
        if off_card.actionable and not off_card.paralyse:
            if off_card.attaque:
                off_card.activate_attaque(self.active_player, self.ennemy_player)
            self.ennemy_player.take_damage(off_card.atk)
            if off_card.vol_vie:
                self.active_player.heal(off_card.atk)
            off_card.actionable = False
            self.active_player.trigger_ishtar = True

    def check_death(self):
        self.active_player.check_death(self.ennemy_player)
        self.ennemy_player.check_death(self.active_player, is_not_turn=True)

    def check_end(self):
        return (self.player_1.health == 0 or self.player_2.health == 0
                or ((self.player_1.is_card_in_hand("Fragment du destin 1")) and (self.player_1.is_card_in_hand("Fragment du destin 2")) and (self.player_1.is_card_in_hand("Fragment du destin 3"))
                    and (self.player_1.is_card_in_hand("Fragment du destin 4")) and (self.player_1.is_card_in_hand("Fragment du destin 5")))
                or ((self.player_2.is_card_in_hand("Fragment du destin 1")) and (self.player_2.is_card_in_hand("Fragment du destin 2")) and (self.player_2.is_card_in_hand("Fragment du destin 3"))
                    and (self.player_2.is_card_in_hand("Fragment du destin 4")) and (self.player_2.is_card_in_hand("Fragment du destin 5"))))