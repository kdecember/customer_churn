# Memo

## Business Relevance

This study was conducted in an attempt to predict which customers will soon cancel their account with us. By predicting which customers are at risk of cancelling, we would be able to mitigate customer churn by enacting preventative measures before they actually cancel their account. 

## Final Model

We ultimately deployed a Gradient Boosting algorithm as our predictive model. This model utilized several factors from customer accounts in order to predict whether or not they would cancel their accounts in the near future. While we cannot say  which factor is most important with certainty, we can say that when accounting for all the included factors, we can identify roughly 88% of all customers who are at risk of leaving.

The reason we didn't push this number to 100% is because if we force our model to perfectly identify customer churn in the training data, then it won't be able to generalize well to the total population of accounts. This would ultimately result in a less effective model.

## Conclusions & Further Analysis

We recommend deploying this algorithm in a real-world setting, as it will enable us to mitigate customer churn.

We would also like to perform subsequent analysis on the methodologies used for customer retention, and whether or not those methodologies worked. This data, combined with the data identifying at risk customers, would allow us to predict whether or not customers will accept retention offers. This would allow us to identify customers who are at risk of leaving, but who are also willing to stay if given a specific retention offer, thereby allowing us to focus our retention resources more effectively.