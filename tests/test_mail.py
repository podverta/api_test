import pytest
from api.models import Mail
import datetime

class TestMailAPI:

    @pytest.mark.django_db(transaction=True)
    def test_mail_not_found(self, client):
        response = client.get('/api/v1/mail/')

        assert response.status_code != 404, 'Страница `/api/v1/mail/` не ' \
                                            'найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_mail_not_auth(self, client):
        response = client.get('/api/v1/mail/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/mail/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_mail_get(self, client, user, mail_1):
        response = client.get('/api/v1/mail/')
        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/mail/` с токеном авторизации возвращаетсся статус 200'

        test_data = response.json()

        assert type(test_data) == list, 'Проверьте, что при GET запросе на `/api/v1/mail/` возвращается список'

        assert len(test_data) == Mail.objects.count(), \
            'Проверьте, что при GET запросе на `/api/v1/mail/` возвращается ' \
            'весь список'

        mails = Mail.objects.all()[0]
        test_mail = test_data[0]
        assert 'id' in test_mail, 'Проверьте, что добавили `id` в список ' \
                                  'полей `fields` сериализатора модели mail'
        assert 'date_start' in test_mail, 'Проверьте, что добавили `text` в список полей `fields` сериализатора модели mail'
        assert 'date_finish' in test_mail, \
            'Проверьте, что добавили `author` в список полей `fields` сериализатора модели mail'
        assert 'tags' in test_mail, \
            'Проверьте, что добавили `pub_date` в список полей `fields` сериализатора модели mail'
        assert 'code_mobile' in test_mail, \
            'Проверьте, что `author` сериализатора модели mail возвращает имя пользователя'

        assert test_mail['id'] == mails.id, \
            'Проверьте, что при GET запросе на `/api/v1/mail/` возвращается весь список статей'

    @pytest.mark.django_db(transaction=True)
    def test_mail_create(self, user, client):
        mail_count = Mail.objects.count()

        data = {}

        response = client.post('/api/v1/mail/', data=data)
        assert response.status_code == 400, \
            'Проверьте, что при POST запросе на `/api/v1/mail/` с не правильными данными возвращается статус 400'

    @pytest.mark.django_db(transaction=True)
    def test_mail_get_current(self, client, mail_1):
        response = client.get(f'/api/v1/mail/{mail_1.id}/')

        assert response.status_code == 200, \
            'Страница `/api/v1/mail/{id}/` не найдена, проверьте этот адрес в *urls.py*'

        test_data = response.json()
        assert test_data.get('code_mobile') == mail_1.code_mobile, \
            'Проверьте, что при GET запросе `/api/v1/mail/{id}/` возвращаете ' \
            'данные сериализатора, ' \
            'не найдено или не правильное значение `code_mobile`'
        assert test_data.get('tags') == mail_1.tags, \
            'Проверьте, что при GET запросе `/api/v1/mail/{id}/` возвращаете данные сериализатора, ' \
            'не найдено или не правильное значение `tags`, должно возвращать имя пользователя '

    @pytest.mark.django_db(transaction=True)
    def test_mail_patch_current(self, client, mail_1):
        response = client.delete(f'/api/v1/mail/{mail_1.id}/')

        assert response.status_code == 204, \
            'Проверьте, что при DELETE запросе `api/v1/mail/{id}/` ' \
            'возвращаете статус 204'



