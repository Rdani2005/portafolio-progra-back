
# -------------- Libraries ---------------------------
from rest_framework.serializers import ModelSerializer
# -------------- own files ---------------------------
from .models import Trabajos
# ------------------ Copyright ----------------------------------
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) Danny Sequeira 2022"
# -------------------- Models --------------------------------
class TrabajosSerializer(ModelSerializer):
    class Meta:
        model = Trabajos
        fields = '__all__'