
# -------------- Libraries ---------------------------
from rest_framework.serializers import ModelSerializer
# -------------- own files ---------------------------
from .models import Complementarios
# ------------------ Copyright ----------------------------------
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) Danny Sequeira 2022"
# -------------------- Models --------------------------------
class ComplementariosSerializer(ModelSerializer):
    class Meta:
        model = Complementarios
        fields = '__all__'