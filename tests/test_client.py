import pytest
from api.models import Client


class TestClientAPI:
    @pytest.mark.django_db(transaction=True)
    def test_client_not_found(self, client):
        response = client.get('/api/v1/client/')

        assert response.status_code != 404, 'Страница `/api/v1/clients/` не найдена, проверьте этот адрес в *urls.py*'


    @pytest.mark.django_db(transaction=True)
    def test_client_get(self, client):
        response = client.get('/api/v1/client/')
        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/client/` возвращается статус 200'

        test_data = response.json()

        assert type(test_data) == list, 'Проверьте, что при GET запросе на `/api/v1/client/` возвращается список'

        assert len(test_data) == Client.objects.count(), \
            'Проверьте, что при GET запросе на `/api/v1/client/` возвращается весь список'



    @pytest.mark.django_db(transaction=True)
    def test_client_create(self, client, user):
        Client_count = Client.objects.count()

        data = {}
        response = client.post('/api/v1/client/', data=data)
        assert response.status_code == 400, \
            'Проверьте, что при POST запросе на `/api/v1/client/` с не правильными данными возвращается статус 400'

        data = {
             'phone_number':'+79998887766',
             'tags':'just',
             'time_zone' : 'Europe/Amsterdam'
        }
        response = client.post('/api/v1/client/', data=data)
        assert response.status_code == 201, \
             'Проверьте, что при POST запросе на `/api/v1/client/` с правильными данными возвращается статус 201'

        test_data = response.json()

        msg_error = 'Проверьте, что при POST запросе на `/api/v1/client/`возвращается словарь с данными'
        assert type(test_data) == dict, msg_error
        assert test_data.get('code_mobile') == '999', msg_error
        assert test_data.get('time_zone') == data['time_zone'], msg_error

        assert Client_count + 1 == Client.objects.count(), \
            'Проверьте, что при POST запросе на `/api/v1/client/` создается запись'

