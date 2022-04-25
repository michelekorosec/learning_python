#Book Database

##Purpose

This Database should serve as a tracking systems for the books I have read throughout the years.
I want to keep track of different book and author characteristics by creating author and book objects with specific attributes.
The books I have read will then be organized in a Pandas DataFrame and plots on the gathered data shall be created.
Ideally I will find a way to sync this Python database with an existing Microsoft Excel sheet containing data from the years 2020 - 2022.

##Plan of Action

- Create an Author Class
    - Attributes: Name, Nationality, Gender
- Create a Book Class
    - Attributes: Title, Author (author class!), Type (audio/physical → child classes), Source (Library, bought, etc), Owned (y/n), Date Started, Date Finished, Series (y/n), Genre, Publication Year, Rating, # of times read, Reading Language
    - Audio Child Class
        - Attributes: Audio length
    - Physical Child Class
        - Attributes: Pages, Format (Paperback/Hardback/ebook)
- Create a Pandas DataFrame
- Create Plots
- FunctionI/Interface to add new books
- Find a way to transfer books from or into Excel file