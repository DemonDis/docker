allure generate logs --clean -o report

cp -r ./report/history ./logs

allure open -p 9999 report&