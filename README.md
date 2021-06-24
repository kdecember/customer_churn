# Customer Churn Analysis

## Business Understanding:
Our data did not come with much of a description, so we concluded that it was data from a mobile phone service provider trying to figure out how to keep customers from leaving. We decided from this conclusion that the most important thing for this company to be able to predict is if a customer is about to leave so that they may be able to incentivise a customer to keep their business. Using this knowledge of the problem we determined that having a small false negative rate (predicting a customer would stay when they are actually canceling their service) would be the most important factor to building a successful model. Now you might be thinking about false positives - predicting a customer would leave when they actually are staying. In this case, it is cheaper for a company to give someone a better deal when they are planning to stay anyway than losing a customer that they thought would keep doing business with them. This is why we focused on recall score first and then f1-score to make sure we are not just giving away incentives.

## Data Understanding:

We weren’t provided any background explanation on what each category meant but luckily enough the labels were easy to understand. A couple questions did emerge where we had to make assumptions on. Chief among them was 'Is account length measured in days, weeks or months?'.

## Data Preparation/Modeling/Evaluation:

Step 1: Ran multiple models on the given data without any changes to the hyperparameters. This showed us that Random Forest and Gradient Boosting models gave us the best recall values for our data. From here we began our journey into feature engineering to find out which of these two models would provide us with the best balance between high recall and f1-scores.
Step 2: For feature engineering we tried a lot of things from using OneHotEncoder for our ‘state’ and ‘zip code’ columns, to adding and dividing columns together to create new features. Overall, we found our model had used the ‘total cost’ column the most. This column is the total amount a person was spending on this service. After some trial and error, we ultimately removed the ‘state’, ‘zip code’, ‘area code’, and ‘phone number’ columns because they were actually lowering the recall and f1-scores when predicting on our hold-out set. 
 
Step 3: In addition to removing the aforementioned columns, we also converted some columns into boolean values (True or False) to indicate whether or not a customer used certain aspects of the service. We converted the ‘international plan’ and ‘voice mail plan’ columns into boolean values, instead of keeping the original ‘yes’ or ‘no’ string values. 
 
Step 4: Our recall and f1-score were still below desired levels and at this point we began to experiment on feature engineering service costs. We created columns for ‘account months’, ‘total minutes’, ‘total calls’, ‘total cost’, and ‘cost per day’. After adding these columns, we brought our f1-score above .90 and our recall above .85 on a consistent basis.
 
Step 5: At this point, we began experimenting with hyperparameters but our best models continued to be the default hyperparameters of both Random Forest and Gradient Boosting. 

## Conclusion: 

We can conclude that given the data we have, the feature engineering we’ve done and the models we have tested - that Gradient Boosting is the best choice. The reason being that it provided the best balance between recall and f1-score, which were .88 and .93, respectively. We also found that changing the hyperparameters had little-to-no effect on the model's performance, and so were left as the default settings. 
