import psycopg2

hostname='localhost'
database='contact_manager'
username='postgres'
pwd='na66248568'
port_id=5648


try:
    conn=psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)
    
    cur=conn.cursor()

    creat_table1='create table if not exists contact(contact_id serial primary key,f_name varchar(20) not null,l_name varchar(20) not null);'
    creat_table2='create table if not exists phone(phone_id serial primary key,contact_id int not null,foreign key (contact_id) references contact(contact_id),number varchar(20) not null);'
    creat_table3='create table if not exists address (address_id serial primary key,contact_id int not null,state varchar (50),city varchar(50),foreign key (contact_id) references contact(contact_id));'
    creat_table4='create table if not exists karbar(user_id serial primary key,username varchar(50) not null,password varchar(100) not null);'
    creat_table5='create table if not exists user_contact(uc_id serial primary key,user_id int not null,contact_id int not null,foreign key(user_id) references karbar(user_id),foreign key (contact_id) references contact(contact_id));'
  
    cur.execute("INSERT INTO karbar ( user_id,username,password ) VALUES ( 2,'javad','hasani' )")
    
    conn.commit()




except Exception as error:
    print(error)
finally:
    conn.close()
    cur.close()

