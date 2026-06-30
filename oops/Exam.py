
# Create a class Exam having attribute string examName, list chapterList.
# Create a init method takes all parameters in above sequence.
# Method should set value of attributes to parameters value.
# Implement two method, findMinimumChapterByMarks and sortChapterByPage in Exam class.
# findChapterByMarks, return chapter having minimum value of marks of all chapters in chapterList of Exam class. 
# If chapterList is empty, return none to main program.
# SortChapterByPage, return sorted list of chapter in ascending order of page for chapterList of Exam class. 
# If no chapter found, return none to main. Method should be called for main method. Main program is inline to simple input.
# Create Exam and Chapter object. Create list of n Chapter object. Read value of n.
# Read value of number, page, marks, name, and create Chapter object and add to list up to n times. 
# Create Exam object by passing examName. Call method using Exam object. If none return, print no data found.


# Example Input

# 3
# 101
# 50
# 40
# Arrays
# 102
# 30
# 20
# Strings
# 103
# 70
# 60
# LinkedList
# Python Exam


# Output

# 102
# 30
# 20
# Strings
# 102
# 30
# 20
# Strings
# 101
# 50
# 40
# Arrays
# 103
# 70
# 60
# LinkedList


class Chapter:
    def __init__(self, number, page, marks, name):
        self.number = number
        self.page = page
        self.marks = marks
        self.name = name


class Exam:
    def __init__(self, examName, chapterList):
        self.examName = examName
        self.chapterList = chapterList

    def findMinimumChapterByMarks(self):
        if not self.chapterList:
            return None

        min_chapter = self.chapterList[0]

        for chapter in self.chapterList:
            if chapter.marks < min_chapter.marks:
                min_chapter = chapter

        return min_chapter

    def sortChapterByPage(self):
        if not self.chapterList:
            return None

        return sorted(self.chapterList, key=lambda x: x.page)


n = int(input())

chapterList = []

for i in range(n):
    number = int(input())
    page = int(input())
    marks = int(input())
    name = input()

    chapter = Chapter(number, page, marks, name)
    chapterList.append(chapter)

examName = input()

exam = Exam(examName, chapterList)

minChapter = exam.findMinimumChapterByMarks()

if minChapter is None:
    print("No Data Found")
else:
    print(minChapter.number)
    print(minChapter.page)
    print(minChapter.marks)
    print(minChapter.name)

sortedChapters = exam.sortChapterByPage()

if sortedChapters is None:
    print("No Data Found")
else:
    for chapter in sortedChapters:
        print(chapter.number)
        print(chapter.page)
        print(chapter.marks)
        print(chapter.name)




    


