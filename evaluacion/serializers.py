
# -------------- Libraries ---------------------------
from rest_framework.serializers import ModelSerializer
# -------------- own files ---------------------------
from .models import Evaluacion
# ------------------ Copyright ----------------------------------
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) Danny Sequeira 2022"
# -------------------- Models --------------------------------
class EvaluacionSerializer(ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'