pipeline {
    agent any
    stages {
        stage("更新代码") {
            steps {
                git credentialsId: '50578efb-1b51-4422-a94a-ccfc9f4592d7', url: 'https://github.com/wxhou/Interface_test_example.git'            
            }
        }
        stage("执行测试") {
            steps {
                sh "pytest --alluredir allure-results --clean-alluredir --junit-xml=allure.xml"
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