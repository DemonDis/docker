from flask import Flask, request
from flask_cors import CORS
import docker
from lxml import etree

app = Flask(__name__)
CORS(app)

client = docker.client.from_env()

@app.route("/", methods=['POST'])
def rest_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        test_name = json['request']['name']
        format = json['request']['format']
        # result_file = '--junit-xml=/usr/src/app/logs/logs/result.xml --strict-markers --alluredir=/usr/src/app/logs/logs'
        # result_file = ''
        container = client.containers.run(
            image='test-cucumber',
            command=f'pytest ./{test_name}/{test_name}.py',
            volumes={
                '/Users/dimart/tmp_docker': {
                    'bind': '/usr/src/app/logs',
                    'mode': 'rw'
                }
            },
            detach=True
        )
        output = container.attach(stdout=True, stream=True, logs=True)
        name_container = client.containers.list(all=True)[0].id[:12]
        for line in output:
            print({line})
        container.wait()
        tree = etree.parse('/Users/dimart/tmp_docker/logs/result.xml')
        xml_hostname = tree.xpath('//testsuites/testsuite/@hostname')
        return {
        'request': {
            'name': test_name,
            'hostname' : xml_hostname[0],
            'format': format,
            'container': f'{name_container}'
        },
        'request_type': 'auto_test'
    }
    else:
        return 'Content-Type not supported'

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3030)