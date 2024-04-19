def winCheck(hand):
    # 统计手牌中每种牌的数量
    hand_dict = {}
    for tile in hand:
        if tile in hand_dict:
            hand_dict[tile] += 1
        else:
            hand_dict[tile] = 1

    # 如果手里的牌数量不是 14 张，无法胡牌
    if len(hand) != 14:
        return False

    # 遍历所有可能的将牌（对子），尝试从手牌中去除对子判断是否可以胡牌
    for pair in hand_dict:
        if hand_dict[pair] >= 2:
            hand_dict[pair] -= 2
            if canWin(hand_dict):
                return True
            hand_dict[pair] += 2

    return False


# 辅助函数，递归判断是否可以胡牌
def canWin(hand_dict):
    if sum(hand_dict.values()) == 0:
        return True

    # 逐个尝试将手牌中的顺子、刻子和杠子移除，然后继续递归判断
    for key in list(hand_dict.keys()):
        if hand_dict[key] >= 3:
            hand_dict[key] -= 3
            if canWin(hand_dict):
                return True
            hand_dict[key] += 3

        if key + 1 in hand_dict and key + 2 in hand_dict:
            hand_dict[key] -= 1
            hand_dict[key + 1] -= 1
            hand_dict[key + 2] -= 1
            if canWin(hand_dict):
                return True
            hand_dict[key] += 1
            hand_dict[key + 1] += 1
            hand_dict[key + 2] += 1
    return False
def gangCheck(hand):
    # 杠牌检查
    if len(hand) % 3 != 0:
        return False

    # 统计每种牌的数量
    count = {}
    for tile in hand:
        if tile not in count:
            count[tile] = 1
        else:
            count[tile] += 1

    # 判断是否有四张相同的牌
    for num in count.values():
        if num == 4:
            return True

    return False
def pengCheck(hand):
    # 碰牌检查
    if len(hand) % 3 != 0:
        return True

    # 统计每种牌的数量
    count = {}
    for tile in hand:
        if tile not in count:
            count[tile] = 1
        else:
            count[tile] += 1

    # 判断是否有三张相同的牌
    for num in count.values():
        if num == 3:
            return True
    return False
hand=[]
print(winCheck(hand))






