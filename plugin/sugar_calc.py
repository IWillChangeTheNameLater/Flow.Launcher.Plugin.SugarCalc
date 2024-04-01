from flowlauncher import FlowLauncher


class SugarCalc(FlowLauncher):
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
