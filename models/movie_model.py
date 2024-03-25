# # create python class that will be a SQL table; same as ddl.sql think: rules of the tables

# from app import db


# class MovieModel(db.Model): #sqlalchemy model class; think instructions for a lego castle 

#     __tablename__ = "movie" 

    
#     director = db.Column(db.Integer, foreign_key=True) #define what data type
#     title = db.Column(db.String(50), nullable = False, unique = True) #string is varchar; setting constraints
#     description = db.Column(db.String(50), nullable = True, unique = True)
#     year = db.Column(db.Integer, nullable = False) # we dont have access to the encryption key
    

# # will also have methods (think: dml, commands)

#     def save_movie(self): 
#         db.session.add(self)
#         db.session.commit()

#     def del_movie(self):
#         db.session.delete(self)
#         db.session.commit()

 
