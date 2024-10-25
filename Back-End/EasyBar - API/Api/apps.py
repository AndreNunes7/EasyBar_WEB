from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from Api.Models.usuarios_model import Usuarios
        from Api.Models.basic_model import Base
        from Api.Models.receita_model import Receita
        from Api.Models.despesas_model import Despesa
        from Api.Models.pagamentos_model import PagamentoFornecedor
        from Api.Models.mesa_model import Mesa
        from Api.Models.produto_model import Produto
        from Api.Models.logAcao_model import LogAcao
