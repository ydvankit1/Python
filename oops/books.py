class Book:
    def __init__(self, bookid, bookname, bookholder):
        self.bookid=bookid
        self.bookname=bookname
        self.bookholder=bookholder  

    def findBookByName(self,booklist, bookname):
        # self.booklist=booklist
        # for book in self.booklist: (if directly using this then get AttributeError:
# 'Book' object has no attribute 'bookList')
        for book in booklist:
            if book.bookname.lower()==bookname.lower():
                return book
        return None
    
    def sortBookByName(self, booklist):
        if(len(booklist))<2:
            return None
        srtdlst=sorted(booklist, key=lambda x: x.bookname.lower()) #by default sorting give priority to uppercase letter 
        # storing in srtdlst because sorted function generate new updated list, if want to update original list use: 
        # booklist.sort(key=lambda x: x.bookname.lower())
        return srtdlst[1]
    
if __name__ == "__main__":
    n=int(input())
    booklist=[]
    for i in range(n):
        bookId=int(input())
        bookname=input()
        bookholder=input()
        bkObj=Book(bookId, bookname, bookholder)
        booklist.append(bkObj)

    srchbk=input()
    obj=booklist[0]
    result=obj.findBookByName(booklist, srchbk)
    if result is None:
        print("No Data Found")
    else:
        print(result.bookid)
        print(result.bookname)
        print(result.bookholder)
    
    scndbk=obj.sortBookByName(booklist)

    if scndbk is None:
        print("No Data Found")
    else:
        print(scndbk.bookid)
        print(scndbk.bookname)
        print(scndbk.bookholder)
