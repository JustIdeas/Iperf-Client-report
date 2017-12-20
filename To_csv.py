import csv
import sys



class Input:

    def __init__(self, values=10, bandwidth='Mbits'):
        self.values = values
        self.bandwidth = bandwidth

    def run(self):
        try:
            with open('names.csv', 'w', newline='') as csvfile:
                fieldnames = ['Speed', 'Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                i=0
                print("has:", self.values[2])
                while i < len(self.values):

                    writer.writerow({'Speed': self.bandwidth, 'Value': self.values[i]})
                    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
                    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
                    i = i + 1
        except:
            print('error', sys.exc_info()[0], sys.exc_info()[1])

# Input(['1','2','3']).run()