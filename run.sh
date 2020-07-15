source venv/bin/activate

pytest --alluredir allure-results --clean-alluredir

cp config/environment.properties allure-results

allure generate allure-results -c -o allure-report

allure open allure-report