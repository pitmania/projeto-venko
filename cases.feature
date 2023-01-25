
Feature: Run the file

Scenario: Run the file
        Given I have the sistema.py file
        And I open the terminal where the file is inside
        When I write “python3 sistema.py”
        And I press “Enter” 
        Then the terminal opens up the file showing the login interface.


#Test login inside the file

Scenario: Logging with the wrong credentials
    Given the terminal is running sistema.py
    When I write the wrong login or password
    Then the terminal shows “The username or password is incorrect”

          
Scenario: Logging with the rigt credentials.
    Given the terminal is running sistema.py
    When I write “admin” for username and password
    Then the system shows the message “Login Success”



Feature: Options after “login success”

Scenario: Selecting “Show Interfaces”
    Given I logged in
    When I press “1” for “Show Interfaces”
    Then the system will show the table with all the IPs and connections in your computer

          
Scenario: Selecting “Quit”.
    Given I logged in
    When I press “2” for “Quit”
    Then the system ends the current file

Scenario: Selecting Other option besides the actual two
    Given I logged in
    When I press a key Other than “1” or “2” 
    Then the system shows “Command not accepted” and asking to press one of the options before
