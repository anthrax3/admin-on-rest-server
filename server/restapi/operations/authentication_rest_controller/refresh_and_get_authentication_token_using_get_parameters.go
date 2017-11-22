package authentication_rest_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/go-openapi/errors"
	"github.com/mikkeloscar/gin-swagger/api"
)

// BusinessLogicRefreshAndGetAuthenticationTokenUsingGET executes the core logic of the related
// route endpoint.
func BusinessLogicRefreshAndGetAuthenticationTokenUsingGET(f func(ctx *gin.Context) *api.Response) gin.HandlerFunc {
	return func(ctx *gin.Context) {

		resp := f(ctx)
		switch resp.Code {
		case http.StatusNoContent:
			ctx.AbortWithStatus(resp.Code)
		default:
			ctx.JSON(resp.Code, resp.Body)
		}
	}
}

// RefreshAndGetAuthenticationTokenUsingGETParams contains all the bound params for the refresh and get authentication token using g e t operation
// typically these are obtained from a http.Request
//
// swagger:parameters refreshAndGetAuthenticationTokenUsingGET
type RefreshAndGetAuthenticationTokenUsingGETParams struct {
}

// BindRequest both binds and validates a request, it assumes that complex things implement a Validatable(strfmt.Registry) error interface
// for simple values it will use straight method calls
func (o *RefreshAndGetAuthenticationTokenUsingGETParams) bindRequest(ctx *gin.Context) error {
	var res []error

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

// vim: ft=go
