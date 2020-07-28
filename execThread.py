from subprocess import Popen
import threading

class execThread(threading.Thread):
    def __init__(self, cmd, outfile=None):
        threading.Thread.__init__(self)
        self.cmd = cmd
        if outfile != None:
            self.outfile = open(outfile, 'w')
        else:
            self.outfile = None

    def run(self):
        # execute the command, queue the result
        if self.outfile != None:
            p = Popen(self.cmd, shell=True, universal_newlines=True, stdout=self.outfile, stderr=self.outfile)
        else:
            p = Popen(self.cmd, shell=True, universal_newlines=True)
        
        ret_code = p.wait()
        if self.outfile != None:
            self.outfile.flush()
            self.outfile.close()
        return ret_code


if __name__ == "__main__":
    nt = execThread("echo aaaa","test")
    nt.run()