// Code generated by go-swagger; DO NOT EDIT.

package data_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the generate command

import (
	"net/http"

	errors "github.com/go-openapi/errors"
	middleware "github.com/go-openapi/runtime/middleware"
	strfmt "github.com/go-openapi/strfmt"
	validate "github.com/go-openapi/validate"
)

// DataMutationUsingDELETEHandlerFunc turns a function with the right signature into a data mutation using d e l e t e handler
type DataMutationUsingDELETEHandlerFunc func(DataMutationUsingDELETEParams) middleware.Responder

// Handle executing the request and returning a response
func (fn DataMutationUsingDELETEHandlerFunc) Handle(params DataMutationUsingDELETEParams) middleware.Responder {
	return fn(params)
}

// DataMutationUsingDELETEHandler interface for that can handle valid data mutation using d e l e t e params
type DataMutationUsingDELETEHandler interface {
	Handle(DataMutationUsingDELETEParams) middleware.Responder
}

// NewDataMutationUsingDELETE creates a new http.Handler for the data mutation using d e l e t e operation
func NewDataMutationUsingDELETE(ctx *middleware.Context, handler DataMutationUsingDELETEHandler) *DataMutationUsingDELETE {
	return &DataMutationUsingDELETE{Context: ctx, Handler: handler}
}

/*DataMutationUsingDELETE swagger:route DELETE /api/{entity}/{id} data-controller dataMutationUsingDELETE

dataMutation

*/
type DataMutationUsingDELETE struct {
	Context *middleware.Context
	Handler DataMutationUsingDELETEHandler
}

func (o *DataMutationUsingDELETE) ServeHTTP(rw http.ResponseWriter, r *http.Request) {
	route, rCtx, _ := o.Context.RouteInfo(r)
	if rCtx != nil {
		r = rCtx
	}
	var Params = NewDataMutationUsingDELETEParams()

	if err := o.Context.BindValidRequest(r, route, &Params); err != nil { // bind params
		o.Context.Respond(rw, r, route.Produces, route, err)
		return
	}

	res := o.Handler.Handle(Params) // actually handle the request

	o.Context.Respond(rw, r, route.Produces, route, res)

}

// DataMutationUsingDELETEOKBody data mutation using d e l e t e o k body
// swagger:model DataMutationUsingDELETEOKBody
type DataMutationUsingDELETEOKBody map[string]interface{}

// Validate validates this data mutation using d e l e t e o k body
func (o DataMutationUsingDELETEOKBody) Validate(formats strfmt.Registry) error {
	var res []error

	if err := validate.Required("dataMutationUsingDELETEOK", "body", o); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}