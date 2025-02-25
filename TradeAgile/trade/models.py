from django.db import models

# Vendedor: informações do vendedor
class Vendedor(models.Model):
    idvende = models.AutoField(primary_key=True)
    codivende = models.CharField(max_length=10)
    nomevende = models.CharField(max_length=100)
    razasocvende = models.CharField(max_length=100)
    fonevende = models.CharField(max_length=20)
    porcvende = models.FloatField()
    class Meta:
        db_table = 'vendedor'  # chamando a tabela no banco de dados

# Produto: detalhes do produto
class Produto(models.Model):
    idprod = models.AutoField(primary_key=True)
    codiprod = models.CharField(max_length=20)
    descprod = models.CharField(max_length=100)
    valorprod = models.FloatField()
    situprod = models.CharField(max_length=1)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    class Meta:
        db_table = 'produto'  # chamando a tabela no banco de dados

# Fornecedor: informações do fornecedor
class Fornecedor(models.Model):
    idforn = models.AutoField(primary_key=True)
    codiforn = models.CharField(max_length=10)
    nomeforn = models.CharField(max_length=100)
    razasocforn = models.CharField(max_length=100)
    foneforn = models.CharField(max_length=20)
    class Meta:
        db_table = 'fornecedor'  # chamando a tabela no banco de dados

# Cliente: dados do cliente
class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)
    codcli = models.CharField(max_length=10)
    nomecli = models.CharField(max_length=100)
    razasoccli = models.CharField(max_length=100)
    datacli = models.DateField()
    cnpjcli = models.CharField(max_length=20)
    fonecli = models.CharField(max_length=20)
    cidcli = models.CharField(max_length=50)
    estcli = models.CharField(max_length=100)
    class Meta:
        db_table = 'cliente'  # chamando a tabela no banco de dados

# ItensVenda: itens de uma venda
class ItensVenda(models.Model):
    iditvend = models.AutoField(primary_key=True)
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)
    valoritvend = models.FloatField()
    qtditvend = models.IntegerField()
    descitvend = models.FloatField()
    class Meta:
        db_table = 'itensvenda'  # chamando a tabela no banco de dados

# Venda: detalhes da venda
class Venda(models.Model):
    idvend = models.AutoField(primary_key=True)
    codivend = models.CharField(max_length=10)
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    valorvend = models.FloatField()
    descvend = models.FloatField()
    totalvend = models.FloatField()
    datavend = models.DateField()
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'venda'

# ClienteBkp: backup dos clientes
class ClienteBkp(models.Model):
    idcli = models.AutoField(primary_key=True)
    codcli = models.CharField(max_length=10)
    nomecli = models.CharField(max_length=100)
    razasoccli = models.CharField(max_length=100)
    datacli = models.DateField()
    cnpjcli = models.CharField(max_length=20)
    fonecli = models.CharField(max_length=20)
    cidcli = models.CharField(max_length=50)
    estcli = models.CharField(max_length=100)
    class Meta:
        db_table = 'clientesbkp'  # chamando a tabela no banco de dados
