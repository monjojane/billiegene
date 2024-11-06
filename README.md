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

After installation, you can verify the packages were installed successfully:
```bash
pip list
```
## Note
Ensure you have done the AWS setup guide and installed all necessary dependencies before running the code below.  

# Model training and prediction

## Data parsing
The raw json data is parsed and aggregated using `data_parsing.py` into a readable csv format.

A test data set is available for you to test the script. To run the script with the test data set:

**Step 1:** Change directory into the `data` folder:
```bash 
cd data
```
**Step 2:** Using the `ls` command, ensure that the raw json file (`test_data.json`) is in the `data` folder. 

**Step 3:** Run the data parsing script:
```bash 
python3 data_parsing.py
```
**Step 4:** Using the `ls` command, ensure that the parsed data have been saved successfully as `parsed_test_data.csv`.

## Model Training 
The model is trained and tuned using our pre-determined parameters and features. The trained model (`model.pkl`) is then generated from the model training script (`model_training.py`). 

`aggregated_data.csv` and `underbalanced_labels.csv` are used in the training script (`model_training.py`) and they can be found in the `data` folder. 

The model training script (`model_training.py`) and trained model file (`model.pkl`) can be found in the `models` folder. However, you <ins>do not</ins> need to run the training script as the trained model is already loaded in the prediction script (`predictions.py`). 

## Generating predictions
The prediction script (`predictions.py`) uses the trained model (`model.pkl`) to make m6A site predictions on the test data set (`parsed_test_data.csv`). 

**Step 1:** Using the `ls` command, ensure that `parsed_test_data.csv` is present in the `data` folder. 

**Step 2:** Change directory into the `predictions` folder: 
```bash 
cd ../predictions
``` 

**Step 3:** Run prediction script: 
```bash 
python3 prediction.py
```

**Step 4:** Using the `ls` command, ensure that the generated predictions have been saved successfully as `prediction_results.csv`. 

**Step 5:** To view the first few rows of the predictions csv file 
```bash 
head prediction_results.csv
```

Here is an example of how the predictions should look like:

<img width="380" alt="Screenshot 2024-11-01 at 1 44 01 PM" src="https://github.com/user-attachments/assets/ea2661ad-5642-4eba-bda3-d0e5bd5757fa">

# Issues
- Instance Limitations:
  Low-memory instances may encounter issues (e.g. insufficient memory, runtime error) during model training. Consider using larger instance types if faced with these issues.
