class StateService:
    def __init__(self):
        self.supported_states = {
            "CA": {
                "name": "California",
                "tax_rate": 0.08,
                "forms": ["540", "540EZ"]
            },
            "NY": {
                "name": "New York",
                "tax_rate": 0.06,
                "forms": ["IT-201", "IT-150"]
            }
        }

    def get_supported_states(self):
        return {"states": list(self.supported_states.keys())}

    def get_state_requirements(self, state_code: str):
        if state_code not in self.supported_states:
            return {"error": "State not supported"}
        return self.supported_states[state_code]

    def get_tax_rates(self, state_code: str):
        if state_code not in self.supported_states:
            return {"error": "State not supported"}
        return {"tax_rate": self.supported_states[state_code]["tax_rate"]}
