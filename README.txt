Python with Selenium Page Object Model framework project.

Techniques used during the setup:

1. Requirements.txt (for saving all the modules used in the project)
2. Pytest fixtures
3. Chrome Options() and Service() (to pre-configure browser and webdriver behaviour)
4. Yield (to act as tearDown aka post condition)
5. Pytest.ini (for CLI configuration and tests groupings)
6. Allure (for recording and reporting test results outputs)
7. POM (each web page is a separate class which keeps all the corresponding data)
8. Inheritance (to use BaseClass content on each of the child classes)
9. Abstraction (using @absractmethod in base_class to be forced on each child class)
10. Decorators (to use on any test function for recording test execution time)
11. Def __init__ (to indicate required data upon creation an object of the class)
12. Custom WebDriverWait(s)
13. Pytest framework (used for Fixture support and Parameterized testing)
14. List, Tuple, Dict / *Args and **Kwargs (to store and unpack data)
15. Match case statement
16. List comprehension
17. .env file (to hide sensitive data)
18. Protected variables
19. @Properties (for cleaner code)