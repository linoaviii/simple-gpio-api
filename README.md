
# RaspberryPi simple GPIO API

Simple Web api used to read and write RaspberryPi GPIO states.
Change your gpio states by URL (usefull for domotic project)
No programming knowledge needed

This API is composed byt a GPIO web test :
```
http://{IP_RASPBERRY}
```
![web api preview](simple-gpio-api/images/test-web.jpg)

And an acces to GPIO by a simple URL:

 - Read GPIO (input or output)
```
http://{IP_RASPBERRY}/gpio/{gpio_number}
will return 0 if GPIO is Down, 1 if GPIO is up (-1 if error)
```
example, read GPIO 12 state (GPIO number is set in BCM mode)
```
http://192.168.0.1/gpio/12
```
- Write GPIO (output)
```
http://{IP_RASPBERRY}/gpio/{gpio_number}/{gpio_state}
will set the gpio with the state and return 0 if GPIO is Down, 1 if GPIO is up (-1 if error)
```
example, set GPIO 12 up (GPIO number is set in BCM mode)
```
http://192.168.0.1/gpio/12/1
```
example, set GPIO 13 down (GPIO number is set in BCM mode)
```
http://192.168.0.1/gpio/13/0
```

## Getting Started

These instructions will get you a copy of the project up and running on your RaspberryPi.

### Prerequisites

To facilitate installation, everything is include in the project.
You just need a raspberry Pi (every versions working) with Raspbian OS installed
To install Raspbian, see : https://www.raspberrypi.org/downloads/


#### a) Automatic copy (using git)

 - Open a terminal :
 ```
 Ctrl + Alt + T
 ```
 - Clone simple-gpio-api project in home folder (/home/pi):
```
git clone https://github.com/linoaviii/simple-gpio-api /home/pi/simple-gpio-api
```

#### b) manual copy 
If git is not installed or if you don't  want to use it, you can copy simple-gpio-api folder  manually into your home folder (/home/pi)


### Installing
 - Open a terminal :
 ```
 Ctrl + Alt + T
 ```
 - Run setup script
```
sudo sh simple-gpio-api/setup.sh
```
and it's done

## Running

 - Open a terminal :
 ```
 Ctrl + Alt + T
 ```
 - Run start script
```
sh simple-gpio-api/start.sh
```
![webservice started preview](simple-gpio-api/images/webservice-started.jpg)

Don't close the terminal to keep API alive.

By default, every GPIO are set to OUTPUT, if you want to set some GPIO as Input, edit the **config.INI** file in **simple-gpio-api** folder 
list all GPIO number (in BCM mode) you want as Input in **gpio_input** line, separated by space
example:
 ```
gpio_input = 2 3 4 17 
 ```
Restart the script to change GPIO functions

## Using
You can use this API directly by your browser.
Available commands :

 - **Read GPIO** : http://**{IP_RASPBERRY}**/gpio/**{gpio_number}**
 - **Write GPIO** : http://**{IP_RASPBERRY}**/gpio/**{gpio_number}**/**{gpio_state}**
 - **GPIO Test**: http://**{IP_RASPBERRY}**
 - **API documentation**: http://**{IP_RASPBERRY}**/doc

## Launch at startup
If you want to launch automatically the script at RaspberryPi startup
 - Open a terminal :
 ```
 Ctrl + Alt + T
 ```
 - launch theses commands :
 ```
 sudo cp /home/pi/simple-gpio-api/simple-gpio-api.service /etc/systemd/system
 sudo systemctl enable simple-gpio-api.service 
 ```
 - reboot your raspberryPi (the API will run without terminal. You can test it directly with you browser)

## Built With
* [Python](https://www.python.org/) - Python 3
* [Swagger](https://swagger.io/) - Web Api editor (openApi)


## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **David Audran** - *Initial work* - [Website](http://davidaudran.com)



