"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8. Use Get, which requires primary key.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
all_cars = db.session.query(Brand.name, Model.name)
all_cars.filter(Brand.name == 'Chevrolet', Model.name == 'Corvette').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()


# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()


# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()


# Get all brands with that are either discontinued or founded before 1950.
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 30: ordinal not in range(128)
# Changed to a regular E in the DB, but I need to know how to store data in non-ASCII format.

Brand.query.filter(( Brand.founded < 1950 )| (Brand.discontinued.is_(None)) ).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(db.not_(Model.name.in_(['Chevrolet']) )).all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for each car model from that year using only ONE database query.'''
# Not working yet -- got     "expected - got '%r'" % (column, )
# sqlalchemy.exc.InvalidRequestError: SQL expression, column, or mapped entity expected - got '(u'Mini Cooper', 1964, u'Austin', u'Longbridge, England')'
# could use some hints in debugging

     chosen_year = year

     models = db.session.query(Model.name,
                               Model.year,
                               Brand.name,
                               Brand.headquarters).join(Brand).all()

     for Model.name, Brand.name, Model.year, headquarters in models:
        if Model.year == chosen_year:
            print Model.name, Brand.name, headquarters
        else:
            pass



    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     all_brands = db.session.query(Brand.name, 
                                   Model.name).join(Model).all()

     print all_brands


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

#  An object of class Brand with ID of 1 and Brand name of Ford.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is the link between tables (A and B), and holds both its own primary key and 
# related foreign keys from table A and B. 
# Each association table record will hold one association primary key, a foreign key from table A, and corresponding
# foreign key from table B. 
