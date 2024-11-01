# Prediction of m6A RNA Modifications from Direct RNA-Seq Data
DSA4262 Project (team: billiegene)

# Table of Contents
1. [Repository Structure](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#repository-structure)
2. [AWS Setup Guide](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#aws-setup-guide)
3. [Prerequisites](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#prerequisites)
5. [Model training and prediction](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#model-training-and-prediction)
6. [Issues](https://github.com/monjojane/billiegene/tree/main?tab=readme-ov-file#issues)

# Repository Structure
- README.md - Main documentation
- requirements.txt - Dependencies
- /data - Test data and code for data parsing and manipulation
- /model - Trained model file and script for model training
- /predictions - Expected predictions csv file and script for predictions

# AWS Setup Guide 
1. Launch an EC2 Instance
   1. Create an ubuntu instance on Research Gateway
   2. Select instance type: `t3.medium` (or higher)
2. Install git and clone the billiegene repository
<pre>sudo apt update && sudo apt install -y git python3-pip  
git clone https://github.com/monjojane/billiegene.git  
cd billiegene</pre>

# Prerequisites

## System Requirements 
- AWS Ubuntu EC2 instance (tested on t3.medium or higher)
- Python 3.8+

## Dependencies 
Ensure that you are in the project directory `billiegene`, else naviate to that directory using this command:
<pre>cd billiegene</pre>

Install all necessary Python packages:
<pre>pip install -r requirements.txt</pre>

Alternatively, create a virtual environment:
<pre>python3 -m venv myenv  
source myenv/bin/activate  
pip install -r requirements.txt</pre>

After installation, you can verify the packages were installed successfully:
<pre>pip list</pre>

# Usage

To run/test the scripts, follow these step-by-step instructions:

## Data parsing
Use `data_parsing.py` to parse your raw data into a readable format.

Ensure that the raw json file is in the `data` folder.

**Step 1:** `cd` into the `data` folder

**Step 2:**  Run the `data_parsing.py` script.

```bash 
python3 data_parsing.py
```

## Training the model (Optional)
Use `model_training.py` to train the model.

**Step 1:** Ensure the paths in the `model_training.py` corresponds to the file you created in step 1.

**Step 2:** `cd` into the `model` folder.

**Step 3:** Run the `model_training.py` script.

```bash
python3 model_training.py
```

## Making predictions
Use `prediction.py` to make predictions.

This script loads the saved trained model and uses it to make predictions on a set of data you input

**Step 1:** Ensure the dataset (parsed csv file) you wish to make predictions on is under the `data` folder.

**Step 2:** Edit the script to input the csv file.

**Step 3:** Ensure the path to output_csv in `prediction.py` corresponds to the file you created in step 3.

**Step 4:** `cd` into the `prediction` folder.

**Step 5:** Run the `prediction.py` script.

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

# Model training and prediction 
(this part still nd to clarify if we need them to train the model themselves or js use model pkl)
## 1. Model Training  
Use the `model_training.py` script to train a new model on RNA-Seq data.  

Command: <pre>python model_training.py --data ./data/train_data.json --labels ./data/labels.csv --output ./models/model.pkl</pre>

Inputs:  
  - RNA-Seq data processed by m6Anet (`train_data.json`)  
  - Labels file containing m6A site information (`labels.csv`)

Output:  
  - Trained model saved as `rf_model_reduced_tuned_kfold.pkl` in `model/` directory
    
## 2. Making Predictions  
Use the `prediction.py` script to make predictions on new data.  

Command:  
<pre>python prediction.py --data ./data/test_data.json --model ./models/model.pkl --output ./predictions.csv</pre>

Inputs:  
  - RNA-Seq test data (`test_data.json`)  
  - Optional: Pre-trained model (`rf_model_reduced_tuned_kfold.pkl`)

Output:  
  - A CSV file with predicted m6A sites (`predictions.csv`)

# Issues
- Instance Limitations:
  Low-memory instances may encounter issues (e.g. insufficient memory, runtime error) during model training. Consider using larger instance types if faced with these issues.
