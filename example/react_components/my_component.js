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
