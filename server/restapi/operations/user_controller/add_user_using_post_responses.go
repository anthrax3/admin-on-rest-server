// Code generated by go-swagger; DO NOT EDIT.

package user_controller

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"net/http"

	"github.com/go-openapi/runtime"

	"github.com/roscopecoltran/admin-on-rest-server/server/models"
)

// AddUserUsingPOSTOKCode is the HTTP code returned for type AddUserUsingPOSTOK
const AddUserUsingPOSTOKCode int = 200

/*AddUserUsingPOSTOK OK

swagger:response addUserUsingPOSTOK
*/
type AddUserUsingPOSTOK struct {

	/*
	  In: Body
	*/
	Payload *models.User `json:"body,omitempty"`
}

// NewAddUserUsingPOSTOK creates AddUserUsingPOSTOK with default headers values
func NewAddUserUsingPOSTOK() *AddUserUsingPOSTOK {
	return &AddUserUsingPOSTOK{}
}

// WithPayload adds the payload to the add user using p o s t o k response
func (o *AddUserUsingPOSTOK) WithPayload(payload *models.User) *AddUserUsingPOSTOK {
	o.Payload = payload
	return o
}

// SetPayload sets the payload to the add user using p o s t o k response
func (o *AddUserUsingPOSTOK) SetPayload(payload *models.User) {
	o.Payload = payload
}

// WriteResponse to the client
func (o *AddUserUsingPOSTOK) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.WriteHeader(200)
	if o.Payload != nil {
		payload := o.Payload
		if err := producer.Produce(rw, payload); err != nil {
			panic(err) // let the recovery middleware deal with this
		}
	}
}

// AddUserUsingPOSTCreatedCode is the HTTP code returned for type AddUserUsingPOSTCreated
const AddUserUsingPOSTCreatedCode int = 201

/*AddUserUsingPOSTCreated Created

swagger:response addUserUsingPOSTCreated
*/
type AddUserUsingPOSTCreated struct {
}

// NewAddUserUsingPOSTCreated creates AddUserUsingPOSTCreated with default headers values
func NewAddUserUsingPOSTCreated() *AddUserUsingPOSTCreated {
	return &AddUserUsingPOSTCreated{}
}

// WriteResponse to the client
func (o *AddUserUsingPOSTCreated) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(201)
}

// AddUserUsingPOSTUnauthorizedCode is the HTTP code returned for type AddUserUsingPOSTUnauthorized
const AddUserUsingPOSTUnauthorizedCode int = 401

/*AddUserUsingPOSTUnauthorized Unauthorized

swagger:response addUserUsingPOSTUnauthorized
*/
type AddUserUsingPOSTUnauthorized struct {
}

// NewAddUserUsingPOSTUnauthorized creates AddUserUsingPOSTUnauthorized with default headers values
func NewAddUserUsingPOSTUnauthorized() *AddUserUsingPOSTUnauthorized {
	return &AddUserUsingPOSTUnauthorized{}
}

// WriteResponse to the client
func (o *AddUserUsingPOSTUnauthorized) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(401)
}

// AddUserUsingPOSTForbiddenCode is the HTTP code returned for type AddUserUsingPOSTForbidden
const AddUserUsingPOSTForbiddenCode int = 403

/*AddUserUsingPOSTForbidden Forbidden

swagger:response addUserUsingPOSTForbidden
*/
type AddUserUsingPOSTForbidden struct {
}

// NewAddUserUsingPOSTForbidden creates AddUserUsingPOSTForbidden with default headers values
func NewAddUserUsingPOSTForbidden() *AddUserUsingPOSTForbidden {
	return &AddUserUsingPOSTForbidden{}
}

// WriteResponse to the client
func (o *AddUserUsingPOSTForbidden) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(403)
}

// AddUserUsingPOSTNotFoundCode is the HTTP code returned for type AddUserUsingPOSTNotFound
const AddUserUsingPOSTNotFoundCode int = 404

/*AddUserUsingPOSTNotFound Not Found

swagger:response addUserUsingPOSTNotFound
*/
type AddUserUsingPOSTNotFound struct {
}

// NewAddUserUsingPOSTNotFound creates AddUserUsingPOSTNotFound with default headers values
func NewAddUserUsingPOSTNotFound() *AddUserUsingPOSTNotFound {
	return &AddUserUsingPOSTNotFound{}
}

// WriteResponse to the client
func (o *AddUserUsingPOSTNotFound) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(404)
}