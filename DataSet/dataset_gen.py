import csv
import random


def usual_traffic():
    traffic = []
    weights = [0.7, 0.3]  # the weights for the IP source/destination
    weights_flags = [0.3, 0.3, 0.1, 0.3]
    traffic.append(random.randint(12, 25))  # the time
    traffic.append((random.randint(4500, 6500)))  # the required space

    #the method choices returns a list
    traffic.append(random.choices([0, 1], weights)[0])  # the  IP destination
    traffic.append(random.choices([0, 1], weights)[0])  # the  IP source
    for index in range(0, 8):  # the flags
        traffic.append(random.choices([250, 500, 750, 0], weights_flags)[0])  # only Syn/ ACK packets

    for index in range(0, 8):  # the TCP method
        traffic.append(random.choice([250, 500, 750, 0]))

    traffic.append(0)  # the class for the normal trafic

    return traffic


def gen_buffer_attack():
    traffic = []
    traffic.append(random.randint(3, 15))  # the time
    traffic.append((random.randint(4500, 9000)))  # the required space
    traffic.append(1)  # the  IP destination
    traffic.append(random.choice([0, 1]))  # the  IP source
    for index in range(0, 8):  # the flags
        traffic.append(random.choice([250, 500]))  # only Syn/ ACK packets

    for index in range(0, 8):  # the TCP method
        traffic.append(random.choice([500, 750]))

    traffic.append(3)  # the class for the DoS attack
    return traffic


# for the smurf attack ( same IP source but very fast low space ECHO requests
def gen_smurf_attack():
    traffic = []
    traffic.append(random.randint(1, 10))  # the time
    traffic.append((random.randint(1500, 3500)))  # the required space
    traffic.append(random.choice([0, 1]))  # the same IP destination
    traffic.append(1)  # the same IP source
    for index in range(0, 8):  # the flags
        traffic.append(750)  # only Syn packets

    for index in range(0, 8):  # the TCP method
        traffic.append(0)

    traffic.append(2)  # the class for the DoS attack
    return traffic


# function to generate Dos attack
def gen_dos_attack():
    traffic = []
    traffic.append(random.randint(1, 8))  # the time
    traffic.append((random.randint(1500, 4500)))  # the required space
    traffic.append(1)  # the same IP destination
    traffic.append(random.choice([0, 1]))  # the same IP source
    for index in range(0, 8):  # the flags
        traffic.append(500)  # only Syn packets

    for index in range(0, 8):  # the TCP method
        traffic.append(0)

    traffic.append(1)  # the class for the DoS attack
    return traffic


with open('tcp_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # the header
    writer.writerow(["time_mean", "dimension_mean", "IP_destination", "IP_source", "flags1", "flags2", "flags3",
                     "flags4", "flags5", "flags6", "flags7", "flags8", "method1", "method2", "method3", "method4",
                     "method5", "method6", "method7", "method8", "class"])

    # ACK = 250
    # SYN = 500
    # ECHO_REQ = 750
    # RESET = 0

    # GET = 250
    # POST = 500
    # PUT = 750
    # DELETE = 0

    for index in range(0, 1000):
        trafic = gen_dos_attack()
        writer.writerow(trafic)

    for index in range(0, 1000):
        trafic = gen_smurf_attack()
        writer.writerow(trafic)

    for index in range(0, 1000):
        trafic = gen_buffer_attack()
        writer.writerow(trafic)

    for index in range(0, 2000):
        trafic = usual_traffic()
        writer.writerow(trafic)
    # writer.writerow(lst)