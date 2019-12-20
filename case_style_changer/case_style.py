class Case(object):
    @staticmethod
    def from_string(case_name):
        if case_name == 'camel_case':
            return CamelCase

    @staticmethod
    def available_list():
        return ['camel_case']


class SpaceSeparated(object):
    pass


class CamelCase(object):
    pass
