from flowlauncher import FlowLauncher


class SugarCalc(FlowLauncher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show_history = self.settings.get('show_history')
        self.latest_result_char = self.settings.get('latest_result_char')
        self.number_of_decimals = self.settings.get('number_of_decimals')
        self.rounding_direction = self.settings.get('rounding_direction')
        self.signs_aliases = self.settings.get('signs_aliases')

    def query(self, query='') -> list:
        return [
            {
                'Title': '',
                'SubTitle': '',
                'IcoPath': '',
                'JsonRPCAction': {
                    'method': '',
                    'parameters': ['']
                }
            }
        ]
