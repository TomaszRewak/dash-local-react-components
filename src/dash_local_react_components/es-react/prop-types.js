import{R as ReactPropTypesSecret,c as createCommonjsModule}from"./checkPropTypes-0d3dc276.js";function emptyFunction(){}function emptyFunctionWithReset(){}emptyFunctionWithReset.resetWarningCache=emptyFunction;var factoryWithThrowingShims=function(){function shim(props,propName,componentName,location,propFullName,secret){if(secret!==ReactPropTypesSecret){var err=new Error("Calling PropTypes validators directly is not supported by the `prop-types` package. Use PropTypes.checkPropTypes() to call them. Read more at http://fb.me/use-check-prop-types");throw err.name="Invariant Violation",err}}function getShim(){return shim}shim.isRequired=shim;var ReactPropTypes={array:shim,bool:shim,func:shim,number:shim,object:shim,string:shim,symbol:shim,any:shim,arrayOf:getShim,element:shim,elementType:shim,instanceOf:getShim,node:shim,objectOf:getShim,oneOf:getShim,oneOfType:getShim,shape:getShim,exact:getShim,checkPropTypes:emptyFunctionWithReset,resetWarningCache:emptyFunction};return ReactPropTypes.PropTypes=ReactPropTypes,ReactPropTypes},propTypes=createCommonjsModule((function(module){module.exports=factoryWithThrowingShims()}));const{array:array,bool:bool,func:func,number:number,object:object,string:string,symbol:symbol,any:any,arrayOf:arrayOf,element:element,elementType:elementType,instanceOf:instanceOf,node:node,objectOf:objectOf,oneOf:oneOf,oneOfType:oneOfType,shape:shape,exact:exact,checkPropTypes:checkPropTypes,resetWarningCache:resetWarningCache,PropTypes:PropTypes}=propTypes;export default propTypes;export{PropTypes,any,array,arrayOf,bool,checkPropTypes,element,elementType,exact,func,instanceOf,node,number,object,objectOf,oneOf,oneOfType,resetWarningCache,shape,string,symbol};