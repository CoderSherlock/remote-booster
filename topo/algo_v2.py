"""
This script is used for calculate CE for All-Synced topologies.
Author: CoderSherlock
"""

import unittest

def CEcalculator_SS(group: list, nic_speed: float, parameter_size: float, mill_time: float, train_time: float) -> float: 
    # Because of all leaders are sync PU, one step will be finished only the slowest worker finished its batch.
    # As for the upper level outsync issue, we just naively treat it as equally splitted top-leader's bandwidth.
    # nic_speed             => Mbps (Bits)
    # parameter_size        => Mb (Bits)
    # mill_time/train_time  => Second 

    upper_level_trans_time = parameter_size * len(group) / nic_speed

    max_lower_level_trans_time = float(0.0)
    for s in group:
        lower_level_amount = s
        lower_level_trans_time = lower_level_amount * parameter_size / nic_speed 
        max_lower_level_trans_time = max(max_lower_level_trans_time, lower_level_trans_time)
    ce = float(sum(group)) / (max_lower_level_trans_time + upper_level_trans_time + 2 * mill_time + train_time)
    return ce

def CEcalculator_S(device: int, nic_speed: float, parameter_size: float, mill_time: float, train_time: float) -> float:
    trans_time = parameter_size * device / nic_speed
    ce = float(device) / (trans_time + mill_time + train_time)
    return ce


LENET_PARAMETER_SIZE = 7.164
LENET_TRAINING_TIME = 0.7
LENET_BATCH_IN_EPOCH = 47
"""
LeNet:
Up
452117 Bytes
452051 Bytes
Down
443645 Bytes
443075 Bytes

Average => 447722 Bytes / 3.581776 Mbits
"""

INCEPTION_PARAMETER_SIZE = 1.778
INCEPTION_TRAINING_TIME = 5.64
INCEPTION_MILLS_TIME = 0.15
INCEPTION_BATCH_IN_EPOCH = 47
"""
Inception_LeNet:
Up
112029 Bytes
112029 Bytes
Down
110115 Bytes
110247 Bytes

Average => 111105 Bytes / 0.88884 Mbits
"""

class TestFunctions(unittest.TestCase):
    def test_CEcalculator_SS(self):
        print("test_CEcalculator_SS")
        # print(1.0/CEcalculator_SS([2,1], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

        # print(1.0/CEcalculator_SS([3,1], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

        # print(1.0/CEcalculator_SS([4,1], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([3,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

        # print(1.0/CEcalculator_SS([5,1], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([4,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([3,3], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([2,2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

        # print(1.0/CEcalculator_SS([6,1], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([5,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([4,3], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([3,2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

        # print(1.0/CEcalculator_SS([7,1], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([6,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([5,3], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([4,4], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([3,3,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([4,2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        print(1.0/CEcalculator_SS([2,2,2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
    
        # print(1.0/CEcalculator_SS([7,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([6,3], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([5,4], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([5,2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([4,3,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_SS([3,3,3], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        print(1.0/CEcalculator_SS([3,2,2,2], 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

    def test_CEcalculator_S(self):
        print("test_CEcalculator_S")
        # print(1.0/CEcalculator_S(1, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(2, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(3, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(4, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(5, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(6, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(7, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        # print(1.0/CEcalculator_S(8, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))
        print(1.0/CEcalculator_S(9, 10, LENET_PARAMETER_SIZE, 0.08, LENET_TRAINING_TIME))

if __name__ == "__main__":
    unittest.main()