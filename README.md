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
Install all necessary Python packages:
<pre>pip install -r requirements.txt</pre>

Alternatively, create a virtual environment:
<pre>python3 -m venv myenv  
source myenv/bin/activate  
pip install -r requirements.txt</pre>

# Model training and prediction 
(this part still nd to clarify if we need them to train the model themselves or js use model pkl)
## 1. Model Training  
Use the `train_model.py` script to train a new model on RNA-Seq data.  

Command: <pre>python train_model.py --data ./data/train_data.json --labels ./data/labels.csv --output ./models/model.pkl</pre>

Inputs:  
  - RNA-Seq data processed by m6Anet (`train_data.json`)  
  - Labels file containing m6A site information (`labels.csv`)

Output:  
  - Trained model saved as `model.pkl` in `models/` directory
    
## 2. Making Predictions  
Use the predict_m6A.py script to make predictions on new data.  

Command:  
<pre>python predict_m6A.py --data ./data/test_data.json --model ./models/model.pkl --output ./predictions.csv</pre>

Inputs:  
  - RNA-Seq test data (`test_data.json`)  
  - Optional: Pre-trained model (`model.pkl`)

Output:  
  - A CSV file with predicted m6A sites (`predictions.csv`)

# Issues
- Instance Limitations:
  Low-memory instances may encounter issues (e.g. insufficient memory, runtime error) during model training. Consider using larger instance types if faced with these issues.
