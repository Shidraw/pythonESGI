def est_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
        return True

yourWord = input('Saisissez votre mot : ')

if est_palindrome(yourWord):
    print('Votre mot est un palindrome !')
else:
    print('Pas lindrome')