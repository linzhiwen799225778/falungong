from home.models import *
class Book:
    def __init__(self,id,num):
        book=TBook.objects.get(id=id)
        self.id=id
        self.num=int(num)
        self.picture=book.phone
        self.name=book.book_name
        self.price=book.dd_price
class Car:
    def __init__(self):
        self.booklist=[]
    def addbook(self,id,num=1):
        book=self.getbook(id)
        if book:
            book.num+=num
        else:
            book=Book(id,num)
            self.booklist.append(book)
    def delbook(self,id):
        book=self.getbook(id)
        if book:
            self.booklist.remove(book)

    def updatenum(self,id,num):
        book = self.getbook(id)
        book.num=num

    def getbook(self,id):
        for book in self.booklist:
            if book.id==id:
                return book
