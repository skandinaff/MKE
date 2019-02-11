import time
import random
from osbrain import run_agent
from osbrain import run_nameserver
from osbrain import run_logger



class MessageCounter:
    def __init__(self, sensor_number, message_count):
        self.sensor_number = sensor_number
        self.message_count = message_count
    def my_custom_handler(self,agent,message):
        print(agent)
        agent.log_info('Received: %s' % message)
        if message != 0:
            msc_sensor1.message_count += 1
            print(msc_sensor1.message_count)




def log_message(agent, message):
    receiver.message_counter(agent,message)

    #print (agent)
    #agent.log_info('Received: %s' % message)
    if message != 0:
        msc_sensor1.message_count += 1
        #print(msc_sensor1.message_count)

def message_counter(self): # agent, message):
    print("Message counter")
    #print (agent)
    #agent.log_info('Received: %s' % message)
    #if message != 0:
    #    msc_sensor1.message_count += 1
    #    #print(msc_sensor1.message_count)


def deploy_data(agent):

    message = str(random.randint(1,11)) + " from: " + str(agent.name)
    agent.send('Data1', message)

def deploy_data2(agent):
    message = str(random.randint(101,121)) + " from: " + str(agent.name)
    agent.send('Data2', message)


if __name__ == '__main__':

    ns = run_nameserver()
    sensor1 = run_agent('Sensor1') # creating proxies to the agents
    sensor2 = run_agent('Sensor2')
    receiver = run_agent('Receiver')

    logger1 = run_logger("Logger1")

    print(ns.agents())

    msc_sensor1 = MessageCounter(sensor1,0)

    addr1 = sensor1.bind('PUSH', alias='Data1')
    addr2 = sensor2.bind('PUSH', alias='Data2')

    receiver.connect(addr1, handler=log_message)
    receiver.connect(addr2, handler=log_message)

    sensor1.set_logger(logger1)

    receiver.set_method(message_counter)



    # Multiple timers with parameters
    sensor1.each(1.0, deploy_data)
    sensor2.each(0.4142, deploy_data2)

    time.sleep(4)

    print("And here we have calculated message count: ")
    # print_number_of_messages()
    print(msc_sensor1.message_count)
    print(receiver.message_counter())

    ns.shutdown()




