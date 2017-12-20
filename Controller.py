import sys

import Command
import To_csv


class Controller:
    def __init__(self, ip='0.0.0.0', port=5000,  type='TCP', parallel=2, time=4):
        self.type = type
        self.parallel = parallel
        self.ip = ip
        self.port = port
        self.time = time


    def run(self):
        print("ip:", self.ip, "Port:", self.port, "type:", self.type, "Parallel:", self.parallel, "time:", self.time)
