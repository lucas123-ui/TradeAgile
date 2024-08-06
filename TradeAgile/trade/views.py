from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor
from .forms import ClienteForm, UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Página inicial do site
def home(request):
    return render(request, 'trade/home.html')


# Cadastro de novos clientes
def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo cliente no banco de dados
            return redirect('home')  # Redireciona para a página inicial após salvar
    else:
        form = ClienteForm()  # Cria um novo formulário vazio
    return render(request, 'trade/cadastro_clientes.html', {'form': form})


# Exibe tabelas com dados de clientes, fornecedores, produtos e vendas
def demonstrativo_tabelas(request):
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    return render(request, 'trade/demonstrativo_tabelas.html', {
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })


# Exibe uma galeria de produtos
def galeria_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'trade/galeria_produtos.html', {'produtos': produtos})


# Processa uma venda
def realizar_venda(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')

        cliente = Cliente.objects.get(idcli=cliente_id)
        produto = Produto.objects.get(idprod=produto_id)
        vendedor = Vendedor.objects.first()
        fornecedor = produto.idforn

        valor_venda = produto.valorprod * int(quantidade)  # Calcula o valor total da venda
        venda = Venda.objects.create(
            codivend='12345',  # Código de venda fixo para simplificação
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Data fixa para simplificação
            valorcomissao=valor_venda * vendedor.porcvende / 100
        )

        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        produto.estoque -= int(quantidade)  # Atualiza o estoque do produto
        produto.save()

        return redirect('venda_realizada')  # Redireciona para a página de venda realizada

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'trade/realizar_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
    })


# Página confirmando que a venda foi realizada
def venda_realizada(request):
    return render(request, 'trade/venda_realizada.html')


# Página de login para autenticar usuários
def login_view(request):
    if request.method == "POST":  # enviar dados para o servidor
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Autentica o usuário
                return redirect('home')  # Redireciona para a página inicial após login
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')  # Adiciona erro se autenticação falhar
    else:
        form = AuthenticationForm()  # Cria um novo formulário de autenticação vazio

    return render(request, 'trade/login.html', {'form': form})


# Página de registro de novos usuários
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica o novo usuário
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UserRegisterForm()  # Cria um novo formulário de registro vazio
    return render(request, 'trade/register.html', {'form': form})


# Página inicial protegida por login
@login_required
def home(request):
    return render(request, 'trade/home.html')
