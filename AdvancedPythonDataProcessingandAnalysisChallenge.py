import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

# Read  travel blog entries 
with open('travel_blogs.txt', 'r') as file:
    blog_text = file.read()
sid = SentimentIntensityAnalyzer()

sentences = nltk.sent_tokenize(blog_text)

positive_words = []
negative_words = []

positive_word_list = ['amazing', 'enjoy', 'beautiful']
negative_word_list = ['bad', 'disappointing', 'poor']

for sentence in sentences:
    sentiment_scores = sid.polarity_scores(sentence)
    if sentiment_scores['compound'] > 0:
        positive_words.extend(nltk.word_tokenize(sentence))
    elif sentiment_scores['compound'] < 0:
        negative_words.extend(nltk.word_tokenize(sentence))

positive_count = len([word for word in positive_words if word.lower() in positive_word_list])
negative_count = len([word for word in negative_words if word.lower() in negative_word_list])

print(f"Positive word count: {positive_count}")
print(f"Negative word count: {negative_count}")