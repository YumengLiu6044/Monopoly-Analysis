from enum import Enum
import random
from typing import List
import pprint

SEED = 12345
random.seed(SEED)

class SpaceType(Enum):
    GO = "go"
    PROPERTY = "property"
    RAILROAD = "railroad"
    UTILITY = "utility"
    TAX = "tax"
    CHANCE = "chance"
    COMMUNITY_CHEST = "community_chest"
    JAIL = "jail"
    GO_TO_JAIL = "go_to_jail"
    FREE_PARKING = "free_parking"


class BoardSpace(Enum):
    GO = 0
    MEDITERRANEAN_AVENUE = 1
    COMMUNITY_CHEST_1 = 2
    BALTIC_AVENUE = 3
    INCOME_TAX = 4
    READING_RAILROAD = 5
    ORIENTAL_AVENUE = 6
    CHANCE_1 = 7
    VERMONT_AVENUE = 8
    CONNECTICUT_AVENUE = 9

    JAIL = 10
    ST_CHARLES_PLACE = 11
    ELECTRIC_COMPANY = 12
    STATES_AVENUE = 13
    VIRGINIA_AVENUE = 14
    PENNSYLVANIA_RAILROAD = 15
    ST_JAMES_PLACE = 16
    COMMUNITY_CHEST_2 = 17
    TENNESSEE_AVENUE = 18
    NEW_YORK_AVENUE = 19

    FREE_PARKING = 20
    KENTUCKY_AVENUE = 21
    CHANCE_2 = 22
    INDIANA_AVENUE = 23
    ILLINOIS_AVENUE = 24
    B_AND_O_RAILROAD = 25
    ATLANTIC_AVENUE = 26
    VENTNOR_AVENUE = 27
    WATER_WORKS = 28
    MARVIN_GARDENS = 29

    GO_TO_JAIL = 30
    PACIFIC_AVENUE = 31
    NORTH_CAROLINA_AVENUE = 32
    COMMUNITY_CHEST_3 = 33
    PENNSYLVANIA_AVENUE = 34
    SHORT_LINE_RAILROAD = 35
    CHANCE_3 = 36
    PARK_PLACE = 37
    LUXURY_TAX = 38
    BOARDWALK = 39


class MonopolySpace:
    def __init__(self, space: BoardSpace, space_type: SpaceType):
        self.space = space
        self.space_type = space_type
        self.counter = 0

        if space_type == SpaceType.JAIL:
            self.is_in_jail_counter = 0

    @property
    def is_property(self):
        return self.space_type in {SpaceType.PROPERTY, SpaceType.RAILROAD, SpaceType.UTILITY}

    @property
    def is_chance(self):
        return self.space_type == SpaceType.CHANCE

    @property
    def is_community_chest(self):
        return self.space_type == SpaceType.COMMUNITY_CHEST

    @property
    def is_go_to_jail(self):
        return self.space_type == SpaceType.GO_TO_JAIL

    @property
    def is_jail(self):
        return self.space_type == SpaceType.JAIL

    def __repr__(self):
        return (f"MonopolySpace("
                f"space='{self.space.name}', "
                f"type={self.space_type.value}, "
                f"counter={self.counter}, "
                f"in_jail_counter={self.is_in_jail_counter if self.is_jail else None}"
                f")")

    def __eq__(self, other):
        if not isinstance(other, MonopolySpace):
            raise TypeError(f"Cannot compare {type(self)} and {type(other)}")

        return self.space == other.space

