
train_dir = "/home/dlib/data/per/Local_training.csv"
test_dir = "/home/dlib/data/per/Local_testing.csv"

config_dest = "/home/dlib/dlib-exper/build/ip-list"

global_ps_ip = "192.168.0.117"

ip_list = ["192.168.0.101",
           "192.168.0.102",
           "192.168.0.103",
           "192.168.0.104",
           "192.168.0.105",
           "192.168.0.106",
           "192.168.0.107",
           "192.168.0.108",
           "192.168.0.109",
           "192.168.0.110",
           "192.168.0.111",
           "192.168.0.112",
           "192.168.0.113",
           "192.168.0.114",
           "192.168.0.115",
           "192.168.0.116",
           ]


def generate_str(group: list, ip_list: list):
    # TODO for 1 device cluster
    config_str = "1 1 " + str(sum(group) + len(group) + 1) + "\n"
    config_str += train_dir + "\n"
    config_str += test_dir + "\n"

    r_index = 0
    d_index = 0

    config_str += "{0} {1} {2} {3} {4}\n".format(
        r_index, global_ps_ip, 15001+r_index, 2, -1)
    grandpa = r_index
    r_index += 1

    for i in range(0, len(group)):
        father = -1
        if (group[i] > 1):
            config_str += "{0} {1} {2} {3} {4}\n".format(
                r_index, ip_list[d_index], 14001+r_index, 1, grandpa)
            father = r_index
            r_index += 1
        for j in range(0, group[i]):
            config_str += "{0} {1} {2} {3} {4}\n".format(
                r_index, ip_list[d_index], 13001+r_index, 0, father if father != -1 else grandpa)
            r_index += 1
            d_index += 1

    return config_str


# localhost_train_path = "/home/pengzhan/Github/dlib-exper/build/Local_training.csv"
# localhost_test_path = "/home/pengzhan/Github/dlib-exper/build/Local_testing.csv"
localhost_train_path = "/home/pengzhan/Github/data/mnist"
localhost_test_path = "/home/pengzhan/Github/data/mnist"

def generate_local_config(group: list):
    config_dict = {}
    amount_of_instances = 1
    for i in range(0, len(group)):
        if (group[i] > 1):
            amount_of_instances += (1 + group[i])
        else:
            amount_of_instances += 1

    config_dict["train"] = [localhost_train_path]
    config_dict["test"] = [localhost_test_path]

    r_index = 0
    l_index = 0
    w_index = 0

    config_dict["device"] = [
        {"index": r_index, "ip": "127.0.0.1", "port": "15001", "role": "2", "parent": "-1"}]

    grandpa = r_index
    r_index += 1

    for i in range(0, len(group)):
        father = -1
        if (group[i] > 1):
            config_dict["device"].append({"index": r_index, "ip": "127.0.0.1", "port": str(
                14001+l_index), "role": str(1), "parent": str(grandpa)})
            father = r_index
            r_index += 1
            l_index += 1
        for j in range(0, group[i]):
            config_dict["device"].append({"index": r_index, "ip": "127.0.0.1", "port": str(
                13001+w_index), "role": str(0), "parent": str(father if father != -1 else grandpa)})
            r_index += 1
            w_index += 1

    return config_dict


def config_to_str(config: dict, ending: int):
    config_str = str(len(config["train"])) + " " + \
        str(len(config["test"])) + " " + str(len(config["device"])) + " " + str(ending) + "\n"
    for tr in config["train"]:
        config_str += tr + "\n"
    for te in config["test"]:
        config_str += te + "\n"

    for de in config["device"]:
        config_str += "{0} {1} {2} {3} {4}\n".format(
            de["index"], de["ip"], de["port"], de["role"], de["parent"])

    return config_str


def generate_file(group: list, ip_list: list, output_file: str, ending: int) -> int:
    config = generate_local_config(group)
    content = config_to_str(config, ending)

    f = open(output_file, "w")
    f.write(content)
    f.close()

    return config


if __name__ == "__main__":
    generate_file([1, 2, 1, 2], ip_list, "ip-list")
