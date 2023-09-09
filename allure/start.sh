allure open -p 9999 report&

cp -r ./report/history ./logs

allure generate logs --clean -o report