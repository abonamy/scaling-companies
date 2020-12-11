from rest_framework import serializers

from .models import Company, Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('ca', 'ebitda', 'loss', 'margin', 'year')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    results = ResultSerializer(many=True, read_only=True)  # nested relationship

    class Meta:
        model = Company
        fields = ('id', 'name', 'siren', 'sector', 'results')

    # https://stackoverflow.com/a/52182750
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['sector'] = instance.get_sector_display()
        return ret
