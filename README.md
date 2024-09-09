# qa_python
==================================================================================================== 1 failed, 11 passed in 0.14s ===================================================================================================== 
(venv) PS C:\Users\user\qa_python> pytest -v tests.py 
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.12.5, pytest-8.3.2, pluggy-1.5.0 -- C:\Users\user\PycharmProjects\qa_python_1\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\user\qa_python
collected 12 items                                                                                                                                                                                                                      

tests.py::TestBooksCollector::test_add_new_book_add_two_books FAILED                                                                                                                                                             [  8%]
tests.py::TestBooksCollector::test_add_new_book PASSED                                                                                                                                                                           [ 16%] 
tests.py::TestBooksCollector::test_add_existing_book PASSED                                                                                                                                                                      [ 25%] 
tests.py::TestBooksCollector::test_set_book_genre PASSED                                                                                                                                                                         [ 33%] 
tests.py::TestBooksCollector::test_get_books_with_specific_genre PASSED                                                                                                                                                          [ 41%] 
tests.py::TestBooksCollector::test_get_books_for_children PASSED                                                                                                                                                                 [ 50%] 
tests.py::TestBooksCollector::test_add_book_in_favorites PASSED                                                                                                                                                                  [ 58%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites PASSED                                                                                                                                                             [ 66%] 
tests.py::TestBooksCollector::test_adding_books_with_various_genres[\u041a\u043d\u0438\u0433\u0430 1-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED                                                        [ 75%] 
tests.py::TestBooksCollector::test_adding_books_with_various_genres[\u041a\u043d\u0438\u0433\u0430 2-\u0423\u0436\u0430\u0441\u044b] PASSED                                                                                      [ 83%] 
tests.py::TestBooksCollector::test_adding_books_with_various_genres[\u041a\u043d\u0438\u0433\u0430 3-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED                                                              [ 91%] 
tests.py::TestBooksCollector::test_get_books_genre PASSED                                                                                                                                                                        [100%] 