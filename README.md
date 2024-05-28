WIP

This is my first technical assessment test for the position of Junior QA Tester.

This assignment was to create a script for a web browser of my choice to automate the commands below:
  1. Open https://careers.veeam.com/vacancies and maximize the browser window.
  2. Using the jobs filter on the page, count the number of Sales positions in two locations: 
    - USA, Texas, Austin
    - Romania, Bucharest
  3. Count positions by choosing the correct filter settings, pressing search 
  button and counting blocks that represent open positions.
  4. Compare the number of positions with the expected result for each location

The entire code is made in 4 blocks to operate an Edge web browser. They are:
  1. Search for open positions outside USA.
  2. Search for open positions in the USA.
    User enters data and searching is done with the find_element method. There are two blocks for the same job: positions in the US require to indicate a city and state, for the rest of the world it requires only to indicate a country and city.
  3. Count the positions.
    Counting is achieved with len() method. 
  4. Compare the amount of positions found through the code with the expected.
    Comparing is done by giving the percentage of coverage the searchh. 

User can demand to count any open position in the company's departments.
If the program cannot find any open position from the user's input, it will be displayed an exception message:
  "No vacancies in the desired department or location."

The current code is unable to identify items that are not visible at first in the dropdown menus in the jobs filters.
