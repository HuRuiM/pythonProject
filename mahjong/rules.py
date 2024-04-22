def winCheck(hand):
    # 判断是否有14张牌
    if len(hand) != 14:
        return False

    # 判断是否有对子
    for i in set(hand):
        if hand.count(i) >= 2:
            temp_hand = hand.copy()
            temp_hand.remove(i)
            temp_hand.remove(i)
            # 开始判断剩下的12张牌是否符合胡牌要求
            # 初始化字典，存放不同牌值的数量
            count_dict = {}
            for j in temp_hand:
                if j not in count_dict:
                    count_dict[j] = 1
                else:
                    count_dict[j] += 1
            # 遍历字典值，判断是否能凑成顺子和刻子
            kezi_count = 0
            shunzi_count = 0
            for count in count_dict.values():
                if count >= 3:
                    kezi_count += count // 3
                if count - 1 in count_dict and count - 2 in count_dict:
                    shunzi_count += 1
            # 若刻子数量加顺子数量为4，则满足胡牌条件
            if kezi_count + shunzi_count == 4:
                return True

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
hand = ['bamboo1', 'bamboo1', 'bamboo1', 'wan2', 'wan2', 'wan2', 'circle3', 'circle3', 'circle3', 'circle4', 'circle4', 'circle4', 'red1','red1']
print(winCheck(hand))





