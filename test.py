# import the necessary packages
import pandas
from sqlalchemy import create_engine

# Create the engine to connect to the inbuilt
# sqllite database
engine = create_engine("sqlite+pysqlite:///:memory:")

# Read data from CSV which will be
# loaded as a dataframe object
data = pandas.read_csv('superstore.csv')

# print the sample of a dataframe
print(data.head())

# Write data into the table in sqllite database
data.to_sql('loan_data', engine)

from sqlalchemy import text

# establish the connection with the engine object
with engine.connect() as conn:
	
	# let's select the column credit_history
	# from the loan data table
	result = conn.execute(text("SELECT Credit_History FROM loan_data"))
	
	# print the result
	for row in result:
		print(row.Credit_History)
