Hello,
This is NLP+Regression hybrid model
In this Model I used Sentence Transformer for feature extraction, Ridge regression model because i was getting good evaluation there compare to others. This model Works on The concept of Keywords where it detect the keyword and do calculation according to the keyword . I declared 3 catagory High urgency , Medium Urgency, Low urgency.
D1.ipynb contain model+ embeddings+evaluation 
testing.py contain my Gradio deployment 
Dataset which I used: https://www.kaggle.com/datasets/wcukierski/enron-email-dataset

+I deployed this model on Gradio for testing purposse.

+I tested this model on my personal mails, result : out of 20 i got 14 correct and other 6 i am confused 

Note : there might be some biasness because of keywords, I choose them which I though could be importantb for model


And I forgot to add all eval matrices so I am mentioning here,

MAE: 0.18516796955636677
MSE: 0.05472790908511526
RMSE: 0.23393996897733244
R2 Score: 0.6449990189088164

