#  Create a class Book with the following attributes:
# • title
# • author
# • list of reviews
# And add methods to:
# • add a new review
# • count reviews
# • display all reviews

class Book:
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews = reviews

    def add_review(self, new_review):
        self.reviews.append(new_review)
        print(f"Added the {new_review} review for {self.title}")

    def print_reviews(self):
        print(f"Review/reviews for '{self.title}' title is/are:")
        for review in self.reviews:
            print(review)

    def count_reviews(self):
        return len(self.reviews)

        
book1 = Book("The Night We Met", "Ruskin Bond", ["Good"])
book2 = Book("Sunday Morning", "Adam Sunday", ["Very Good"])
book3 = Book("Data Structure in C++", "James Bond", ["Bad"])

print(f"The review/reviews for {book1.title} written by {book1.author} is/ are: {book1.reviews}")
print(f"The review/reviews for {book2.title} written by {book2.author} is/ are: {book2.reviews}")
print(f"The review/reviews for {book3.title} written by {book3.author} is/ are: {book3.reviews}")


print("Do you want to perform any actions?")
x = input("Enter Yes or No: ").lower()
if(x=="yes"):
    print("Select the operation from below you want to perform:\n" \
    "1. Add a new review\n" \
    "2. Count Reviews\n" \
    "3. Display all reviews")
    y = int(input("Enter 1/2/3:" ))
    print("Enter the serial no. of the title from below:\n\n" \
        "1. The Night We Met\n" \
        "2. Sunday Morning\n" \
        "3. Data Structure in C++")
    z = int(input("Enter the serial number of the title:" ))
    if(y==1):
        p = int(input("Enter the number of reviews you want to add: "))
        i = 0
        if(z==1):
            while(i<p):
                q = input("Enter the new review: ")
                book1.add_review(q)
                i+=1
            print("The new reviews are:\n")
            print(book1.reviews)
        elif(z==2):
                while(i<p):
                    q = input("Enter the new review: ")
                    book2.add_review(q)
                    i+=1
                print("The new reviews are:\n")
                print(book2.reviews)
        elif(z==3):
                while(i<p):
                    q = input("Enter the new review: ")
                    book3.add_review(q)
                    i+=1
                print("The new reviews are:\n")
                print(book3.reviews)
        else:
            print("Invalid Input!")

    elif(y==2):
        if(z==1): 
            print(f"The total count of review/reviews of {book1.title} is {book1.count_reviews()}")
        elif(z==2):
            print(f"The total count of review/reviews of {book2.title} is {book2.count_reviews()}")
        elif(z==3):
            print(f"The total count of review/reviews of {book3.title} is {book3.count_reviews()}")
        else:
            print("Invalid Input!")

    elif(y==3):
        if(z==1):
            book1.print_reviews()
        elif(z==2):
            book2.print_reviews()
        elif(z==3):
            book3.print_reviews()
        else:
            print("Invalid Input!")

    else:
        print("Invalid Input!")

    # new_review = input("Enter the ")
    # book3.add_review("Worst")
    # book3.print_reviews()
    # print(f"Total number of reviews for {book3.title} is {book3.count_reviews()}")