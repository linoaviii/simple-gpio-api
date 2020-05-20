# coding: utf-8
import RPi.GPIO as GPIO
import os
import configparser

# Raspberry pi GPIO management
class Gpio(object):
    
    def __init__(self):
        """Init GPIO management
        """
        # Init GPIO configuration
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        
        # Load configuration file
        self.config_file = os.path.dirname(os.path.abspath(__file__)) + "/../config.INI"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        
        self.nb_gpio = int(self.config['GENERAL']['nb_gpio'])
        gpio_input = self.config['GENERAL']['gpio_input'].split()

        # Set all GPIO (INPUT or OUTPUT), see ../config.INI file to change mode
        for i in range(1,self.nb_gpio+1):
           
            if str(i) in gpio_input:
                print("input : " + str(i))
                GPIO.setup(i, GPIO.IN)
            else:
                GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)


    def read(self, gpio_number):
        """Read a GPIO state

        Read the GPIO {gpio_number} state in BCM mode (0 if down, 1 if up, -1 if unknown)

        :param gpio_number: GPIO number in BCM mode
        :type gpio_number: int

        :rtype: int
        """
        GPIO.setmode(GPIO.BCM)
        
        gpio_function = GPIO.gpio_function(gpio_number)
        gpio_state = -1

        #read only If the gpio is set as input or output
        if gpio_function == GPIO.IN or gpio_function == GPIO.OUT:
            gpio_state = GPIO.input(gpio_number)
            
        return gpio_state
    
    
    def read_all(self):
        """Read all GPIO state

        Read all GPIO state in BCM mode (0 if down, 1 if up, -1 if unknown)
        And return a list  with all state

        :rtype: dictionnary
        """
        gpio_states = {}
        
        # Read all GPIO
        for i in range(1,self.nb_gpio+1):
            gpio_states[i] = self.read(i)
        
        return gpio_states
    
    
    def function_all(self):
        """Read all GPIO state

        Read all GPIO function in BCM mode (INPUT or OUTPUT)
        And return a list  with all function

        :rtype: dictionnary
        """
        gpio_functions = {}
        
        # Read all GPIO functions
        for i in range(1,self.nb_gpio+1):
            gpio_functions[i] = GPIO.gpio_function(i)
        
        return gpio_functions
    
    
    def write(self, gpio_number, gpio_state):
        """Write a GPIO state

        Write the GPIO {gpio_number} state in BCM mode # noqa: E501

        :param gpio_number: GPIO number in BCM mode
        :type gpio_number: int
        :param gpio_state: New GPIO state in BCM mode (0 if down, 1 if up, -1 if unknown)
        :type gpio_state: int

        :rtype: int
        """
        
        # New GPIO state 
        new_state = -1
        
        #If the gpio is an output
        if GPIO.gpio_function(gpio_number) == GPIO.OUT:
            GPIO.output(gpio_number, gpio_state)
            new_state = self.read(gpio_number)
    
        return new_state
        