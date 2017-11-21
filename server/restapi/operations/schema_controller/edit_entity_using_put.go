// Code generated by go-swagger; DO NOT EDIT.

package schema_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the generate command

import (
	"net/http"

	middleware "github.com/go-openapi/runtime/middleware"
)

// EditEntityUsingPUTHandlerFunc turns a function with the right signature into a edit entity using p u t handler
type EditEntityUsingPUTHandlerFunc func(EditEntityUsingPUTParams) middleware.Responder

// Handle executing the request and returning a response
func (fn EditEntityUsingPUTHandlerFunc) Handle(params EditEntityUsingPUTParams) middleware.Responder {
	return fn(params)
}

// EditEntityUsingPUTHandler interface for that can handle valid edit entity using p u t params
type EditEntityUsingPUTHandler interface {
	Handle(EditEntityUsingPUTParams) middleware.Responder
}

// NewEditEntityUsingPUT creates a new http.Handler for the edit entity using p u t operation
func NewEditEntityUsingPUT(ctx *middleware.Context, handler EditEntityUsingPUTHandler) *EditEntityUsingPUT {
	return &EditEntityUsingPUT{Context: ctx, Handler: handler}
}

/*EditEntityUsingPUT swagger:route PUT /schemas/_entitys/put/{id} schema-controller editEntityUsingPUT

editEntity

*/
type EditEntityUsingPUT struct {
	Context *middleware.Context
	Handler EditEntityUsingPUTHandler
}

func (o *EditEntityUsingPUT) ServeHTTP(rw http.ResponseWriter, r *http.Request) {
	route, rCtx, _ := o.Context.RouteInfo(r)
	if rCtx != nil {
		r = rCtx
	}
	var Params = NewEditEntityUsingPUTParams()

	if err := o.Context.BindValidRequest(r, route, &Params); err != nil { // bind params
		o.Context.Respond(rw, r, route.Produces, route, err)
		return
	}

	res := o.Handler.Handle(Params) // actually handle the request

	o.Context.Respond(rw, r, route.Produces, route, res)

}