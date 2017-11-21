// Code generated by go-swagger; DO NOT EDIT.

package schema_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the generate command

import (
	"net/http"

	middleware "github.com/go-openapi/runtime/middleware"
)

// FindOneUsingGET1HandlerFunc turns a function with the right signature into a find one using g e t 1 handler
type FindOneUsingGET1HandlerFunc func(FindOneUsingGET1Params) middleware.Responder

// Handle executing the request and returning a response
func (fn FindOneUsingGET1HandlerFunc) Handle(params FindOneUsingGET1Params) middleware.Responder {
	return fn(params)
}

// FindOneUsingGET1Handler interface for that can handle valid find one using g e t 1 params
type FindOneUsingGET1Handler interface {
	Handle(FindOneUsingGET1Params) middleware.Responder
}

// NewFindOneUsingGET1 creates a new http.Handler for the find one using g e t 1 operation
func NewFindOneUsingGET1(ctx *middleware.Context, handler FindOneUsingGET1Handler) *FindOneUsingGET1 {
	return &FindOneUsingGET1{Context: ctx, Handler: handler}
}

/*FindOneUsingGET1 swagger:route GET /schemas/_entitys/{eid} schema-controller findOneUsingGET1

findOne

*/
type FindOneUsingGET1 struct {
	Context *middleware.Context
	Handler FindOneUsingGET1Handler
}

func (o *FindOneUsingGET1) ServeHTTP(rw http.ResponseWriter, r *http.Request) {
	route, rCtx, _ := o.Context.RouteInfo(r)
	if rCtx != nil {
		r = rCtx
	}
	var Params = NewFindOneUsingGET1Params()

	if err := o.Context.BindValidRequest(r, route, &Params); err != nil { // bind params
		o.Context.Respond(rw, r, route.Produces, route, err)
		return
	}

	res := o.Handler.Handle(Params) // actually handle the request

	o.Context.Respond(rw, r, route.Produces, route, res)

}