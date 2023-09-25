HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    # test case: 888 88 8
def num_eights(pos):
    if (pos % 10 == 8):
        return num_eights(pos // 10) + 1
    elif (pos > 0):
        return num_eights(pos // 10)
    else:
        return 0


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    # index: 10 -> 6
    # 10 ... 8, 9 
    # 6  ... 8, 7

    # 9 ... 7, 8
    #   ... 7, 8

    # def helper(m, inc, n):
    #     val = 0
    #     while (m <= n):
    #         if inc:
    #             val += 1
    #         else:
    #             val -= 1
    #         if m % 8 == 0 or num_eights(m) > 0:
    #             inc = not(inc)
    #         m += 1
    #     return val

    def helper(m, inc, val):
        if m == n:
            return val
        elif m % 8 == 0 or num_eights(m) > 0:
            return helper(m + 1, -inc, val - inc)
        else:
            return helper(m + 1, inc, val + inc)
            
    return helper(1, 1, 1)


def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    # 1, 5, 10, 25
    def helper(n = change, m = 25):
        if n < m and m != 1:
            return helper(n, next_smaller_coin(m))
        else:
            if n == 0:
                return 1
            elif m == 1:
                return 1
            else:
                return helper(n - m, m) + helper(n, next_smaller_coin(m))
    return helper(change)
