Here is a comprehensive README file in Markdown format that integrates the information from both the `lab_4.py` and `main.py` scripts.

```markdown
# Python Applications

## Introduction
This repository contains two Python applications:
1. **Python Matrix Application**: An interactive game that includes phone number and zip code validation.
2. **Python Data Analysis App**: A data analysis tool for processing CSV files related to population changes and housing data.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To run these applications, ensure you have Python installed on your machine. You can download Python from the [official website](https://www.python.org/).

### Steps to Install:
1. Clone the repository:
    ```sh
    git clone https://github.com/Khakipapi/Python-Data-Analysis-App.git
    ```
2. Navigate to the project directory:
    ```sh
    cd python-applications
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Python Matrix Application
To start the Python Matrix Application, run the `lab_4.py` script:
```sh
python lab_4.py
```

#### Interactive Prompts
1. The program will prompt if you want to play the matrix game. Enter `Y` for Yes and `N` for No.
2. If you choose to play, you will be asked to enter a phone number in the format `xxx-xxx-xxxx`.
3. You will also be asked to enter a zip code.

### Python Data Analysis App
To start the Python Data Analysis App, run the `main.py` script:
```sh
python main.py
```

#### Data Analysis Options
1. The program processes `PopChange.csv` and `Housing.csv` files.
2. It will prompt you to select the column you want to analyze for population data.
3. Enter the corresponding option to view data or exit the column.

## Features

### Python Matrix Application
- **Matrix Game**: An interactive game that users can play.
- **Phone Number Validation**: Ensures the entered phone number is in the correct format.
- **Zip Code Validation**: Ensures the entered zip code is valid.

### Python Data Analysis App
- **Population Data Analysis**: Analyze different columns of population data from a CSV file.
- **Housing Data Analysis**: Analyze different columns of housing data from a CSV file.

## Dependencies
- Python 3.x
- numpy

You can install the dependencies using the following command:
```sh
pip install numpy
```

## Configuration
No specific configuration is needed for these applications. Ensure you have the required dependencies installed.

## Examples

### Running the Python Matrix Application
```sh
python lab_4.py
```
Example interaction:
```
Name: Jose Reyes
Course: SDEV300
Date: 2024-08-08
*************************Welcome to Python Matrix Application************************
Do you want to play the matrix game?
Enter y for Yes and n for No: y
Please enter your phone number (xxx-xxx-xxxx): 123-456-7890
Please enter your zip code: 12345
```

### Running the Python Data Analysis App
```sh
python main.py
```
Example interaction:
```
Name: Jose Reyes
Course: SDEV300
Date: 2024-08-08
***************** Welcome to the Python Data Analysis App**********
You have entered Population Data. Select the Column you want to analyze:
a. Pop Apr 1
b. Pop Jul 1
c. Change Pop
d. Exit Column
Enter your option: a
```

## Troubleshooting
- Ensure Python and the required packages are installed correctly.
- Verify the format of phone numbers and zip codes entered.
- Ensure the CSV files (`PopChange.csv` and `Housing.csv`) are in the correct directory and properly formatted.

## Contributors
- **Jose Reyes** - Initial work

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
