from generate_config import generate_file
from execThread import execThread
import time


class topology_task:
    def __init__(self, taskname, topology, ending):
        self.taskname = taskname
        self.topology = topology
        self._tp = []
        self.ending = ending

    def prepare_task(self):
        config = generate_file(self.topology, None, "ip-list", self.ending)
        for i in config["device"]:
            if i["role"] == "2":
                tmpT = execThread(
                    "/home/pengzhan/Github/dlib-exper/build/lenet_3level_worker {0} {1} {2} -c ip-list".format(
                        i["ip"], i["port"], i["index"]), self.taskname)
                self._tp.append(tmpT)
            else:
                tmpT=execThread(
                    "/home/pengzhan/Github/dlib-exper/build/lenet_3level_worker {0} {1} {2} -c ip-list".format(i["ip"], i["port"], i["index"]))
                self._tp.append(tmpT)

    def run(self):
        for t in self._tp:
            t.start()

    def wait(self):
        for t in self._tp:
            t.join()

class multiple_tasks:
    def __init__(self, taskname, topology, count, ending):
        self.taskname = taskname
        self.topology = topology
        self.count = count
        self.ending = ending

    def run_tasks(self):
        for i in range(0, self.count):
            one_task = topology_task(self.taskname + "-" + str(i), self.topology, self.ending)
            one_task.prepare_task()
            one_task.run()
            one_task.wait()
            time.sleep(10)


if __name__ == "__main__":
    # tasks = multiple_tasks("test1-1", [1], 10, 8)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test2-1", [2], 10, 18)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test3-1", [3], 10, 22)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test4-1", [4], 10, 25)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test5-1", [5], 10, 28)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test6-1", [6], 10, 33)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test7-1", [7], 10, 38)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-1", [8], 10, 43)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test2-2", [1, 1], 10, 18)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test3-2", [2, 1], 10, 22)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test4-2", [2, 2], 10, 25)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test5-2", [3, 2], 10, 28)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test6-2", [3, 3], 10, 33)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test7-2", [4, 3], 10, 38)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-2", [4, 4], 10, 43)
    # tasks.run_tasks()
    
    # tasks = multiple_tasks("test3-3", [1, 1, 1], 10, 22)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test4-3", [2, 1, 1], 10, 25)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test5-3", [2, 2, 1], 10, 28)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test6-3", [2, 2, 2], 10, 33)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test7-3", [3, 2, 2], 10, 38)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-3", [3, 3, 2], 10, 43)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test4-4", [1, 1, 1, 1], 10, 25)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test5-4", [2, 1, 1, 1], 10, 28)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test6-4", [2, 2, 1, 1], 10, 33)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test7-4", [2, 2, 2, 1], 10, 38)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-4", [2, 2, 2, 2], 10, 43)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test5-5", [1, 1, 1, 1, 1], 10, 34)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test6-5", [2, 1, 1, 1, 1], 10, 39)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test7-5", [2, 2, 1, 1, 1], 10, 43)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-5", [2, 2, 2, 1, 1], 10, 51)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test6-6", [1, 1, 1, 1, 1, 1], 10, 40)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test7-6", [2, 1, 1, 1, 1, 1], 10, 44)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-6", [2, 2, 1, 1, 1, 1], 10, 52)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test7-7", [1, 1, 1, 1, 1, 1, 1], 10, 44)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test8-7", [2, 1, 1, 1, 1, 1, 1], 10, 49)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test8-8", [1, 1, 1, 1, 1, 1, 1, 1], 1, 54)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test9-1", [9], 10, 8)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test9-2", [5, 4], 10, 18)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test9-3", [3, 3, 3], 10, 22)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test9-4", [3, 2, 2, 2], 10, 25)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test9-5", [2, 2, 2, 2, 1], 10, 28)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test9-6", [2, 2, 2, 1, 1, 1], 10, 33)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test9-7", [2, 2, 1, 1, 1, 1, 1], 10, 38)
    # tasks.run_tasks()    
    # tasks = multiple_tasks("test9-8", [2, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test9-9", [1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    # tasks.run_tasks()

    # tasks = multiple_tasks("test10-9", [2, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    # tasks.run_tasks()
    # tasks = multiple_tasks("test10-10", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    # tasks.run_tasks()


    tasks = multiple_tasks("test11-9", [2, 2, 2, 1, 1, 1, 1, 1], 10, 43)
    tasks.run_tasks()
    tasks = multiple_tasks("test11-9", [2, 2, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    tasks.run_tasks()
    tasks = multiple_tasks("test11-10", [2, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    tasks.run_tasks()
    # tasks = multiple_tasks("test11-11", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    # tasks.run_tasks()

    tasks = multiple_tasks("test12-9", [2, 2, 2, 1, 1, 1, 1, 1, 1], 10, 43)
    tasks.run_tasks()
    tasks = multiple_tasks("test12-10", [2, 2, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    tasks.run_tasks()
    tasks = multiple_tasks("test12-11", [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    tasks.run_tasks()
    # tasks = multiple_tasks("test12-12", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 43)
    # tasks.run_tasks()