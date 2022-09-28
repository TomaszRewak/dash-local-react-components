from dash import Dash
from dash.development.base_component import Component
from urllib import parse
from flask import send_from_directory
import uuid

react_import_url = 'https://unpkg.com/es-react@16.13.1'

_import_file_name = '/__local_react_components_import__.js'
_import_namespace = '__local_react_components__'

_initialized_apps = set()
_initialized_libraries = set()
_initialized_components = dict()


def _change_function_name(func):
    def wrapper(**kwargs):
        return func(**kwargs)
    wrapper.__name__ = func.__name__ + uuid.uuid4().hex
    return wrapper


def _generate_component_import_file(public_path, file_path, export_name, component_name):
    return f'''
        import {{{export_name} as {component_name}}} from "./{public_path}/{file_path}";
        {_import_namespace}["{component_name}"] = {component_name}
    '''


def _generate_import_file(app):
    header = f'''
        const {_import_namespace} = {{}};
    '''

    footer = f'''
        window.{_import_namespace} = {_import_namespace};

        if (window.__start_dash_app__)
            window.__start_dash_app__();
    '''

    component_imports = [
        _generate_component_import_file(public_path, file_path, export_name, component.unique_name)
        for (component_app, public_path, file_path, export_name), component in _initialized_components.items()
        if component_app is app
    ]

    return header + '\n'.join(component_imports) + footer


def _initialize_app(app: Dash):
    app.renderer = f'''
        window.__start_dash_app__ = () => new DashRenderer();

        if (window.{_import_namespace})
            window.__start_dash_app__();
    '''

    app.config.external_scripts += [f'''
        "></script>
        <script type="importmap">{{ "imports": {{ "react": "{react_import_url}" }} }}</script>
        <script src="
    ''']

    @app.server.route(_import_file_name)
    def get_import_file():
        return app.server.response_class(
            response=_generate_import_file(app),
            status=200,
            mimetype='application/javascript')

    app.config.external_scripts += [{'src': _import_file_name, 'type': 'module', 'async':'false', 'defer':'false'}]


def _initialize_library(app: Dash, public_path: str):
    public_path_template = parse.urljoin(f'/{public_path}/', '<path:path>')

    @app.server.route(public_path_template)
    @_change_function_name
    def get_public_files(path):
        return send_from_directory(
            public_path,
            path,
            mimetype='application/javascript' if path.endswith('.js') else None)


def _create_component():
    class LocalReactComponent(Component):
        unique_name = 'c' + uuid.uuid4().hex

        def __init__(self, **kwargs):
            self._prop_names = kwargs.keys()
            self._type = LocalReactComponent.unique_name
            self._namespace = _import_namespace
            self._valid_wildcard_attributes = []

            super(LocalReactComponent, self).__init__(**kwargs)

    return LocalReactComponent


def load(app: Dash, public_path: str, file_path: str, export_name: str = 'default'):
    app_key = app
    library_key = (app, public_path)
    component_key = (app, public_path, file_path, export_name)

    if app_key not in _initialized_apps:
        _initialize_app(app)
        _initialized_apps.add(app_key)

    if library_key not in _initialized_libraries:
        _initialize_library(app, public_path)
        _initialized_libraries.add(library_key)

    if component_key not in _initialized_components:
        component = _create_component()
        _initialized_components[component_key] = component

    return _initialized_components[component_key]
