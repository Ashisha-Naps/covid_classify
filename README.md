SUPERVISED LEARNING - COVID AUDIO CLASSIFICATION

Tools
  -- Vscode

packages
  --Pandas, Dataframe
  --librosa -- handles audio 
  --sklearn -- preprocessing labelencoder , standardscalar
            -- model_selection train_test_split
 --xgboost -- xgbclassifier           

Data gathering
    Dataset -- https://www.kaggle.com/datasets/andrewmvd/covid19-cough-audio-classification

EDA - 
    1 > removed duplicate values
    2 > removed missing values
    3 >used Smote - to balance the classes
    4 >features extracted from audio file using librosa
                -- MFCC
                -- Chroma
    
    
    
