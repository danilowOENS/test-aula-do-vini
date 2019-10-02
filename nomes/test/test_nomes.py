from rest_framework.test import APITestCase
from rest_framework import status
from nomes.models import Nome


class NomesTests(APITestCase):
    def setUp(self):
        Nome.objects.create(nome='vinicius')
        Nome.objects.create(nome='Groger')
        Nome.objects.create(nome='Lucas')

    def test_get_list(self):
        url = '/nomes/'
        resposta = self.client.get(url, format= 'json')
        self.assertEqual(len(resposta.data), 3)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)

    def test_create_name(self):
        url ='/nomes/'
        dados = {'nome': 'Xablau'}
        resposta = self.client.post(url, dados, format='json')
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Nome.objects.get(nome=dados['nome']).nome, 'Xablau')