class Monopoly:
    DICE_FACES = 6
    DICE_COUNT = 2

    BOARD = [
        MonopolySpace(BoardSpace.GO, SpaceType.GO),
        MonopolySpace(BoardSpace.MEDITERRANEAN_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.COMMUNITY_CHEST_1, SpaceType.COMMUNITY_CHEST),
        MonopolySpace(BoardSpace.BALTIC_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.INCOME_TAX, SpaceType.TAX),
        MonopolySpace(BoardSpace.READING_RAILROAD, SpaceType.RAILROAD),
        MonopolySpace(BoardSpace.ORIENTAL_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.CHANCE_1, SpaceType.CHANCE),
        MonopolySpace(BoardSpace.VERMONT_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.CONNECTICUT_AVENUE, SpaceType.PROPERTY),

        MonopolySpace(BoardSpace.JAIL, SpaceType.JAIL),
        MonopolySpace(BoardSpace.ST_CHARLES_PLACE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.ELECTRIC_COMPANY, SpaceType.UTILITY),
        MonopolySpace(BoardSpace.STATES_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.VIRGINIA_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.PENNSYLVANIA_RAILROAD, SpaceType.RAILROAD),
        MonopolySpace(BoardSpace.ST_JAMES_PLACE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.COMMUNITY_CHEST_2, SpaceType.COMMUNITY_CHEST),
        MonopolySpace(BoardSpace.TENNESSEE_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.NEW_YORK_AVENUE, SpaceType.PROPERTY),

        MonopolySpace(BoardSpace.FREE_PARKING, SpaceType.FREE_PARKING),
        MonopolySpace(BoardSpace.KENTUCKY_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.CHANCE_2, SpaceType.CHANCE),
        MonopolySpace(BoardSpace.INDIANA_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.ILLINOIS_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.B_AND_O_RAILROAD, SpaceType.RAILROAD),
        MonopolySpace(BoardSpace.ATLANTIC_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.VENTNOR_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.WATER_WORKS, SpaceType.UTILITY),
        MonopolySpace(BoardSpace.MARVIN_GARDENS, SpaceType.PROPERTY),

        MonopolySpace(BoardSpace.GO_TO_JAIL, SpaceType.GO_TO_JAIL),
        MonopolySpace(BoardSpace.PACIFIC_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.NORTH_CAROLINA_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.COMMUNITY_CHEST_3, SpaceType.COMMUNITY_CHEST),
        MonopolySpace(BoardSpace.PENNSYLVANIA_AVENUE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.SHORT_LINE_RAILROAD, SpaceType.RAILROAD),
        MonopolySpace(BoardSpace.CHANCE_3, SpaceType.CHANCE),
        MonopolySpace(BoardSpace.PARK_PLACE, SpaceType.PROPERTY),
        MonopolySpace(BoardSpace.LUXURY_TAX, SpaceType.TAX),
        MonopolySpace(BoardSpace.BOARDWALK, SpaceType.PROPERTY),
    ]

    CHANCE_DECK_SIZE = 16
    CHANCE_JAIL_CARD_COUNT = 1

    COMMUNITY_CHEST_DECK_SIZE = 16
    COMMUNITY_CHEST_JAIL_CARD_COUNT = 1

    JAIL_TURN_LIMIT = 3
    ALL_EQUAL_JAIL_TURNS = 3

    def __init__(self):
        # Init board
        for space in Monopoly.BOARD:
            space.counter = 0
            if space.is_jail:
                space.is_in_jail_counter = 0

        self.board_index = 0

        # Init chance and community chest decks
        self.chance_deck = [
            False if i >= self.CHANCE_JAIL_CARD_COUNT else True
            for i in range(self.CHANCE_DECK_SIZE)
        ]
        self.community_chest_deck = [
            False if i >= self.COMMUNITY_CHEST_JAIL_CARD_COUNT else True
            for i in range(self.COMMUNITY_CHEST_DECK_SIZE)
        ]
        random.shuffle(self.chance_deck)
        random.shuffle(self.community_chest_deck)

        self.chance_index = 0
        self.community_chest_index = 0

        # Init jail index
        jail_space = MonopolySpace(BoardSpace.JAIL, SpaceType.JAIL)
        if Monopoly.BOARD.count(jail_space) != 1:
            raise ValueError("Jail space count is not 1")

        self.jail_index = self.BOARD.index(jail_space)

        # Init jail turn counter
        self.is_in_jail = False
        self.jail_visit_counter = 0
        self.all_equal_turn_counter = 0

    @staticmethod
    def roll_dice() -> List[int]:
        return [random.randint(1, Monopoly.DICE_FACES) for _ in range(Monopoly.DICE_COUNT)]

    def go_to_jail(self):
        self.is_in_jail = True
        self.jail_visit_counter = 0
        self.all_equal_turn_counter = 0
        self.board_index = self.jail_index

    def take_turn(self):
        current_space = self.BOARD[self.board_index]
        rolls = self.roll_dice()
        all_equal = all(roll == rolls[0] for roll in rolls)
        current_space.counter += 1

        # Determine the next space based on rolls or jail state
        if self.is_in_jail:
            current_space.is_in_jail_counter += 1

            if current_space.is_in_jail_counter >= Monopoly.JAIL_TURN_LIMIT or all_equal:
                self.is_in_jail = False
                self.jail_visit_counter = 0
            else:
                self.jail_visit_counter += 1
                return
        else:
            if all_equal:
                self.all_equal_turn_counter += 1
                if self.all_equal_turn_counter >= Monopoly.ALL_EQUAL_JAIL_TURNS:
                    self.go_to_jail()
                return
            else:
                self.all_equal_turn_counter = 0

        self.board_index = (self.board_index + sum(rolls)) % len(Monopoly.BOARD)
        next_space = self.BOARD[self.board_index]

        if next_space.is_chance:
            chance_card_is_jail = self.chance_deck[self.chance_index]
            if chance_card_is_jail:
                next_space.counter += 1
                self.go_to_jail()
            self.chance_index = (self.chance_index + 1) % self.CHANCE_DECK_SIZE

        if next_space.is_community_chest:
            community_chest_card_is_jail = self.community_chest_deck[self.community_chest_index]
            if community_chest_card_is_jail:
                next_space.counter += 1
                self.go_to_jail()
            self.community_chest_index = (self.community_chest_index + 1) % self.COMMUNITY_CHEST_DECK_SIZE

        if next_space.is_go_to_jail:
            next_space.counter += 1
            self.go_to_jail()

    def run(self, turns: int):
        for _ in range(turns):
            self.take_turn()


if __name__ == "__main__":
    monopoly = Monopoly()
    monopoly.run(100000)
    pprint.pprint(sorted(monopoly.BOARD, key=lambda x: x.counter, reverse=True))