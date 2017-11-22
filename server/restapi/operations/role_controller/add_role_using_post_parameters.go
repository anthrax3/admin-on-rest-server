package role_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	"github.com/mikkeloscar/gin-swagger/api"

	strfmt "github.com/go-openapi/strfmt"

	"github.com/roscopecoltran/admin-on-rest-server/server/models"
)

// BusinessLogicAddRoleUsingPOST executes the core logic of the related
// route endpoint.
func BusinessLogicAddRoleUsingPOST(f func(ctx *gin.Context, params *AddRoleUsingPOSTParams) *api.Response) gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// generate params from request
		params := &AddRoleUsingPOSTParams{}
		err := params.bindRequest(ctx)
		if err != nil {
			errObj := err.(*errors.CompositeError)
			problem := api.Problem{
				Title:  "Unprocessable Entity.",
				Status: int(errObj.Code()),
				Detail: errObj.Error(),
			}
			ctx.Writer.Header().Set("Content-Type", "application/problem+json")
			ctx.JSON(problem.Status, problem)
			return
		}

		resp := f(ctx, params)
		switch resp.Code {
		case http.StatusNoContent:
			ctx.AbortWithStatus(resp.Code)
		default:
			ctx.JSON(resp.Code, resp.Body)
		}
	}
}

// AddRoleUsingPOSTParams contains all the bound params for the add role using p o s t operation
// typically these are obtained from a http.Request
//
// swagger:parameters addRoleUsingPOST
type AddRoleUsingPOSTParams struct {

	/*role
	  Required: true
	  In: body
	*/
	Role *models.Role
}

// AddRoleUsingPOSTParamsFromCtx gets the params struct from the gin context.
func AddRoleUsingPOSTParamsFromCtx(ctx *gin.Context) *AddRoleUsingPOSTParams {
	params, _ := ctx.Get("params")
	return params.(*AddRoleUsingPOSTParams)
}

// BindRequest both binds and validates a request, it assumes that complex things implement a Validatable(strfmt.Registry) error interface
// for simple values it will use straight method calls
func (o *AddRoleUsingPOSTParams) bindRequest(ctx *gin.Context) error {
	var res []error
	formats := strfmt.NewFormats()

	if runtime.HasBody(ctx.Request) {
		var body models.Role
		if err := ctx.BindJSON(&body); err != nil {
			if err == io.EOF {
				res = append(res, errors.Required("role", "body"))
			} else {
				res = append(res, errors.NewParseError("role", "body", "", err))
			}

		} else {
			if err := body.Validate(formats); err != nil {
				res = append(res, err)
			}

			if len(res) == 0 {
				o.Role = &body
			}
		}

	} else {
		res = append(res, errors.Required("role", "body"))
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

// vim: ft=go
