# What is PrettyLog?
PrettyLog is a logging library I have made in python. It's meant to be only used by me because who would stop using the regular logging library in exchange for this right? But anyways I made it public just incase anyone wanted to use it.

### Why?
Years ago when I was first starting out my programming journey I was too lazy to learn the logging library. So I decided to make my own (such a dumbass move), overtime I improved and still kept using my own logger rather than switching to the logging library (just why young me). Fast forward to 2022, now we're here.

## Features
- Colored printing.
- Organized logging onto files. Each level will have its own log file.
- Cached logs. Stores logs in the cache first before writing to a file in order to prevent spam.
- Group logs by name. This allows you to disable certain groups of logs if needed.

## Get Started
To get started, import the Logger class and initialize it.
```py
from prettylog import Logger

logging = Logger()
```

You can specify the following parameters for the `Logger()` class.

- `folder` : `str` Where to store all the log files.
- `file_format` : `str` Format of each log file. Defaults to .log (. should be included)
- `format` : `str` The format of the logs. This is not the same as file_format. Refer to the documentation below for the available formats.
- `debug` : `bool` Debug mode. Defaults to False. If True, print_level and file_level will automatically be set to debug.
- `print_level` : `str` What level to print on. Anything above and at this level will be printed. Defaults to info.
- `file_level` : `str` What level to write on. Anything above and at this level will be written to a file. Defaults to warning.
- `cache_size` : `int` How many logs to store in the cache before updating the file again. Defaults to 5.
- `disabled_group_prints` : `List[str]` List of groups that are disabled for printing. Defaults to None
- `disabled_group_files` : `List[str]` List of groups that are disabled for writing to a file. Defaults to None

## Logging Methods
You can pass a `group="my group"` parameter into each logging method to specify which group that specific log belongs to.
```py
logging.debug("This is a debug message")
logging.info("This is some info")
logging.success("Woah something happened successfully or smth idk")
logging.warning("Warning! Warning!")
logging.error("Error! Error!")
logging.critical("Oh shit critical error")
logging.Cr1TiKal("Moist") # Alias to .critical
```

## Formatting
You can format your logs to meet your needs and here's how.
```
[{level}] - [{iso_date}] - [{file:lineno}] {text}
```
The code above would then translate to
```
[INFO] - [2022-01-13T10:24:07.946115] - [app.py:50] This an informative log
```

If you'd like to add colored output then you would add `{COLORED}` at the very end like so.
```
[{level}] - [{iso_date}] - [{file:lineno}] {text} {COLORED}
```

That then translates to the following.
<pre>
    <span style="color: cyan">[INFO] - [2022-01-13T10:24:07.946115] - [app.py:50] This an informative log</span>
</pre>

> **NOTE**: Logging to a file will get rid of the strings that makes it colored.

### Properties
- `group`: The current group of the log
- `level`: The level of the log
- `iso_date`: The current date when this was logged in an `ISO 8601` format.
- `file`: The name of the file (not a full path).
- `file:lineno`: The name of the file together with the line where this log was called.
- `text`: The actual log text itself.
- `COLORED`: A special property that should only get added at the end. It indicated that the log should be colored.

### Other Methods

**set_group(group: str)**
- Set the default group to use

**clear_cache()**
- Manually clear the cache and dump whatever is inside it to the files.
- You'd normally want to call this before your program exits.
