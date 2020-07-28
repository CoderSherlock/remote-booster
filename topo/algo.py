import timeit


####################################################################################################
def group_helper_v2(remain_worker: int, cur_list: list, last_max_number: int) -> list:
    global ret_list
    if (remain_worker < 0):
        return -1

    if (remain_worker == 0):
        ret_list.append(cur_list)
    
    for i in range(1, last_max_number + 1):
        tmp_list = cur_list[:]
        tmp_list.append(i)
        group_helper_v2(remain_worker - i, tmp_list, i)

def all_groups_v2(worker_amount: int) -> list:
    global ret_list
    ret_list = []
    group_helper_v2(worker_amount, [], worker_amount)
    return ret_list[:]

def group_helper(remain_worker: int, remain_group: int, cur_list: list) -> list:
    global ret_list
    if (remain_worker <= 0 and remain_group > 0):
        return -1
    if (remain_worker <= 0 and remain_group <= 0):
        # print(cur_list)
        ret_list.append(cur_list)
        return 0
    if (remain_group <= 0):
        return -1
    if (remain_group > remain_worker):
        return -1

    for i in range(1, remain_worker + 1):
        tmp_list = cur_list[:]
        tmp_list.append(i)
        group_helper(remain_worker - i, remain_group - 1, tmp_list)

    return 0


ret_list = []


def group(worker_amount: int, group_amount: int):
    global ret_list
    group_helper(worker_amount, group_amount, [])
    ret = ret_list[:]
    ret_list = []
    for i in ret:
        i.sort(reverse=True)
    return [list(x) for x in set(tuple(x) for x in ret)]


def all_groups(worker_amount: int) -> list:
    ret = []
    for i in range(1, worker_amount + 1):
        ret += group(worker_amount, i)
    return ret

####################################################################################################


def time_bias(level: int, children_amount: int) -> float:
    if (level == 0):
        if children_amount <= 4:
            return 0.3
        elif children_amount <= 5:
            return 0.35
        else:
            return 0.8
    else:
        if children_amount <= 5:
            return 0.3
        elif children_amount <= 6:
            return 0.35
        else:
            return 0.8


def caculate_ce(group: list, bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / bandwidth
    top_level_amount = len(group)
    top_level_trans_time = top_level_amount * \
        trans_time_rate  # * time_bias(0, top_level_amount)

    ce = float(0)
    for s in group:
        if (s == 1):
            s_ce = s / (top_level_trans_time * 2 + mill_time + train_time)
            # print(s_ce)
            ce += s_ce
        else:
            bottom_level_amount = s - 1
            bottom_level_trans_time = bottom_level_amount * \
                trans_time_rate  # * time_bias(1, bottom_level_amount)
            s_ce = s / ((top_level_trans_time + bottom_level_amount)
                        * 2 + mill_time * 2 + train_time)
            # print(s_ce)
            ce += s_ce

    return ce

def caculate_ce_v2(group: list, inbound_bandwidth: float, outbound_bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / 2 / inbound_bandwidth + parameter_size / 2 / outbound_bandwidth
    top_level_amount = len(group)
    top_level_trans_time = top_level_amount * \
        trans_time_rate  # * time_bias(0, top_level_amount)

    ce = float(0)
    for s in group:
        if (s == 1):
            s_ce = s / (top_level_trans_time * 2 + mill_time + train_time)
            # print(s_ce)
            ce += s_ce
        else:
            bottom_level_amount = s - 1
            bottom_level_trans_time = bottom_level_amount * \
                trans_time_rate  # * time_bias(1, bottom_level_amount)
            s_ce = s / ((top_level_trans_time + bottom_level_amount)
                        * 2 + mill_time * 2 + train_time)
            # print(s_ce)
            ce += s_ce

    return ce

def caculate_ce_v3(group: list, inbound_bandwidth: float, outbound_bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / 2 / inbound_bandwidth + parameter_size / 2 / outbound_bandwidth
    top_level_amount = len(group)
    top_level_trans_time = top_level_amount * \
        trans_time_rate  # * time_bias(0, top_level_amount)

    ce = float(0)
    for s in group:
        if (s == 1):
            s_ce = s / (top_level_trans_time * 2 + mill_time + train_time)
            # print(s_ce)
            ce += s_ce
        else:
            bottom_level_amount = s - 1
            bottom_level_trans_time = bottom_level_amount * \
                trans_time_rate  # * time_bias(1, bottom_level_amount)
            s_ce = s / ((top_level_trans_time + bottom_level_amount)
                        * 2 + mill_time * 2 + train_time)
            # print(s_ce)
            ce += s_ce

    return ce

####################################################
# 50 Mbps
# [2,2,2,1,1] 133.556
# [3,2,1,1,1] 134.871
# [3,2,2,1] 135.444
# [3,3,1,1] 135.599
# ------------------------
# [4,2,1,1] 140.824
# [2,2,2,2] 141.158
# [2,2,1,1,1,1] 141.301
# [3,1,1,1,1,1] 142.571
# [5,1,1,1] 142.751
# [4,1,1,1,1] 142.912
# [3,3,2] 144.108
# -------------------------
# [2,1,1,1,1,1,1] 146.214
# [4,3,1] 146.329
# [4,2,2] 148.557
# [4,4] 160.296
# [6,1,1] 161.719
####################################################


if __name__ == "__main__":
    #  tmp_ending_epoch = [51, 84, 110, 116, 105, 141, 177, 194]
    #  tmp_ending_epoch = [3, 5, 6, 7, 8, 10, 11, 12]
    ce_table = []
    for w in range(8, 9):
        start = timeit.default_timer()
        gs = all_groups_v2(w)
        end = timeit.default_timer()
        print("Generate time: {0}".format(end - start))
        print(len(gs))
        start = timeit.default_timer()
        for g in gs:
            if(len(g)>8):
                continue
            ce_table.append((52/caculate_ce_v2(g, 100, 100, 25.6, 0.08, 1.15), g))
        end = timeit.default_timer()
        print("Calculate time: {0}".format(end - start))
        start = timeit.default_timer()

    #  ce_table.sort(reverse=True)
    ce_table.sort()
    end = timeit.default_timer()
    print("Sort time: {0}".format(end - start))

    len_list = []
    for v, k in ce_table:
        if (len(k) in len_list):
            continue
        if (len(k) > 8):
            continue
        else:
            print(len(k), k, v)
            len_list.append(len(k))
