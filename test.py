class Palindrome:
    @staticmethod
    def is_palindrome(mot):
        return mot == mot[::-1]

print(Palindrome.is_palindrome("aba"))
