from sqlalchemy import create_engine
import string 
import random

S = 6
my_conn = create_engine("mysql://root:@localhost/recommendo_login")

for i in range(1000):
    uname = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    pwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    query = my_conn.execute("INSERT INTO  `recommendo_login`.`user` (`username` ,`password`) \
                  VALUES (", uname, ", ", pwd, "))")
    
