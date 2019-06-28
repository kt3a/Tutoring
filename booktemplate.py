##practice with objects, inherritance, and getter/setter functions
##Virtual Library Project

class book:

    def __init__(self, title, author):
        ##create this constructor
        
    def get_title(self):
        ##fill this out so that it will return the title of the book
        
    def get_author(self):
        ##fill this out so that it will return the author of the book
        
    def change_title(self, new_title):
        ##fill this out so that it will reset the title
        
    def change_author(self, new_author):
        ##fill this out so that it will make a new author
        
    def __str__(self):
        ##fill out this string function so that it will print the book title in quotes and then the authors name
        ##format: "Harry Potter," by JK Rowling
        return "\"{},\" by {}".format(self.title, self.author)

class comics(book):

    #hint: you dont need to rewrite the get and set functions from above and you can still call those functions on a comic book object
    
    def __init__(self,title, author, protagonist, antagonist):
        ##dont forget the super() method
        

    def __str__(self):
        ##use the format: "Title," Author has {} protagonist and {} antagonist.
       

def main():
    ##create a list of book objects, it can contain both comic books and regular books
    ##then create a user input that will ask a person to pick what way they want to search for a book -- author or title
    ##then based on that they can type in an author's name to search for what kinds of books are in your list -- and whether or not that book is in our virtual library
    ##if the book is found --print it's information, if the book is not found ask them to search again and print an error that the book doesn't exist


main()
