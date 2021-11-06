# EmotionDetection from textual comments and feedback
# Objective
Aim is to make machines understand and detect emotions from any textual input. A text based emotion recognition system which give an overall sentiment of the sentence/paragraph in terms of the overall emotion.

# Work Done:
Analyse the impact of effective words on the sentence.
Used supervied learning models to classify the emotion classes on given sentence.
Further work includes Emotional analysis on a given sentence/paragraph .

# Dependencies:
Numpy
Pandas
matplotlib
NLTK
sklearn
Python3

# Dataset:
   http://https//data.world/crowdflower/sentiment-analysis-in-text



# Overview:
Approach followed is:

Raw data set: It contains 2000 tweets and 4columns.

# Data Preprocessing:

Pre - processing includes:

->converting all text into lowercase

->Removal of Punctuations using string library

->Tokenizing the input text into tokens using word_tokenize from NLTK

->Removal of lemmas (Lexicon Normalization) using WordNetLemmatizer from NLTK

->Removal of multi-letter ambiguities, e.g 'noooo' gets converted to 'no'

->Removal of stop-words - caused decrease in f1-score as well as overall accuracy


# CountVectorization:
 Words are vectorized each vector represnts the category of emotion.

# Training Model:
 Naive bayes is used to train the model
 data is splitted into train & test using train_test_split from sklearn
# Accuracy
 Naive Bayes(On 2000 tweets): 53%
