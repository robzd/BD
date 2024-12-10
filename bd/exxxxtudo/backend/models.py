from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.nome} - {self.telefone}'
    
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100) 
    bairro = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) # UM CLIENTE PODE TER VÁRIOS ENDEREÇOS E
                                                                   # CADA ENDEREÇO É DE UM SÓ CLIENTE
    def __str__(self):
        return f'{self.rua} - {self.bairro} - {self.cliente.nome}'
    

class Perfil(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE) # UM CLIENTE SÓ TEM UM PERFIL E                 
    data_nascimento = models.DateField()                              # CADA PERFIL É DE UM SÓ CLIENTE
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.cliente.nome} - {self.cpf} - {self.data_nascimento}'


class Servico(models.Model):        
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_evento = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('pendente', 'Pendente'), ('concluido', 'Concluído'), ('cancelado', 'Cancelado')])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_servico = models.ForeignKey('TipoServico', on_delete=models.CASCADE, default=None, blank=True, null=True)
    

    def __str__(self):
        return self.descricao + ' - ' + str(self.preco) + ' - ' + str(self.data_evento) + ' - ' + self.status + ' - ' + str(self.cliente) + ' - ' + str(self.tipo_servico)


class TipoServico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome + ' - ' + self.descricao        
    


# class Item (models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.CharField(max_length=100)
#     preco = models.DecimalField(max_digits=8, decimal_places=2)
#     estoque = models.IntegerField()
    
#     def __str__(self):
#         return f'{self.nome} - {self.descricao} - R$ {self.preco} - Estoque: {self.estoque}'


# class Pedido(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
#     itens = models.ManyToManyField(Item)
#     data_pedido = models.DateTimeField(auto_now_add=True)
#     data_entrega = models.DateTimeField()
    
#     def __str__(self): 
#         return f'{self.cliente} - Data do Pedido: {self.data_pedido}'

