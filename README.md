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

The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. The precision is intuitively the ability of the classifier not to label a negative sample as positive.

The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.

The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall, where an F-beta score reaches its best value at 1 and worst score at 0.

The F-beta score weights recall more than precision by a factor of beta. beta == 1.0 means recall and precision are equally important.
    
    
    
