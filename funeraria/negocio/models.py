from django.db import models


class servicos(models.Model):
     nome_do_cliente = models.CharField(max_length=100)
     servico = models.CharField(max_length=100)
     valor_cobrado = models.IntegerField()
     pagamento = models.CharField(max_length=100)
     cemiterio = models.CharField(max_length=100)

     def __str__(self):
        return self.nome_do_cliente + ' '+ self.servico + ' ' + str(self.valor_cobrado)