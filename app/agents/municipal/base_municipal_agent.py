from app.agents.base_agent import BaseAgent

from app.agents.base_agent import BaseAgent

class BaseMunicipalAgent(BaseAgent):
    def __init__(self, name=None):
        super().__init__(name or self.__class__.__name__)