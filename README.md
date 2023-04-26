## Welcome To GulistanDB 👋

GulistanDB is a simple Python-based local database for small-scale projects. With GulistanDB, users can create, drop, and rename tables, insert records, and read data without needing knowledge of SQL. The package automatically creates a 'data' folder within the current working directory to store the CSV files. Created with beginners in mind, GulistanDB is easy to use and perfect for those who want to manage their data without dealing with complex databases.

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
| UPDATE | _\__                                         | Coming Soon                                                 |
| DELETE | _\__                                         | Coming Soon                                                 |

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Screenshots

![App Screenshot](https://i.ibb.co/rkBtqXy/gddb.png)

## Support

For support, email lipuahmedazaz79@gmail.com.
