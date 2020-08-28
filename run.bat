call python script\addpth.py

call pytest --alluredir allure-results --clean-alluredir

call COPY config\environment.properties allure-results

call allure generate allure-results -c -o allure-report

call allure open allure-report