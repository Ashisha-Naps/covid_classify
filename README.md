SUPERVISED LEARNING - COVID AUDIO CLASSIFICATION 

  

Tools 

   	-- Vscode 

  

Packages 

	  --NumPy—array operations 

  	--Pandas-- Dataframe 

  	--librosa -- handles audio  

  	--sklearn -- preprocessing labelencoder , standardscalar 

            	-- model_selection train_test_split 

    --xgboost -- xgbclassifier            

Steps  

  1 > **Data gathering** -  https://www.kaggle.com/datasets/andrewmvd/covid19-cough-audio-classification 

  2 > **EDA** -  

    i > removed duplicate values 

    ii > removed missing values 

    iii >used Smote - to balance the classes 

    iv >features extracted from audio file using librosa 

                -- MFCC -- Mel-Frequency Cepstral Coefficients (MFCCs) are a set of features that represent the spectral envelope of a sound signal. They are commonly used in  speech recognition systems and for modeling the                                                       characteristics of the human voice. 

                -- Chroma -- represents the tonal content of a musical audio signal in a condensed form
 
 3 >**Model Selection** – XgboostBinaryClassifier 

 4 > **Data Preprocessing** -  

        i> Concatenate both the features into single feature 
        ii>splitting Data into train set and testing set with 80:20 ratio 	 

 5 >**Model Training** –  

      i> training model with Train set with 5-fold of cross validation. 
      ii>setting Eval metric – auc 

 6> **Model Performence Metric** -   

      i> The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. The precision is intuitively the ability of the classifier not to label a negative sample as positive. 
      ii>The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples. 
      iii>The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall, where an F-beta score reaches its best value at 1 and worst score at 0. 
      iv>The F-beta score weights recall more than precision by a factor of beta. beta == 1.0 means recall and precision are equally important. 

  

  

Accuracy: 0.83 

              precision    recall  f1-score   support
     healthy       0.84      0.94      0.89      2528
 symptomatic       0.78      0.57      0.66      1004

  

    accuracy                           0.83      3532
   macro avg       0.81      0.75      0.77      3532
weighted avg       0.83      0.83      0.82      3532 

  

  

![image](https://github.com/user-attachments/assets/6f689a8d-4cee-44c9-8975-09c88b2d7386) 

  

     

     

     

 



    
    
    
