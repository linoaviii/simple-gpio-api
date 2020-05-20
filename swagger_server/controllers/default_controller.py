from gpio.gpio import Gpio
from flask import render_template
import os

#GPIO management object
gpio = Gpio()

def doc_get():  # noqa: E501
    """API documentation

    show the Api documentation details in html # noqa: E501


    :rtype: str
    """
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../templates/doc.html', 'r') as content_file:
        content = content_file.read()
        return content


def gpio_gpio_number_get(gpio_number):  # noqa: E501
    """Read a GPIO state

    Read the GPIO {gpio_number} state in BCM mode # noqa: E501

    :param gpio_number: GPIO number in BCM mode
    :type gpio_number: int

    :rtype: int
    """
    return gpio.read(gpio_number)


def gpio_gpio_number_gpio_state_get(gpio_number, gpio_state):  # noqa: E501
    """Write a GPIO state

    Write the GPIO {gpio_number} state in BCM mode # noqa: E501

    :param gpio_number: GPIO number in BCM mode
    :type gpio_number: int
    :param gpio_state: New GPIO state in BCM mode
    :type gpio_state: int

    :rtype: int
    """

    return gpio.write(gpio_number, gpio_state)


def root_get():  # noqa: E501
    """Test interface

    Web page showing all GPIO states and allow user to change GPIO values # noqa: E501


    :rtype: str
    """
    gpio_states = gpio.read_all()
    gpio_functions = gpio.function_all()
    
    return render_template('index.html', gpio_states=gpio_states, gpio_functions=gpio_functions)


def root_gpio_number_gpio_state_get(gpio_number, gpio_state):  # noqa: E501
    """Test interface

    Web page showing all GPIO states after GPIO change value # noqa: E501


    :rtype: str
    """
    gpio_gpio_number_gpio_state_get(gpio_number, gpio_state)
    
    return root_get()

