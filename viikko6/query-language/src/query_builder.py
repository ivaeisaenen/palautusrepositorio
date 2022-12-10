from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matchers=None):
        if matchers is None:
            self._matchers = []
        else:
            self._matchers = matchers

    def build(self):
        return And(*self._matchers)

    def playsIn(self, team):
        querybuilder = QueryBuilder(self._matchers + [PlaysIn(*self._matchers, team)])
        return querybuilder

    def hasAtLeast(self, value, attr):
        querybuilder = QueryBuilder(self._matchers + [HasAtLeast(value, attr)])
        return querybuilder

    def hasFewerThan(self, value, attr):
        querybuilder = QueryBuilder(self._matchers + [HasFewerThan(value, attr)])
        return querybuilder