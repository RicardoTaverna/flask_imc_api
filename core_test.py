import unittest

from api import app
from flask import json

class ApiTests(unittest.TestCase):
    """Classe de testes da API."""

    def setUp(self):
        """Método para realizar setup."""
        self.client = app.test_client()
    
    def test_healthcheck_success(self):
        """Método para testar a saúde da API."""
        response = self.client.get("/healthcheck")

        self.assertEqual(response.status_code, 200)
    
    def test_home_success(self):
        """Método para testar o carregamento da pagina principal."""
        response = self.client.get("/")

        self.assertIn('text/html', response.content_type)

    def test_imc_fail(self):
        """Método para testar o calculo sem parametros ."""
        response = self.client.get("/imc")

        self.assertEqual(response.status_code, 405)
    
    def test_imc_success(self):
        """Método para testar o calculo do IMC com sucesso."""
        peso = 110
        altura = 1.70
        resultado = 38.06

        with app.test_client() as client:
            
            sent = {
                'peso': peso,
                'altura': altura
            }
            response = client.post(
                '/imc',
                data=json.dumps(sent),
                content_type='application/json',
            )

            data = json.loads(response.get_data(as_text=True))
            
            assert response.status_code == 200
            assert data['resultado'] == resultado
