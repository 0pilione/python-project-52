from task_manager.labels.models import Labels
from task_manager.statuses.forms import CreateStatusForm


class CreateLabelForm(CreateStatusForm):
    class Meta:
        model = Labels
        fields = ['name']


class UpdateLabelForm(CreateLabelForm):
    pass
