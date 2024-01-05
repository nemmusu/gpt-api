# Readme
[README: Italiano](./README_IT.md)

[README: English](./README.md)

# GPT Chat Bot
This project provides a Python script to interface with OpenAI's GPT language model and a GUI to use it.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Configuration File](#configuration-file)
   - [Using the GPT Class](#using-the-gpt-class)
   - [gpt.py Script](#gptpy-script)
3. [Interface](#interface)
4. [Creating the Executable](#creating-the-executable)
   - [PyInstaller](#pyinstaller)
   - [cx_Freeze](#cxfreeze)

## Installation <a name="installation"></a>
To install the project, follow these steps:

1. Download the project from the GitHub repository. Open the terminal and navigate to the folder where you want to download the project. You can do this using the `cd` command followed by the folder path.
    ```shell
    cd /path/to/folder
    ```
2. Clone the repository using the `git clone` command followed by the repository URL:
    ```shell
    git clone https://github.com/nemmusu/gpt-api.git
    ```
3. Access the project folder:
    ```shell
    cd gpt-api
    ```
4. Install the required `openai` library for this project:
    ```shell
    pip install openai
    ```

## Usage <a name="usage"></a>

### Configuration File <a name="configuration-file"></a>
The `config.ini` file is used to configure various aspects of the chat bot. Here is an example of how it could be configured:

```ini
[OPENAI]
api_key = your_api_key
question = What do you recommend doing today?
temperature = 0.7
model = gpt-3.5-turbo
system_role_message = You are an expert assistant and will answer my questions in a specific and detailed manner using markdown format.
```

### Using the GPT Class <a name="using-the-gpt-class"></a>
To use the GPT class, create an instance of GPT and call the `get_chat_response()` method. All parameters are optional and if not specified, will be fetched from the configuration file.

Here is an example usage without parameters:
```python
from gpt import GPT

chatbot = GPT() # Uses default values from the configuration file
response = chatbot.get_chat_response()
print(response)
```

And an example usage with parameters:
```python
from gpt import GPT

chatbot = GPT(config_file='/etc/gpt-api/config.ini', api_key='your_api_key', question='What is the meaning of life?', 
              temperature=0.5, model='gpt-4', 
              system_role_message='You are an expert assistant and will answer my questions in a specific and detailed manner using markdown format.')
response = chatbot.get_chat_response()
print(response)
```

The parameters you can use are as follows:

- `config_file`: The path to the configuration file (default: `config.ini`)
- `api_key`: The OpenAI API key
- `question`: The question to pass to the GPT model
- `temperature`: The temperature for the GPT model
- `model`: The GPT model to use
- `system_role_message`: The system role message for the GPT model

### gpt.py Script <a name="gptpy-script"></a>
The `gpt.py` script can be run standalone or imported as a module. All parameters are optional and if not specified, will be fetched from the configuration file.

You can run it using the following command:
```shell
python gpt.py --question "What do you recommend doing today?" --temperature 0.7 --model gpt-3.5-turbo
```
The available parameters are:

- `--config`: Path to the configuration file (default: `config.ini`).
- `--api_key`: The API key for OpenAI.
- `--question`: The question to pass to the GPT model.
- `--temperature`: The temperature for the GPT model.
- `--model`: The GPT model to use.
- `--system_role_message`: The system role message for the GPT model.

To view the command's help, run:
```shell
python gpt.py --help
```

## Interface <a name="interface"></a>
The interface implemented in `gui.pyw` uses PyQt5. To install PyQt5, run the command:
```shell
pip install pyqt5
```
To run the GUI interface, use the command:
```shell
python gui.pyw
```

## Creating the Executable <a name="creating-the-executable"></a>

### PyInstaller <a name="pyinstaller"></a>
To create an executable using PyInstaller, you need to install PyInstaller on your system. You can do this using the following command:

```
pip install pyinstaller
```

Once PyInstaller is installed, you can create the executable using the following command:

```
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtWidgets
```

This command creates a single executable file named "GUI_ChatGPT" using "gui.pyw" as the entry point. It also specifies some hidden dependencies like "gpt", "argparse", "configparser", "openai", "PyQt5.QtCore", and "PyQt5.QtWidgets" that need to be included in the executable.

### cx_Freeze <a name="cxfreeze"></a>
To create an executable using cx_Freeze, you need to install cx_Freeze on your system. You can do this using the following command:

```
pip install cx_Freeze
```

Once cx_Freeze is installed, you can create the executable using the following command:

```
python compile_cx_freeze.py build
```

This command will create a structured package with folders containing the executable and necessary libraries.

# Screenshot

![Screenshot](https://github.com/nemmusu/gpt-api/blob/main/screenshots/interface_example.png)