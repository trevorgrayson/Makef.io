from dataclasses import dataclass, field
from collections import defaultdict
from typing import List

import re

TARGET = re.compile('^[A-Za-z_]*:.*')


class Makefile:
    """ Represents a single Makefile. """

    def __init__(self, **kwargs):
        self.header = kwargs.get('header', [])
        # needs to maintaain order
        self.targets = defaultdict(list)
        self.deps = {}

    def render(self, **kwargs):
        """
        Args:
            kwargs - set any env `VARIABLE?=` you would like to override
        Returns:
            text Makefile doc
        """
        mf = "\n".join(self.header) + "\n"

        for target, body in self.targets.items():
            mf += f"{target}:{self.deps[target]}\n"
            mf += "\n".join(body)

        return mf 

    def __add__(self, other):
        self.deps.update(other.deps)
        self.targets.update(other.targets)
        self.header += other.header

        return self

    @classmethod
    def parse(cls, makefile):
        """
        Args:
            makefile - text buffer
        Returns:
            Makefile
        """
        mk = Makefile()

        present_target = mk.header
        for line in makefile:
            if TARGET.match(line):
                target, deps = line.split(':')
                mk.targets[target] = []
                present_target = mk.targets[target]
                mk.deps[target] = deps
            else:
                present_target.append(line)

        return mk


@dataclass
class Target:
    target_line: str
    body: List[int] = field(default_factory=list)


