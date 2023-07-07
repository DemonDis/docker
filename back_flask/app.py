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
        date_test = json['request']['date']
        result_file_xml = f'--junit-xml=/usr/src/app/logs/{test_name}_{date_test}.xml --strict-markers'
        # result_file_json = '--alluredir=/usr/src/app/logs/logs'
        container = client.containers.run(
            image='test-cucumber',
            command=f'pytest {result_file_xml} ./{test_name}/{test_name}.py',
            volumes={
                '/Users/dimart/tmp_docker/logs': {
                    'bind': '/usr/src/app/logs',
                    'mode': 'rw'
                }
            },
            auto_remove=True,
            detach=True
        )
        output = container.attach(stdout=True, stream=True, logs=True)
        name_container = client.containers.list(all=True)[0].id[:12]
        for line in output:
            print({line})
        container.wait()
        tree = etree.parse(f'/Users/dimart/tmp_docker/logs/{test_name}_{date_test}.xml')
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