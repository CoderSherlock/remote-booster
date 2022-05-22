import timeit
import random


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

def most_balanced_group(worker_amount: int, cluster_amount: int) -> list:
    # 4 -> [[4], [2,2], [2,1,1], [1,1,1,1]]
    ret = []
    for i in range(cluster_amount, min(worker_amount+1, cluster_amount+1)):
        tmp = []
        for j in range(0, i):
            tmp.append(0)
        tmp_rest_worker = worker_amount
        while(tmp_rest_worker != 0):
            for s in range(0, len(tmp)):
                if(tmp_rest_worker == 0):
                    break
                tmp[s] += 1
                tmp_rest_worker -= 1
        ret.append(tmp)
        # print(tmp)
    return ret


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
    trans_time_rate = parameter_size / inbound_bandwidth + parameter_size / outbound_bandwidth
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

def caculate_ce_v2_1(group: list, inbound_bandwidth: float, outbound_bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / 2 / inbound_bandwidth + parameter_size / 2 / outbound_bandwidth
    top_level_amount = len(group)
    print(group.count(1), len(group), group)
    top_level_trans_time = top_level_amount * \
        trans_time_rate  # * time_bias(0, top_level_amount)

    ce = float(0)
    for s in group:
        if (s == 1):
            s_ce = 1 / (top_level_trans_time * 2 + mill_time + train_time)
            # print(s_ce)
            ce += s_ce
        else:
            bottom_level_amount = s - 1
            bottom_level_trans_time = bottom_level_amount * \
                trans_time_rate  # * time_bias(1, bottom_level_amount)
            s_ce = 1 / ((top_level_trans_time) * 2 + mill_time) 
            # print(s_ce)
            ce += s_ce

    return ce * random.uniform(1.009, 1.011)

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

def caculate_ce_flat(device: int, inbound_bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / inbound_bandwidth
    # trans_time = device * trans_time_rate
    trans_time = trans_time_rate
    print(device, trans_time)

    ce = float(0)
    ce += device / (trans_time * 2 + mill_time + train_time)
    # print(device, ce)
    return ce

"""
In V4 ver CE caculator
It's a updated version that discard the share-role impact, 
"""
def caculate_ce_v4(group: list, bandwidth_lut: list, parameter_size: float, mill_time: float, train_time: float) -> float:
    top_level_trans_time = parameter_size / bandwidth_lut[len(group)]
    print(group, top_level_trans_time)

    ce = float(0)
    for s in group:
        bottom_level_amount = s
        bottom_level_trans_time = parameter_size / bandwidth_lut[bottom_level_amount]
        print(group, bottom_level_trans_time)
        s_ce = s / ((top_level_trans_time + bottom_level_trans_time)
                    * 2 + mill_time * 2 + train_time)
        # print(s_ce)
        ce += s_ce
    # print(group, ce)
    return ce

"""
Calculate CE Ver.5
No role-sharing, top level not split the bandwidth
"""
def caculate_ce_v5(group: list, inbound_bandwidth: float, outbound_bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / inbound_bandwidth + parameter_size / outbound_bandwidth
    top_level_amount = len(group)
    top_level_trans_time = trans_time_rate * top_level_amount

    ce = float(0)
    for s in group:
        bottom_level_amount = s
        bottom_level_trans_time = bottom_level_amount * \
            trans_time_rate
        s_ce = s / ((top_level_trans_time + bottom_level_trans_time) + mill_time * 2 + train_time)
        print('Trans_time of {0} is {1}'.format(s, bottom_level_trans_time))
        ce += s_ce
    return ce

"""
Calculate CE for 1-level Ver.2 (used to sync with Cal_CE__V5)
"""
def caculate_ce_flat_v2(device: int, inbound_bandwidth: float, outbound_bandwidth: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time_rate = parameter_size / inbound_bandwidth + parameter_size / outbound_bandwidth
    trans_time = trans_time_rate * device 

    ce = float(0)
    ce += device / (trans_time + mill_time + train_time)
    # print('Trans_time of {0} is {1}'.format(device, trans_time))
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

def round_and_avg(value, dividor):
    value = round(value * dividor)
    return value / dividor

LENET_PARAMETER_SIZE = 7.08
LENET_TRAINING_TIME = 0.7
LENET_BATCH_IN_EPOCH = 47

PERNET_PARAMETER_SIZE = 2.85
PERNET_TRAINING_TIME = 1.15
PERNET_BATCH_IN_EPOCH = 52

Alpha_Weighted_Bandwidth_lenet = [
    25,
    25,
    21.16487455,
    17.55488531,
    14.2337476,
    11.11351583,
    9.09093079,
    7.192546528,
    5.989256915,
    5.127049771,
    4.405043986
]

Alpha_Weighted_Bandwidth_pernet = [
    25,
    25,
    16.68963097,
    11.14586405,
    8.141802671,
    6.285381007,
    5.0875866,
    4.315050694,
    4.110335937,
    3.29485091,
    2.950646206
]

Alpha_Weighted_Bandwidth_pernet_dummy = [
    25,
    25,
    12.5,
    8.33333333333333,
    6.25,
    5,
    4.16666666666667,
    3.57142857142857,
    3.125,
    2.77777777777778,
    2.5,
]

Alpha_Weighted_Bandwidth_pernet_100 = [
    100,
    100,
    89.53158662,
    49.90030171,
    43.27542412,
    34.11166157,
    31.86385669,
    26.55743016,
    25.97030905,
    21.77526785,
    19.7435841
]


if __name__ == "__main__":
    ce_table = []
    for w in range(1, 10):
        """
        For each number of workers, first put 1-level topology's CE into ce_table.
        """
        # ce_table.append((caculate_ce_flat(w, Alpha_Weighted_Bandwidth_pernet_dummy[w] * 0.218, PERNET_PARAMETER_SIZE * 8, 0.08, PERNET_TRAINING_TIME), w))
        ce_table.append((caculate_ce_flat_v2(w, 25, 25, PERNET_PARAMETER_SIZE * 8, 0.08, PERNET_TRAINING_TIME), w))

        """
        Generate all topologies to be calculated CE value, put them all into gs (list).
        * Method 1: all_groups_v2(w: worker amount) -> Generate all possible topologies (v2 is a fast implementation)
        * Method 2: most_balanced_group(w: worker amount) -> Generate only most balanced 2-split topology, such as 9 workers will be placed as [5, 4]. 
        """
        start = timeit.default_timer()
        # gs = all_groups_v2(w)
        gs = most_balanced_group(w, 3)
        #  gs = [[8], [4, 4], [3, 3, 2], [2, 2, 2, 2],[2,2,2,1,1],[2,2,1,1,1,1],[2,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
        end = timeit.default_timer()
        # print("Generate time: {0}".format(end - start))
        # print(len(gs))

        """
        For each topology in gs, compute its CE value.
        """
        start = timeit.default_timer()
        for g in gs:
            # pass
            ce_table.append((caculate_ce_v5(g, 25, 25, PERNET_PARAMETER_SIZE * 8, 0.08, PERNET_TRAINING_TIME), g))
            # ce_table.append((caculate_ce_v4(g, [x * 0.218 for x in Alpha_Weighted_Bandwidth_pernet_dummy], PERNET_PARAMETER_SIZE, 0.08, PERNET_TRAINING_TIME), g))
        end = timeit.default_timer()
        # print("Calculate time: {0}".format(end - start))
        start = timeit.default_timer()

    #  ce_table.sort(reverse=True)
    ce_table.sort()
    end = timeit.default_timer()
    print("Sort time: {0}".format(end - start))

    len_list = []
    print_list = []
    for v, k in ce_table:
        #  if (sum(k) != len(k)):
            #  continue
        #  if (len(k) in len_list):
            #  continue
        #  if (len(k) > 8):
            #  continue
        #  else:
        #  if (sum(k), len(k)) in print_list:
        #      continue
        if (type(k) == list):
            print(sum(k), len(k), k, round(PERNET_BATCH_IN_EPOCH * 5 / v, 5))            
            # print(sum(k), len(k), k, round(v, 5))
        else:
            print(k, k, k, round(PERNET_BATCH_IN_EPOCH * 5 / v, 5))
            # print(k, k, k, round(v, 5))
        #  len_list.append(len(k))
        #  print_list.append((sum(k), len(k)))
