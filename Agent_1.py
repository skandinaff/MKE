import time
import random
from osbrain import run_agent
from osbrain import run_nameserver



def log_message(agent, message):
    agent.log_info('Received: %s' % message)

def count_message(agent, message):

    if(message != 0):
        print("we got msg!")




def deploy_data(agent):

    message = str(random.randint(1,11)) + " from: " + str(agent.name)
    agent.send('Data1', message)

def deploy_data2(agent):
    message = str(random.randint(101,121)) + " from: " + str(agent.name)
    agent.send('Data2', message)


if __name__ == '__main__':

    ns = run_nameserver()
    sensor1 = run_agent('Sensor1')
    sensor2 = run_agent('Sensor2')
    receiver = run_agent('Receiver')

    addr1 = sensor1.bind('PUSH', alias='Data1')
    addr2 = sensor2.bind('PUSH', alias='Data2')
    receiver.connect(addr1, handler=[log_message, count_message])
    receiver.connect(addr2, handler=log_message)

    # Multiple timers with parameters
    sensor1.each(1.0, deploy_data)
    sensor2.each(0.4142, deploy_data2)




    time.sleep(10)


    ns.shutdown()