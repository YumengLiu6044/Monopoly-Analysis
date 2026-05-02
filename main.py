from enum import Enum
import random
from typing import List

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

    BOARD_TEMPLATE = [
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

    CHANCE_CARDS = [
        lambda pos: BoardSpace.BOARDWALK.value,  # 1. Boardwalk
        lambda pos: BoardSpace.GO.value,  # 2. GO
        lambda pos: BoardSpace.ILLINOIS_AVENUE.value,  # 3. Illinois Ave
        lambda pos: BoardSpace.ST_CHARLES_PLACE.value,  # 4. St. Charles Place
        lambda pos: Monopoly.next_railroad(pos),  # 5. Nearest Railroad
        lambda pos: Monopoly.next_railroad(pos),  # 6. Nearest Railroad
        lambda pos: Monopoly.next_utility(pos),  # 7. Nearest Utility
        lambda pos: pos,  # 8. +$50 (no move)
        lambda pos: pos,  # 9. Get Out of Jail Free
        lambda pos: (pos - 3 + len(Monopoly.BOARD_TEMPLATE)) % len(Monopoly.BOARD_TEMPLATE),  # 10. Go back 3
        lambda pos: BoardSpace.JAIL.value,  # 11. Go to Jail
        lambda pos: pos,  # 12. Repairs
        lambda pos: pos,  # 13. Pay $15
        lambda pos: BoardSpace.READING_RAILROAD.value,  # 14. Reading RR
        lambda pos: pos,  # 15. Pay players
        lambda pos: pos,  # 16. +$150
    ]

    COMMUNITY_CHEST_CARDS = [
        lambda pos: BoardSpace.GO.value,  # 1. GO
        lambda pos: pos,  # 2. +$200
        lambda pos: pos,  # 3. Pay $50
        lambda pos: pos,  # 4. +$50
        lambda pos: pos,  # 5. Get Out of Jail Free
        lambda pos: BoardSpace.JAIL.value,  # 6. Go to Jail
        lambda pos: pos,  # 7. +$100
        lambda pos: pos,  # 8. +$20
        lambda pos: pos,  # 9. Birthday
        lambda pos: pos,  # 10. +$100
        lambda pos: pos,  # 11. Pay $100
        lambda pos: pos,  # 12. Pay $50
        lambda pos: pos,  # 13. +$25
        lambda pos: pos,  # 14. Repairs
        lambda pos: pos,  # 15. +$10
        lambda pos: pos,  # 16. +$100
    ]

    JAIL_TURN_LIMIT = 3
    ALL_EQUAL_JAIL_TURNS = 3

    @staticmethod
    def next_railroad(pos: int) -> int:
        railroads = [
            BoardSpace.READING_RAILROAD.value,
            BoardSpace.PENNSYLVANIA_RAILROAD.value,
            BoardSpace.B_AND_O_RAILROAD.value,
            BoardSpace.SHORT_LINE_RAILROAD.value,
        ]
        for r in railroads:
            if r > pos:
                return r
        return railroads[0]

    @staticmethod
    def next_utility(pos: int) -> int:
        utilities = [
            BoardSpace.ELECTRIC_COMPANY.value,
            BoardSpace.WATER_WORKS.value,
        ]
        for u in utilities:
            if u > pos:
                return u
        return utilities[0]

    def __init__(self):
        self.board_index = 0

        self.BOARD = Monopoly.BOARD_TEMPLATE.copy()

        # Init chance and community chest decks
        random.shuffle(self.CHANCE_CARDS)
        random.shuffle(self.COMMUNITY_CHEST_CARDS)

        self.chance_index = 0
        self.community_chest_index = 0

        # Init jail index
        jail_space = MonopolySpace(BoardSpace.JAIL, SpaceType.JAIL)
        if self.BOARD.count(jail_space) != 1:
            raise ValueError("Jail space count is not 1")

        self.jail_index = self.BOARD.index(jail_space)

        # Init jail turn counter
        self.is_in_jail = False
        self.jail_visit_counter = 0

    @staticmethod
    def roll_dice() -> tuple[List[int], bool]:
        rolls = [
            random.randint(1, Monopoly.DICE_FACES)
            for _ in range(Monopoly.DICE_COUNT)
        ]
        all_equal = all(roll == rolls[0] for roll in rolls)
        return rolls, all_equal

    def go_to_jail(self):
        self.is_in_jail = True
        self.jail_visit_counter = 0
        self.board_index = self.jail_index

    def take_turn(self):
        current_space = self.BOARD[self.board_index]
        rolls, all_equal = self.roll_dice()
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
            all_equal_turn_counter = 1
            while all_equal:
                all_equal_turn_counter += 1
                rolls, all_equal = self.roll_dice()

                if all_equal_turn_counter >= Monopoly.ALL_EQUAL_JAIL_TURNS:
                    self.go_to_jail()
                    return


        self.board_index = (self.board_index + sum(rolls)) % len(self.BOARD)
        next_space = self.BOARD[self.board_index]
        match next_space.space_type:
            case SpaceType.CHANCE:
                result = self.CHANCE_CARDS[self.chance_index](self.board_index)
                if result != self.board_index:
                    next_space.counter += 1
                    if result == BoardSpace.JAIL.value:
                        self.go_to_jail()
                    else:
                        self.board_index = result
                self.chance_index = (self.chance_index + 1) % len(self.CHANCE_CARDS)

            case SpaceType.COMMUNITY_CHEST:
                result = self.COMMUNITY_CHEST_CARDS[self.community_chest_index](self.board_index)
                if result != self.board_index:
                    next_space.counter += 1
                    if result == BoardSpace.JAIL.value:
                        self.go_to_jail()
                    else:
                        self.board_index = result
                self.community_chest_index = (self.community_chest_index + 1) % len(self.COMMUNITY_CHEST_CARDS)

            case SpaceType.GO_TO_JAIL:
                next_space.counter += 1
                self.go_to_jail()

    def run(self, turns: int):
        for _ in range(turns):
            self.take_turn()
