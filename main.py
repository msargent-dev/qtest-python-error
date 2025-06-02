import os
import swagger_client

API_KEY = os.environ.get('QTEST_API_KEY')


configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = API_KEY
configuration.client_side_validation = False
configuration.verify_ssl = False
api_client = swagger_client.ApiClient(configuration)


swagger_client.TestRunApi(api_client).get_of(108781)
