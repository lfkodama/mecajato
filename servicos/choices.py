from django.db.models import TextChoices

class ChoicesCategoriasManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvula do motor"
    TROCAR_OLEO = "TO", "Troca óleo"
    BALANCEAMENTO = "B", "Balancemanento de rodas"