# File Handling Quiz

### 1. How to print 5 symbols from the file starting from 3d symbol?
* ```file.read(3, 5)```
* ```file.read(2, 8)```
* ```
  file.seek(2)
  file.read(5)
  ```
* ```file.seek(2, 5)```

### 2. Choose all correct statements for the Context Manager
* ```It's an object, that implements __enter__ and __exit__ magic methods```
* ```Context Manager helps automaticaly handle file closing```
* ```The Context Manager is called through the "with open("file.txt") as file:" construction```
* ```If error is raised inside the with statement the file won't be closed```

### 3. Choose the right statement for "r" mode
* ```Opens a file in a binary mode```
* ```Opens a file for a reading and writing```
* ```Opens a file for appending at the end of the file. Crates a new file if it doesn't exist```
* ```Opens a file for reading```

### 4. Choose the right statement for "a" mode
* ```Opens a file in a binary mode```
* ```Opens a file for a reading and writing```
* ```Opens a file for appending at the end of the file. Crates a new file if it doesn't exist```
* ```Opens a file for reading```

### 5. How to close file in Python?
* ```By using close(file) function```
* ```Do nothing, files in Python close authomaticaly```
* ```By using context manager```
* ```By using "file.close()" method```