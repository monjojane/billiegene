# billiegene
DSA4262 Project 

## Structure
1) `data` folder
  - Contains datasets used as well as codes used to manipulate the data.

2) `model` folder
  - Contains code for creating the model as well as the model itself.

3) `prediction` folder
  - Contains code used to make predictions using the model as well as prediction csvs that were generated.

## Steps before running any files
1) Change directory in your terminal to `billiegene` and run `pip install -r requirements.txt`.
  - You may use a virtual environment if you wish to.

## How to run and use the model
#### 1. Model Training  
Use the train_model.py script to train a new model on RNA-Seq data.  

Command:  
python train_model.py --data ./data/train_data.json --labels ./data/labels.csv --output ./models/model.pkl
  
- Inputs:  
  - RNA-Seq data processed by m6Anet (in JSON format)  
  - Labels file containing m6A site information  
- Output:  
  - Trained model saved in models/ directory
    
#### 2. Making Predictions  
Use the predict_m6A.py script to make predictions on new data.  

Command:  
python predict_m6A.py --data ./data/test_data.json --model ./models/model.pkl --output ./predictions.csv
  
- Inputs:  
  - RNA-Seq test data (in JSON format)  
  - Optional: Pre-trained model  
- Output:  
  - A CSV file with predicted m6A sites
