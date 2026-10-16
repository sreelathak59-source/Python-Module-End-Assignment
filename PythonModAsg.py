#------- Step : 1  Preloaded Feedbacks -------

print("----- Survey Feedback Analyzer -----")
feedback_data = {
    'S_No' : [1,2,3,4,5,6,7,8,9,10],
    'Name' : ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback' : ['Very GOOD Service!!!', 'poor support, not happy ',
                  'GREAT experience! will come again.', 'okay okay...',
                  ' not BAD', 'Excellent care, excellent staff!',
                  'good food and good ambience!', 'Poor response and poor handling of issue',
                  'Satisfied. But could be better.', 'Good support... quick service.'],
    'Ratings' : [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
print(feedback_data)

#------- Step 2: Add More Feedbacks -------
print("\n----- Adding FeedBacks -----\n")
n=int(input("Enter how many more feedbacks you want to add : "))
for i in range(n) :
    feedback_data['S_No'].append(len(feedback_data['S_No'])+1)
    name=input("Enter the name : ")
    feedback_data['Name'].append(name)
    feed=input("Enter the Feedback : ")
    feedback_data['Feedback'].append(feed)
    rat=int(input("Enter the Ratings : "))
    feedback_data['Ratings'].append(rat)
print(feedback_data)

#------- Step 3: Text Cleaning -------
print("\n------ Text Cleaning -------\n")
for i in range(len(feedback_data['Feedback'])):
    old_text = feedback_data.get("Feedback")[i]
    feedback_data['Feedback'][i] = feedback_data['Feedback'][i].replace("!","")
    feedback_data['Feedback'][i] = feedback_data['Feedback'][i].replace(".","")
    feedback_data['Feedback'][i] = feedback_data['Feedback'][i].replace(",","")
    feedback_data['Feedback'][i] = feedback_data['Feedback'][i].replace("?","")
    feedback_data['Feedback'][i] = ' '.join(feedback_data['Feedback'][i].split())
    feedback_data['Feedback'][i] = feedback_data['Feedback'][i].strip()
    feedback_data['Feedback'][i] = feedback_data['Feedback'][i].lower()
    print(old_text ,"  :  " ,feedback_data.get("Feedback")[i])
print(feedback_data)

#------- Step 4: Word Count Insights -------
print("\n---Counting of Words(Good,Poor,Excellent) in Feedback---\n")
def count_word_in_feedbacks(word):
    n = 0
    for i in range(len(feedback_data['Feedback'])):
        words=feedback_data['Feedback'][i].split()
        for j in range(len(words)):
            if words[j].lower() == word.lower() :
                n = n + 1
    print(f'The word {word} appeared {n} times')
    return n

w=input("Enter the one word want to be counted : ")
count_word_in_feedbacks(w)


#------- Step 5: Final Summary & Insights -------
print("\n---Cleaned Data---\n")
print(feedback_data)

print("\n---Average---\n")
def average():
    sum=0
    for i in range(len(feedback_data['Ratings'])) :
        sum = sum + feedback_data['Ratings'][i]
    return sum/len(feedback_data['Ratings'])
avg=average()
print("---Average of Rating is : ", avg)

print("\n---Longest Comment---\n")
max_count = 0
for i in range(len(feedback_data['Feedback'])):
    h = feedback_data['Feedback'][i].split()
    word_count=len(h)
    if word_count > max_count :
        max_count = word_count
        longest_feedback = feedback_data['Feedback'][i]
print("Longest Feedback : ",longest_feedback)
print("Words Count : ", max_count)

print("\n---List of unique words---\n")
unique_words = []
for i in range(len(feedback_data['Feedback'])):
    uni = feedback_data['Feedback'][i].split()
    for u in uni :
        if u not in unique_words :
            unique_words.append(u)
print("Unique words in Feedback are : ", unique_words)

print("\n---Zipped and Sorted---\n")
zipped_file = sorted(zip(feedback_data['Ratings'],feedback_data['Feedback']),reverse=True)
print(zipped_file)

 