# Pyrengine

Pyrengine is a lightweight graphics rendering and game engine build using Python and Vulkan. It aims to provide the clean interface of Python and the power of the Vulkan API. It is highly customizable and completely open-source. It's main usage is to be for rendering complex simulations from IPython and Jupyter notebooks but can be used to create video games.


# How to Run (Linux)
Currently only tested on Linux (Ubuntu 17.0.4) using Python 3.5.2

1. Install GLFW3 Development library on your system:
    ```
    $ sudo apt-get install libglfw3-dev
    ```
2. Install Python 3 virtualenv on your system:
    ```
    $ sudo pip3 install virtualenv
    ```
3. Initialise new virtual environment in root of project:
    ```
    $ virtualenv .env
    ```
4. Activate virtual environment:
    ```
    $ source .env/bin/activate
    ```
5. Install requirements:
    ```
    $ pip3 install -r requirements.txt
    ```
    
You can then run the app from /src/main/python/main.py

(WIP)
