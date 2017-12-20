import Command
import To_csv
import argparse
import sys

import Controller


# ip = argparse
# result = Command.shell("iperf -c 127.0.0.1 -i1 -p 6000 -t3 -P2 | grep \"SUM\" | awk {\' print $7 \'}").run()
#
# result = result.split("\n")
#
# print("resultado=", result)
# To_csv.Input(result).run()

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Basic Functions')
    parser.add_argument('-H', '--host',
                        help='host ip',
                        required='True',
                        default='localhost')
    parser.add_argument('-dp', '--port',
                        help='destination port',
                        default='5000')
    parser.add_argument('-p', '--protocol',
                        help='Protocolo TCP/UDP',
                        default='')
    parser.add_argument('-P', '--parallel',
                        help='Process in Parallel',
                        default='')
    parser.add_argument('-t', '--time',
                        help='time of test /s',
                        default='')

    results = parser.parse_args(args)
    return (results.host,
            results.port,
            results.protocol,
            results.parallel,
            results.time)

if __name__ == '__main__':
    h, dp, p, P, t= check_arg(sys.argv[1:])
    Controller.Controller(h, dp, p, P, t).run()
