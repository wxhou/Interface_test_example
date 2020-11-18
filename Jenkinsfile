pipeline {
    agent any
    stages {
        stage("更新代码") {
            steps {
                git credentialsId: "6f0f9910-6541-4aaa-abda-b7875e44737b", url: "https://github.com/wxhou/Interface_test_example.git"  
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