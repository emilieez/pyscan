# PyScan3D
Uses data gathered from the Structure Sensor by Occipital to classify things into their respective shapes. 
Python is required to be able to run this program.

## Features:
**Mail Parser** - Log in to your email to select and download scans <br>
**Object Classifier** - Load a .obj or .ply file to classify its shape

## Installation:
Clone the repository using HTTPS:
```
git clone https://github.com/emilieez/pyscan.git
```

Clone the repository using SSH:

```
git clone git@github.com:emilieez/pyscan.git
```

## Run the PyScan virtual environment
A virtual environment is provided if the dependencies are not installed.
### Windows:

Run the following line in Command Prompt:
```
PyScan\Scripts\activate.bat
```

The terminal should now look something like this:
```
(PyScan) D:\pyscan>
```

### Linux or MacOS: 

Run the following line in the terminal:
```
source /PyScan/bin/activate
```

The terminal should now look something like this:
```
(PyScan) root@localhost:~/pyscan$
```

### Deactivate the Virtual Environment
To deactivate the virtual environment on Windows, simply type:
```
PyScan\Scripts\deactivate.bat
```
or on Linux/MacOS:
```
Deactivate
```

### Installing Dependencies
Alternatively, all dependencies can be installed using this command in the root folder of the repository:
```
pip install -r requirements.txt
```

## Running the PyScan3D Application
In the root folder of the repository type:
```
python pyscan.py
```