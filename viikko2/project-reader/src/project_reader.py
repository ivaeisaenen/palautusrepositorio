from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        """Example content dictionary:
            {'tool':
                {'poetry':
                    {
                        'name': 'web-login-robot',
                        'version': '0.1.0',
                        'description': '',
                        'authors': ['Kalle Ilves <kalle.ilves@helsinki.fi>'],
                        'dependencies': {
                            'python': '^3.6', 'Flask': '^1.1.2'
                            },
                        'dev-dependencies': {
                            'robotframework': '^3.2.2', 'robotframework-seleniumlibrary': '^4.5.0', 'requests': '^2.24.0'
                            }
                    }
                },
            'build-system':
                {'requires': ['poetry-core>=1.0.0'], 'build-backend': 'poetry.core.masonry.api'}
            }
        """
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_dict = tomli.loads(content)
        print(toml_dict)
        name = str(toml_dict['tool']['poetry']['name'])
        description = str(toml_dict['tool']['poetry']['description'])
        dependencies_list = list(toml_dict['tool']['poetry']['dependencies'].keys())
        dev_dependencies_list = list(toml_dict['tool']['poetry']['dev-dependencies'].keys())
        print(name)
        print(description)
        print(dependencies_list)
        print(dev_dependencies_list)
        return Project(name, description, dependencies_list, dev_dependencies_list)
