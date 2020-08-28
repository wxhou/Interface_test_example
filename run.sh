source venv/bin/activate

python script/addpth.py

pytest --alluredir allure-results --clean-alluredir

cp config/environment.properties allure-results

allure generate allure-results -c -o allure-report

allure open allure-report