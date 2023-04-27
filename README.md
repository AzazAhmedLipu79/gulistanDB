## Welcome To GulistanDB 👋

GulistanDB is a simple Python-based local database for small-scale projects. With GulistanDB, users can create, drop, and rename tables, insert records, and read data without needing knowledge of SQL. The package automatically creates a 'data' folder within the current working directory to store the CSV files. Created with beginners in mind, GulistanDB is easy to use and perfect for those who want to manage their data without dealing with complex databases.

Gulistandb is a Python package that simplifies file interaction for small-scale projects where using SQL or NoSQL databases is too time-consuming. It allows users to create, read, insert, and delete data in CSV or JSON files, which are stored in a Data folder in the current working directory. Gulistandb is not a database, but it tries to behave like one.

This Python library that lets you create local databases using CSV or JSON files. It is designed for small-scale projects that do not require complex queries or operations. You can use it to store any kind of data, such as user information, product details, inventory records, etc. GulistanDB is also ideal for beginners who want to learn how to work with data in Python without having to install or configure anything. All you need is to import the Table class from gulistandb and start creating your tables. GulistanDB will automatically create a ‘data’ folder in your current working directory and save your data there. You can then perform basic operations such as inserting, reading, deleting, and renaming your tables. GulistanDB is not a full-fledged database, but it tries to behave like one. It is a simple and convenient solution for your data needs.

It is a simple Python-based local database for small-scale projects. With GulistanDB, users can create, drop, and rename tables, insert records, and read data without needing knowledge of SQL. The package automatically creates a 'data' folder within the current working directory to store the CSV files. Created with beginners in mind, GulistanDB is easy to use and perfect for those who want to manage their data without dealing with complex databases.

GulistanDB can be used for:

- Developing and testing applications that require a local database without installing SQL Server or other complex databases
- Storing and managing data for small-scale projects that do not need high performance or scalability
- Learning and experimenting with database concepts and operations using CSV or JSON files
- Creating and manipulating data tables with simple Python commands and syntax
- Migrating data from CSV or JSON files to Azure SQL Database or other cloud databases easily
- Storing and retrieving configuration settings for your application
- Saving and loading user preferences and profiles
- Logging and analyzing data from sensors or devices
- Creating and updating inventory lists or product catalogs
- Generating and exporting reports or charts

- Data analysis and visualization
- Web scraping and crawling
- Machine learning and AI
- Testing and debugging

Are you looking for a simple and fast way to store and manage your data in Python? Do you want to avoid the hassle of setting up and learning SQL or other databases? If so, you might be interested in GulistanDB, a Python package that lets you create local databases using CSV or JSON files. GulistanDB is designed for small-scale projects that do not require complex queries or operations. You can use it to store any kind of data, such as user information, product details, inventory records, etc. GulistanDB is also ideal for beginners who want to learn how to work with data in Python without having to install or configure anything. All you need is to import the Table class from gulistandb and start creating your tables. GulistanDB will automatically create a 'data' folder in your current working directory and save your data there. You can then perform basic operations such as inserting, reading, deleting, and renaming your tables. GulistanDB is not a full-fledged database, but it tries to behave like one. It is a simple and convenient solution for your data needs. To learn more about GulistanDB and how to use it, please visit azazahmedlipu79.github.io/gulistanDB/.

## How to INSTALL

Install GulistanDB

```python
  pip install gulistandb
```

## Usage/Examples

```python
from gulistandb import Table


Book_Library = Table('Book_Library_NY', 'BookName','ISBN','BookPAGES', fileType='json')



```

| Method | Example                                      | Description                                                 |
| ------ | -------------------------------------------- | ----------------------------------------------------------- |
| rename | xyzDB.rename(NewfileName, fileType=Optional) | Rename the table to a new name and/or a new file type       |
| drop   | xyzDB.drop()                                 | Deletes the file containing the table data, if it exists    |
| read   | xyzDB.read(OutputFormat:optional='dict')     | Read the table data from the file and return it as a string |
| get    | xyzDB.get()                                  | Same As Read But Slow and Manual Process                    |
| insert | xyzDB.insert(datas)                          | Inserts new data into the table file                        |
| clear  | xyzDB.clear()                                | To clear table file's Data                                  |
| UPDATE | \_\_\_                                       | Coming Soon                                                 |
| DELETE | \_\_\_                                       | Coming Soon                                                 |

## License

[MIT](/License)

## Screenshots

![App Screenshot](https://i.ibb.co/n7mPbNh/gdb.png)

## Support

For support, email lipuahmedazaz79@gmail.com.
