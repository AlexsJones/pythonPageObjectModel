###PythonPageObjectModel

This is a very simple working example of how a page object model works in Python
Primarily for the use of web pages that you want to represent as seperate classes.
This is useful as it lets you group page specific functionality and use mixin's for cross site functionality.


e.g. 

```python
   def test_search(self):
        driver = self.driver
        #Arrange
        google = GooglePage(driver)
        #Act
        google.visit()
        #Assert
        google.verify()
```
