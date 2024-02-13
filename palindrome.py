def is_palindrome(word):
    word = word.replace("", "").lower()
start=0
end=len(word)-1
    while start < end:
    if word[start]!= word[end]:
        return False
        start+=1
        end-=1
        return true

input_word = input("was it a girl or a boy")
if is_palindrome(input_word):
    print(f"{input_word}is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")
Enter a word or phrase:Madam
Madam is a palindrome





