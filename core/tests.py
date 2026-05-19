from django.test import TestCase, Client
from .models import TaskModel

class criarTarefaTest(TestCase):
    def test_criar_tarefa(self):
        c = Client()
        response = c.post("/core/adicionar/", {"nome": "realizar testes de integraçao"})
        self.assertEqual(TaskModel.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/core/home/")

class ListarTarefaTest(TestCase):
    def test_listar_tarefa(self):
        c = Client()
        c.post("/core/adicionar/", {"nome": "realizar testes de integraçao"})
        response = c.get("/core/home/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(TaskModel.objects.get(nome="realizar testes de integraçao"), response.context["dados"])

class EditarTarefaTest(TestCase):
    def test_editar_tarefa(self):
        c = Client()
        c.post("/core/adicionar/", {"nome": "realizar testes de integraçao"})
        task = TaskModel.objects.get(nome="realizar testes de integraçao")
        response = c.post(f"/core/editar/{task.pk}/", {"nome": "editando teste"})
        task = TaskModel.objects.get(nome="editando teste")
        self.assertRedirects(response, "/core/home/")
        self.assertEqual(task.nome, "editando teste")



class DeletarTarefaTest(TestCase):
    def test_deletar_tarefa(self):
        c = Client()
        response = c.post("/core/adicionar/", {"nome": "realizar testes de integraçao"})
        task = TaskModel.objects.get(nome="realizar testes de integraçao")
        c.get(f"/core/apagar/{task.pk}/")
        self.assertRedirects(response, "/core/home/")
        self.assertEqual(TaskModel.objects.count(), 0)