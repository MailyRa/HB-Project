from model import db, User, Loan, User_loan, Category_loan, Loan_website  

def create_user(fname, lname, dob, address, credit_score, email, password):

    user = User(fname=fname, lname=lname, dob=dob, address=address, credit_score=credit_score, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user 

def create_loan(loan_name, loan_description, category_loans_id):

    loan = Loan(loan_name=loan_name,
                loan_description=loan_description,
                category_loans_id=category_loans_id)
    
    db.session.add(loan)
    db.session.commit()

    return loan 

def create_category_loan(category_name):

    category_loan = Category_loan(category_name=category_name)

    db.session.add(category_loan)
    db.session.commit()

    return category_loan

def create_loan_website(loan_id, url):

    loan_website = Loan_website(loan_id=loan_id, url=url)

    db.session.add(Loan_website)
    db.session.commit()
    
    return loan_website

def create_user_loan(loan_id, user_id):

    user_loan = User_loan(loan_id=loan_id, user_id=user_id)

    db.session.add(User_loan)
    db.session.commit()

    return user_loan

#Create functions from all the model.py tables TOTAL of 5 functions


def get_user():

     return User.query.all()

def get_loan():

    return Loan.query.all()

def get_category_loan():

    return Category_loan.query.all()

def get_loan_website():

    return Loan_website.query.all()

def get_user_loan():

    return User_loan.query.all()

#Query all the information from all the tables TOTAL of 5 

def get_loan_by_id(loan_id):

    return Loan.query.get(loan_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()

#Query Model "Loan"






