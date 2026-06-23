import psycopg2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

conn = psycopg2.connect(
    dbname="STUDENT_PREDICTION",        
    user="postgres",          
    password="2007",
    host="localhost",
    port="5432")
query='SELECT number_courses,time_study,"Marks" from STUDENT_DATA'
df=pd.read_sql_query(query,conn)
conn.close()

X=df[['number_courses','time_study']]
Y=df['Marks']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=56)
model=LinearRegression()
model.fit(X_train,Y_train)

test_prediction=model.predict(X_test)
print(mean_absolute_error(Y_test,test_prediction))

new_student_data = pd.DataFrame([[3, 6]], columns=['number_courses', 'time_study'])
predicted_mark = model.predict(new_student_data)
print('Predicted marks:', predicted_mark[0])

