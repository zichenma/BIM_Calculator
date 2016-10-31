
import sqlite3
#Element 25 Create a BMI_database
db = sqlite3.connect('BMI_database.db')
c = db.cursor()
#Element 26 Create a insert function so that the users hit calculate the user's data will be insert into BMI database.
def insert(self):
    db.execute('insert into BMI (weight,feet,inch,gender,age,name,email,comment,BMI_value,Body_status) '
               'values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
               (self.entry_weight.get(),
                self.entry_ft.get(),
                self.entry_in.get(),
                self.gender.get(),
                self.age.get(),
                self.entry_name.get(),
                self.entry_email.get(),
                self.text_comments.get(1.0, 'end'),
                self.calculate_BMI(),
                self.body_status #Element 27. Create a body status feild
                ))
    db.commit()
#Element 28. Create a read function, so each time the users hit calculate button, all the records will show in the console
def read_from_db():
   c.execute('SELECT * FROM BMI')
   for row in c.fetchall():
     print(row)

#Element 25 Create the BMI database
def create_database():
    db.row_factory = sqlite3.Row
    print('Create BMI database')
    db.execute('drop table if exists BMI')
    db.execute('create table BMI ( weight int,feet int,inch int,gender text, age int,'
               'name text, email text, comment text, BMI_value float,Body_status text )')

if __name__ == "__main__": create_database()