"""Test
>>> count_possible_decodings('11')   #aa, k
2
>>> count_possible_decodings('111')  #aaa, ak, ka
3
>>> count_possible_decodings('1111') #aaaa, aak, aka, kaa, kk
5
>>> count_possible_decodings('2726') #bgbf, bgz
2
"""


def count_possible_decodings(message :str) -> int:
    """ Get The number of possilbe deconings for a encoded message.

    The coding mapping is: a : 1, b : 2, ... z : 26
    """
    if not message:
        return 1
    # get every single position as one possible.
    num =  count_possible_decodings(message[1:])
    # the possible 2 char branch adds one possiblility
    if len(message) >= 2 and int(message[:2]) <= 26:
        num += count_possible_decodings(message[2:])
    return num

if __name__ == "__main__":
    import doctest
    doctest.testmod()
