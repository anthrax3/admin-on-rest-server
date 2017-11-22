package data_source_controller

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

// BusinessLogicEditDataSourceUsingPUT executes the core logic of the related
// route endpoint.
func BusinessLogicEditDataSourceUsingPUT(f func(ctx *gin.Context, params *EditDataSourceUsingPUTParams) *api.Response) gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// generate params from request
		params := &EditDataSourceUsingPUTParams{}
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

// EditDataSourceUsingPUTParams contains all the bound params for the edit data source using p u t operation
// typically these are obtained from a http.Request
//
// swagger:parameters editDataSourceUsingPUT
type EditDataSourceUsingPUTParams struct {

	/*dataSource
	  Required: true
	  In: body
	*/
	DataSource *models.DataSource
	/*id
	  Required: true
	  In: path
	*/
	ID string
}

// EditDataSourceUsingPUTParamsFromCtx gets the params struct from the gin context.
func EditDataSourceUsingPUTParamsFromCtx(ctx *gin.Context) *EditDataSourceUsingPUTParams {
	params, _ := ctx.Get("params")
	return params.(*EditDataSourceUsingPUTParams)
}

// BindRequest both binds and validates a request, it assumes that complex things implement a Validatable(strfmt.Registry) error interface
// for simple values it will use straight method calls
func (o *EditDataSourceUsingPUTParams) bindRequest(ctx *gin.Context) error {
	var res []error
	formats := strfmt.NewFormats()

	if runtime.HasBody(ctx.Request) {
		var body models.DataSource
		if err := ctx.BindJSON(&body); err != nil {
			if err == io.EOF {
				res = append(res, errors.Required("dataSource", "body"))
			} else {
				res = append(res, errors.NewParseError("dataSource", "body", "", err))
			}

		} else {
			if err := body.Validate(formats); err != nil {
				res = append(res, err)
			}

			if len(res) == 0 {
				o.DataSource = &body
			}
		}

	} else {
		res = append(res, errors.Required("dataSource", "body"))
	}

	rID := []string{ctx.Param("id")}
	if err := o.bindID(rID, true, formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (o *EditDataSourceUsingPUTParams) bindID(rawData []string, hasKey bool, formats strfmt.Registry) error {
	var raw string
	if len(rawData) > 0 {
		raw = rawData[len(rawData)-1]
	}

	o.ID = raw

	return nil
}

// vim: ft=go
