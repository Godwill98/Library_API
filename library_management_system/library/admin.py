from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book
from .models import Author
from .models import Member
from .models import Loan
from .models import Librarian


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Librarian)

