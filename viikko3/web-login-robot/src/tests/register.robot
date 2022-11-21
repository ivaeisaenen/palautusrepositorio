*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123  kalle123
    Page Should Contain   Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123  kalle123
    Page Should Contain   too short username

Register With Valid Username And Too Short Password
    Input Credentials  kalle  k  k
    Page Should Contain   too short password

Register With Nonmatching Password And Password Confirmation
    Input Credentials  kalle  kalle123  kalle1234
    Page Should Contain   non matching passwords

Login After Successful Registration
    Input Credentials  kalle  kalle123  kalle123
    Go To Login Page
    Input Text  username  kalle
    Input Password  password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Input Credentials  kalle  kalle123  kalle321
    Go To Login Page
    Input Text  username  kalle
    Input Password  password  kalle123
    Click Button  Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Input Credentials
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Go To Register Page
    Input Text  username  ${username}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password_confirmation}
    Click Button  Register