def reverse(words):
    
    for word in range(len(words)):
        print(words[word],end="")
    for word in reversed(range(len(words))):
        print(words[word],end="")
    print("\n")
    
reverse("good")
reverse("Python")
reverse("")
reverse("a") 
