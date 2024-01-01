# Readme
[README in italiano](./README_IT.md)

[English README](./README.md)

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

1. Download the project from the GitHub repository. Open the terminal and go to the folder where you want to download the project. You can do this using the `cd` command, followed by the path of the folder.
    ```shell
    cd /path/to/folder
    ```
2. Clone the repository using the `git clone` command, followed by the URL of the repository:
    ```shell
    git clone https://github.com/nemmusu/gpt-api.git
    ```
3. Access the project folder:
    ```shell
    cd gpt-api
    ```
4. Install the `openai` library needed for this project:
    ```shell
    pip install openai
    ```

## Usage <a name="usage"></a>

### Configuration File <a name="configuration-file"></a>
The `config.ini` file is used to configure various aspects of the chat bot. Here's an example of how it might be set up:

```ini
[OPENAI]
api_key = your_api_key
question = What do you suggest doing today?
temperature = 0.7
model = gpt-3.5-turbo
system_role_message = We are here to help you answer your questions.
```

### Using the GPT Class <a name="using-the-gpt-class"></a>
To use the GPT class, we create an instance of GPT and call the `get_chat_response()` method. All parameters are optional and, if not specified, will be taken from the configuration file.

Here's an example of use without parameters:
```python
from gpt import GPT

chatbot = GPT() # Uses the default values from the configuration file
response = chatbot.get_chat_response()
print(response)
```

And an example of use with parameters:
```python
from gpt import GPT

chatbot = GPT(config_file='/etc/gpt-api/config.ini', api_key='your_api_key', question='What is the meaning of life?', 
              temperature=0.5, model='gpt-4', 
              system_role_message='you are an expert assistant and will answer my questions in a specific and detailed manner exclusively in markdown format')
response = chatbot.get_chat_response()
print(response)
```

The parameters you can use are as follows:

- `config_file`: The path of the configuration file (default: `config.ini`)
- `api_key`: The API key for OpenAI
- `question`: The question to pass to the GPT model
- `temperature`: The temperature for the GPT model
- `model`: The GPT model to use
- `system_role_message`: The system role message for the GPT model

### gpt.py Script <a name="gptpy-script"></a>
The `gpt.py` script can be run on its own or imported as a module. All parameters are optional and, if not specified, will be taken from the configuration file.

You can run it using the following command:
```shell
python gpt.py --question "What do you suggest doing today?" --temperature 0.7 --model gpt-3.5-turbo
```
The available parameters are:

- `--config`: Path of the configuration file (default: `config.ini`).
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
To run the GUI interface, run the command:
```shell
python gui.pyw
```

## Creating the Executable <a name="creating-the-executable"></a>

### PyInstaller <a name="pyinstaller"></a>
To create an executable with PyInstaller, use the following command:
```shell
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtWidgets
```

### cx_Freeze <a name="cxfreeze"></a>
To create an executable with cx_Freeze, you need to have the `compile_cx_freeze.py` file in the same directory and then run the command:
```shell
python compile_cx_freeze.py build
```
The command will create a structured package with folders containing the executable and necessary libraries.