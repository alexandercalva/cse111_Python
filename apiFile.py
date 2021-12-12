import csv


   
def read_Scriptures(filename):
  # Enter information for the customer
  nameBook = str(input("Enter the book name: "))
  chapterBook = str(input("Enter the chapter: "))
  verseNumber = str(input("Enter the number of verse: "))
  try: 
   # Open the file with all information about the scriptures 
   with open("scriptures.csv", "rt") as fileLDS:
      books = {}
      reader = csv.reader(fileLDS)
      next(reader)
      try: 
        for row in reader: # Search all information in the file
            book_id = row[1]
            books[book_id] = row[5] # Name of the book
            for book in books.items(): # Search only the books
              if(book[1] == nameBook): # Validate if the book entered for the customer is the same than in the file
                if(chapterBook == row[14]): # Validate if the chapter is the same
                  if(verseNumber == row[15]): # Validate if the verse is the same
                    nameBook = " " # If the customer found the verse, the name of book is not necessary search again
                    text = row[16] # Verse found
                    return text
      except:
        print("Try again please.") 
  except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

      

def main():
  #scripture = Input_scriptures()
  print("Program to search any scripture by book, chapter, and verse")
  showWords = read_Scriptures("scriptures.csv") # Call the function read_Scriptures
 
  if showWords != None:
    print (f'"{showWords}"')
  else:
    print("The book, chapter, or verse does not exist")

if __name__ == "__main__":
  main()
  
