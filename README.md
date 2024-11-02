# Prediction of m6A RNA Modifications from Direct RNA-Seq Data
DSA4262 Project (team: billiegene)

# Table of Contents
1. [Repository Structure](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#repository-structure)
2. [AWS Setup Guide](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#aws-setup-guide)
3. [Prerequisites](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#prerequisites)
5. [Model training and prediction](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#model-training-and-prediction)
6. [Issues](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#issues)

# Repository Structure
- /data - Test data and code for data parsing and manipulation
- /models - Trained model file and script for model training
- /predictions - Expected predictions csv file and script for predictions
- README.md - Main documentation
- requirements.txt - Dependencies


# AWS Setup Guide 
1. Launch an EC2 Instance
   1. Create an ubuntu instance on Research Gateway
   2. Select instance type: `t3.medium` (or higher)
2. Install git 
```bash
sudo apt update && sudo apt install -y git python3-pip 
```
3. Clone the billiegene repository
``` bash
git clone https://github.com/monjojane/billiegene.git  
```
4. `cd` into billiegene
```bash
cd billiegene
```

# Prerequisites

## System Requirements 
- AWS Ubuntu EC2 instance (tested on t3.medium or higher)
- Python 3.8+

## Dependencies 
Ensure that you are in the project directory `billiegene`, else naviate to that directory using this command:
```bash
cd billiegene
```

Install all necessary Python packages:
```bash
pip install -r requirements.txt
```

Alternatively, create a virtual environment:
<pre>python3 -m venv myenv  
source myenv/bin/activate  
pip install -r requirements.txt</pre>

After installation, you can verify the packages were installed successfully:
```bash
pip list
```

# How to run the method on AWS

To run/test the scripts, ensure you have done the AWS setup guide and installed all necessary dependencies as mentioned above. 

Then follow these step-by-step instructions:

## Data parsing
Use `data_parsing.py` to parse your raw json data into a readable csv format.
Ensure that the raw json file is in the `data` folder.

A test data set is available for you to test the script. To run the script with the test data set:

**Step 1:** `cd` into the `data` folder.

**Step 2:**  Ensure that the dataset you would like to parse is correctly stated in the script `data_parsing.py`.

**Step 3:** Run `data_parsing.py`.

```bash 
python3 data_parsing.py
```

## Training the model (Optional)
Use `model_training.py` to train the model.

**Step 1:** `cd` into the `model` folder.

**Step 2:** Run the `model_training.py` script.

```bash
python3 model_training.py
```

## Making predictions
Use `prediction.py` to make predictions. This script loads the saved trained model and uses it to make predictions on a set of data you input.

**Step 1:** Ensure the dataset (parsed csv file) you wish to make predictions on is in the `data` folder.

**Step 2:** Edit the `prediction.py` script to input the csv file.

**Step 3:** `cd` into the `predictions` folder.

**Step 5:** Run `prediction.py`.

```bash
python3 prediction.py
```

# Example Usage
We already have a dataset ready (`example_parsed_data.csv`) to make predictions on. This dataset has been parsed and aggregated using our scripts. 

We have also saved the trained model as `model.pkl` which is already loaded in the `prediction.py` script.

All you have to do is `cd` into `prediction` folder and run the `prediction.py` file to generate the results.

```bash
python3 prediction.py
```
Here is an example of how the predictions should look like:
<img width="380" alt="Screenshot 2024-11-01 at 1 44 01 PM" src="https://github.com/user-attachments/assets/ea2661ad-5642-4eba-bda3-d0e5bd5757fa">

# Issues
- Instance Limitations:
  Low-memory instances may encounter issues (e.g. insufficient memory, runtime error) during model training. Consider using larger instance types if faced with these issues.
