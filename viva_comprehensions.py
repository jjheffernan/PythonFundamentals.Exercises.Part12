from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Generates list based off input. ascending order of even or odd based upon parity

    :param start: start number based
    :param stop: number to end list, be careful not to go too big
    :param parity: determines even or odd numbers in list
    :return:
    """
    if parity == Parity.EVEN:
        # out_list = [(x+2) for x in range(start, stop)]
        # tried to use list comprehensions
        out_list = []
        for x in range(start, stop + 1):
            # out_list = [(x + 2) for x in range(start, stop + 1)]
            if x == 0:
                out_list.append(x)
            elif x % 2 == 0:
                out_list.append(x)
    elif parity == Parity.ODD:
        out_list = []
        for x in range(start, stop):
            # out_list = [(x + 2) for x in range(start, stop + 1)]
            if x % 2 != 0:
                out_list.append(x)
    return out_list

    # pass  # escape return


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Generates dict based off of input numbers and strategy. List is in ascending order based upon strategy
    The key index is what is used to generate the value number

    :param start: starting number in index
    :param stop:
    :param strategy: how should the list iterate (ex x **2 for x^2)
    :return:
    """
    # out_dict = dict((start, strategy(start)))
    out_dict = {x: strategy(x) for x in range(start, stop)}
    return out_dict
    pass  # escape return


def gen_set(val_in: str) -> Set:
    """
    Generates set based off of input strings.

    :param val_in: tuple of input letters.
    :return:
    """
    pass
