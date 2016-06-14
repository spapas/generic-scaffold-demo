from generic_scaffold import CrudManager
import models

class BookCrudManager(CrudManager):
    model = models.Book
    prefix = 'books'


class AuthorCrudManager(CrudManager):
    model = models.Author
    prefix = 'authors'


class CategoryCrudManager(CrudManager):
    model = models.Category
    prefix = 'categories'
