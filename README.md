## How to use?

#### First Import Table Class From GulistanDB

```
from gulistandb import Table

# BookLibrary = Table("TableName", *ColumnNames)
# TableName must to be an unique one

BookLibrary = Table("Book Library", "BookId", "BookName", "BookPages")
bL = BookLibrary
```

| Method | Example                                 | Description                                                                                                                          |
| :----- | :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| commit | bL.commit()                             | To initialize your db, a 'Data' folder will be automatically created in your current working directory where all data will be saved. |
| rename | bL.rename("newName")                    | To Rename Your Table                                                                                                                 |
| drop   | bL.drop()                               | To Delete Your Table                                                                                                                 |
| insert | bL.rename("101", "Atomic Habit", "377") | To Insert Data in Table                                                                                                              |
| read   | bL.read(type='dict', default='csv')     | To Read Overview of your Table (Fast)                                                                                                |
| get    | bL.get()                                | To get all data of your Table (Slow)                                                                                                 |

Upcoming...

NOTE: CURRENTLY IT IS ON BETA VERSION
