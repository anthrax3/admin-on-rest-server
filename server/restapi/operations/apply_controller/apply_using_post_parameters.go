package apply_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"

	strfmt "github.com/go-openapi/strfmt"
	"github.com/roscopecoltran/admin-on-rest-server/server/api"

	"github.com/roscopecoltran/admin-on-rest-server/server/models"
)

// BusinessLogicApplyUsingPOST executes the core logic of the related
// route endpoint.
func BusinessLogicApplyUsingPOST(f func(ctx *gin.Context, params *ApplyUsingPOSTParams) *api.Response) gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// generate params from request
		params := &ApplyUsingPOSTParams{}
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

// ApplyUsingPOSTParams contains all the bound params for the apply using p o s t operation
// typically these are obtained from a http.Request
//
// swagger:parameters applyUsingPOST
type ApplyUsingPOSTParams struct {

	/*apply
	  Required: true
	  In: body
	*/
	Apply *models.Apply
}

// ApplyUsingPOSTParamsFromCtx gets the params struct from the gin context.
func ApplyUsingPOSTParamsFromCtx(ctx *gin.Context) *ApplyUsingPOSTParams {
	params, _ := ctx.Get("params")
	return params.(*ApplyUsingPOSTParams)
}

// BindRequest both binds and validates a request, it assumes that complex things implement a Validatable(strfmt.Registry) error interface
// for simple values it will use straight method calls
func (o *ApplyUsingPOSTParams) bindRequest(ctx *gin.Context) error {
	var res []error
	formats := strfmt.NewFormats()

	if runtime.HasBody(ctx.Request) {
		var body models.Apply
		if err := ctx.BindJSON(&body); err != nil {
			if err == io.EOF {
				res = append(res, errors.Required("apply", "body"))
			} else {
				res = append(res, errors.NewParseError("apply", "body", "", err))
			}

		} else {
			if err := body.Validate(formats); err != nil {
				res = append(res, err)
			}

			if len(res) == 0 {
				o.Apply = &body
			}
		}

	} else {
		res = append(res, errors.Required("apply", "body"))
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

// vim: ft=go
