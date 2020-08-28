pipeline {
    agent any
    stages {
        stage("更新代码") {
            steps {
                git credentialsId: "dbb5483f-ef6f-43c6-bed7-cf89859170b3", url: "https://github.com/wxhou/Interface_test_example.git"  
            }
        }
        stage("添加环境变量") {
            steps {
                sh "python3 script/addpth.py"
            }
        }
        stage("执行测试") {
            steps {
                sh "python3 -m pytest --alluredir allure-results --clean-alluredir --junit-xml=allure.xml"
            }
        }
    }
    post {
        always {
            script {
                junit 'allure.xml'                
            }
        }
    }
}