import django
from django.db.models import Count
 
from apps.dojo_ninjas.models import *
from apps.books_authors.models import *

def create_dojo(name, city, state):
    return Dojos.objects.create(name=name, city=city, state=state)

def delete_dojo(name):
    Dojos.objects.get(name=name).delete()


def create_ninja(dojo_name, first_name, last_name):
    dojo = Dojos.objects.get(name=dojo_name)
    return Ninjas.objects.create(dojo=dojo, first_name=first_name, last_name=last_name)


def show_ninjas(dojo_name):
    dojo = Ninjas.objects.filter(dojo__name=dojo_name)
    for ninja in dojo:
        print ninja.first_name, ninja.last_name

def problem_6():
    author = Author.objects.first()
    books = Book.objects.all().order_by('id')[0:2]
    books[0].authors.add(author)
    books[1].authors.add(author)
    print books[0].name, 'author is ' + author.first_name, author.id
    print books[1].name, 'author is ' + author.first_name, author.id

def problem_7():
    author = Author.objects.get(id=2)

    books = Book.objects.all().order_by('id')[0:3]
    books[0].authors.add(author)
    books[1].authors.add(author)
    books[2].authors.add(author)
    
    print books[0].name, 'author is ' + author.first_name, author.id
    print books[1].name, 'author is ' + author.first_name, author.id
    print books[2].name, 'author is ' + author.first_name, author.id

def problem_8():
    author = Author.objects.get(id=3)

    books = Book.objects.all().order_by('id')[0:4]
    books[0].authors.add(author)
    books[1].authors.add(author)
    books[2].authors.add(author)
    books[3].authors.add(author)

    print books[0].name, 'author is ' + author.first_name, author.id
    print books[1].name, 'author is ' + author.first_name, author.id
    print books[2].name, 'author is ' + author.first_name, author.id
    print books[3].name, 'author is ' + author.first_name, author.id

def problem_9():
    author = Author.objects.get(id=4)

    books = Book.objects.all().order_by('id')[0:5]
    books[0].authors.add(author)
    books[1].authors.add(author)
    books[2].authors.add(author)
    books[3].authors.add(author)
    books[4].authors.add(author)

    print books[0].name, 'author is ' + author.first_name, author.id
    print books[1].name, 'author is ' + author.first_name, author.id
    print books[2].name, 'author is ' + author.first_name, author.id
    print books[3].name, 'author is ' + author.first_name, author.id
    print books[4].name, 'author is ' + author.first_name, author.id

def problem_10():
    book3 = Author.objects.filter(books__id=3)
    for book in book3:
        print book.first_name, book.id

def problem_11():
    book = Book.objects.get(id=3)
    author = book.authors.first()
    book.authors.remove(author)

def problem_12():
    book = Book.objects.get(id=2)
    author = Author.objects.get(id=5)
    book.authors.add(author)
    for author in book.authors.all():
        print author.first_name, author.last_name, author.id

def print_all_books():
    for book in Book.objects.all():
        print book.id, book.name

def print_all_authors():
    for author in Author.objects.all():
        print author.id, author.first_name, author.last_name



