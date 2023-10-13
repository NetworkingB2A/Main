
## Logging
logging module built into python. No need to install anything special.

Link to the python documentation.
https://docs.python.org/3/library/logging.html


### Why use logging vs print?
Logging will allow you to capture additional data about the running of your code. It will give you flexibility as to how you capture your logs. Print only allow very basic capturing of your logging.



### logging levels
| Level | Numeric value | Description
|-|-|-|
|CRITICAL| 50| A serious error, indicating that the program itself may be unable to continue running.|
|ERROR| 40| Due to a more serious problem, the software has not been able to perform some function.|
|WARNING| 30| An indication that something unexpected happened, or indicative of some problem in the near future. |The software is still working as expected. This is the default level for the logging module.
|INFO |20| Confirmation that things are working as expected|
|DEBUG| 10| Detailed information, typically of interest only when diagnosing problems. When this is used it works a lot like the print statement and displays basic data to the screen. |
|NONSET| 0||


### How to set up logging
Here is a very VERY basic logging script. 

The following is showing that you want to see warning levels and higher. When main is run you would only see critical, error and warning levels.

When using this basic config in your script like this, you will be using that is called the root logger. Below is a section that will explain a root logger vs import logger and why this is important. 

```python
import logging

def main() -> None:
    logging.basicConfig(level=logging.WARNING)

    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")
```

Example of the output
```python

>>> main()
WARNING:root:This is a warning message
ERROR:root:This is a error message
CRITICAL:root:This is a critical message
```

Here is an example of the same code but I have added some formatting.
Format keyword is used to show what is displayed to the screen or the output file. The datefmt keyword is used to configure the (asctime) and show what time you want to show up. By default, the logging is written to the console. if you would like to to write the logging to a file you only need to add a filename keyword and the name of the log you are creating. NOTE when adding filename logging keyword to the config all of the output is sent to the logging file. logging will add to the existing log file, logging does not overwrite it by default. 

```python
import logging

def main() -> None:
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logging_training.log",
        )

    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")
```
Here is the output of the formatted output. 

```python
2023-09-19 15:05:14 WARNING This is a warning message
2023-09-19 15:05:14 ERROR This is a error message
2023-09-19 15:05:14 CRITICAL This is a critical message
```


### Root logger vs imported logger
TODO:
I need to learn this.


### More advanced logging
if you only need the most basic level of logging and you only really plan on using these logs for yourself using the basicConfig logger makes the most sense. If you would like to share this logger, or user different logging customizations for different parts of your code, or many other reasons. The better solution is to use a logger.

#### Breaking down more advanced logging
You have a logger. This is the configuration of how your logging will work.

You have handlers.
- Handlers are what you do with your logs.
- Handler types
  - Stream handler - puts logs out to screen. 
  - File handler - puts logs out to a specific file.



If you default to the root logging and you decide to import a different module that also has a root logger, the root logger of the imported class will actually do the logging and the logger you have in your main code down below will not be called, because you already have a root logger called.
Example of best practice code

using the `__name__` will pass the name of the module you are running into the logger, this will replace the word root in the logger.
```python
import logging
logger = logging.getLogger(__name__)

#You would use this next part if you want to customize your logger a bit more. This will allow you to change the root logger info.
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('runbook_logging/testlog2.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

```
You can also do a logging.exception inside a try/except block to log the traceback errors.

If you want this logging to show up on your console window you can use a stream Handler.


### Other
if you call a method without the parentheses, the code will call a memory reference to the method. 