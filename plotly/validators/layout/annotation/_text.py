import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='text', parent_name='layout.annotation', **kwargs
    ):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+arraydraw',
            role='info',
            **kwargs
        )