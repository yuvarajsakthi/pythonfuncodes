input_sentence=input("Enter a sentence here: ")
# sentence=input_sentence.lower()
sentence= input_sentence.upper() 
print(sentence)
count=0
vowles=["a","e","i","o","u"]
for char in sentence:
    if char in vowles:
        count=count+1
print(" The number of Vowles in a given Sentence is :", count)

