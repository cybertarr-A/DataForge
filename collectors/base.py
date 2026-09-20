from abc import ABC, abstractmethod


class Collector(ABC):

    @abstractmethod
    def collect(self, source: str) -> list[dict]:
        raise NotImplementedError