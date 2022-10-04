# dash-local-react-components

A small library that allows for loading react components in Dash applications directly from local project files, without any need for a separate build process.

# Setting up

**1. Install the `dash-local-react-components` python package**

```
pip install dash-local-react-components
```

**2. Put `.js` files containing your react.js components into a subdirectory of your project**

```
my-project
├ main.py
└ public
  ├ common.js
  └ my_component.js
```

**3. Load your component**

```python
from dash import Dash
from dash_local_react_components import load_react_component

app = Dash()

# if the component is exported from the my_component.js module as a default export
MyComponent = load_react_component(app, 'public', 'my_component.js')

# if the component is exported from the my_component.js module as a named export
MyComponent = load_react_component(app, 'public', 'my_component.js', 'MyComponent')
```

**4. Add your component to the layout of your application**

```python
app.layout = html.Div([
    html.H1('My application'),
    MyComponent(id='my-component', text='Hello world')
])
```

# Writing Dash react components

Writing custom react.js components for Dash applications is similar to writing any other react.js components. Nevertheless, there are some differences that worth noting.

An example of a Dash react component may look as follows:

```js
import React from 'react'
import { add } from './common.js';

export default function MyComponent(props) {
    const { setProps, count } = props;

    function onClick() {
        setProps({ count: add(count, 1) });
    }

    return React.createElement('div', {}, [
        React.createElement('div', {}, `count: ${count}`),
        React.createElement('button', { onClick }, 'Increment')
    ]);
}

MyComponent.defaultProps = {
    count: 0
};

```

First, let's address the elephant in the room. As the `dash-local-react-components` package removes the need for any build steps from the development process, it does not support `.jsx` files (which are not natively supported by web browsers). This means that one cannot use the native react notation like `<div>my text</div>`, but rather has to fall back to a little bit more involving syntax: `React.createElement('div', {}, 'my text')` (where the first statement gets compiled into the second during a regular build process). Functionally both expressions are identical, so one can still create fully fledged react components without using the .jsx format, it just requires some getting used to and is not as convenient.

Apart form syntactic differences (imposed not necessarily by the Dash framework, but rather by this library), there are also some behavioral changes. Namely, each component used within a layout of a Dash application is provided with a special `setProps` property. It's a function that can be used to change values of other properties of the current component. It behaves similarly to the `setState` function of class-based components, but instead of modifying the state, it modifies the properties. You can use this function to manage the parts of the state of the component that should be exposed to python callbacks of your Dash application.

# Motivation

The goal of this library is to remove any additional configuration and build steps from the process of creating Dash applications with custom react.js components in order to shorten the development cycle of prototyping small visualizations.

It is not recommended (until you fully know what you are doing) to use this library in bigger scale projects. The `dash-local-react-components` serves raw .js files in an un-minified and un-bundled way, which means that they require more resources in order to be download and executed.

But if you are working on a small project and don't want to worry about npms, gulps, webpacks and grunts at this stage - this library might be something for you. Just run your `main.py` and enjoy your fully interactive application.

# Future improvements

The most inconvenient part of this library is the fact that it does not support .jsx files. It's a limitation of the current implementation, not the general design, though. It would be possible to compile .jsx files into .js files on the fly, when first requested. I did some investigation into it, but did not find any fully-python-based jsx transpilers, so I did not follow through - therefore it is not supported in the current version. But it might be a good thing to revisit in the future.