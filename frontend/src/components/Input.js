import React from 'react';

const Input = (props) => {

    return (
        <div className="form-group">
            <label htmlFor={props.id}>{props.label}</label>
            <input className="form-control" {...props}/>
        </div>
    );
}

export default Input;
