<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Prediction in outpatient visits]


## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The aim of this project is to provide a probability of non-attendance to improve communication with the patient and avoid missed visits.


## Dataset
The dataset has been obtained from a private source after anonymisation of the patients.

## Cleaning and columns transformation 
Initial columns= Date,name,treatment,zip code, nationality
After transformation= Week day, Week, gender, distance to the clinic, % of dropout about the treatment

For this transformation a scrapping of different webs was performed.


## Model Training and Evaluation
* Steps:
	- Dataset split
	- SMOTE for oversampling the X_train and y_train
	- Different classificators trial (ExtraTreeClassifier, AdaBoost, Gradient...)
	- GridSearch of the best classificators
	- Roc curve with Predict_proba of X_test

## Conclusion
PDF of the presentation: https://github.com/irazus13/Prediction_dropouts/tree/main/web
