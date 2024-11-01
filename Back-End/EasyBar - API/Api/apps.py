from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from Api.Models.cadastros import Cadastro
        from Api.Models.basic_model import Base
        from Api.Models.receita import Receita
        from Api.Models.despesas import Despesa
        from Api.Models.pagamentos import Pagamento
        from Api.Models.produtos import Produto
        from Api.Models.logEstoque import MovimentacaoEstoque
        from Api.Models.fornecedores import Fornecedor
        from Api.Models.financeiro import Financeiro
        from Api.Models.dashboard import Dashboard
        from Api.Models.relatorio import Relatorio
        
