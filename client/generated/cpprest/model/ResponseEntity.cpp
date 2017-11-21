/**
 * DataHive RESTful APIs
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator 2.2.3.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */



#include "ResponseEntity.h"

namespace io {
namespace swagger {
namespace client {
namespace model {

ResponseEntity::ResponseEntity()
{
    m_BodyIsSet = false;
    m_StatusCode = U("");
    m_StatusCodeIsSet = false;
    m_StatusCodeValue = 0;
    m_StatusCodeValueIsSet = false;
}

ResponseEntity::~ResponseEntity()
{
}

void ResponseEntity::validate()
{
    // TODO: implement validation
}

web::json::value ResponseEntity::toJson() const
{
    web::json::value val = web::json::value::object();

    if(m_BodyIsSet)
    {
        val[U("body")] = ModelBase::toJson(m_Body);
    }
    if(m_StatusCodeIsSet)
    {
        val[U("statusCode")] = ModelBase::toJson(m_StatusCode);
    }
    if(m_StatusCodeValueIsSet)
    {
        val[U("statusCodeValue")] = ModelBase::toJson(m_StatusCodeValue);
    }

    return val;
}

void ResponseEntity::fromJson(web::json::value& val)
{
    if(val.has_field(U("body")))
    {
        if(!val[U("body")].is_null())
        {
            std::shared_ptr<Object> newItem(nullptr);
            newItem->fromJson(val[U("body")]);
            setBody( newItem );
        }
    }
    if(val.has_field(U("statusCode")))
    {
        setStatusCode(ModelBase::stringFromJson(val[U("statusCode")]));
    }
    if(val.has_field(U("statusCodeValue")))
    {
        setStatusCodeValue(ModelBase::int32_tFromJson(val[U("statusCodeValue")]));
    }
}

void ResponseEntity::toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix) const
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix[namePrefix.size() - 1] != U('.'))
    {
        namePrefix += U(".");
    }

    if(m_BodyIsSet)
    {
        if (m_Body.get())
        {
            m_Body->toMultipart(multipart, U("body."));
        }
        
    }
    if(m_StatusCodeIsSet)
    {
        multipart->add(ModelBase::toHttpContent(namePrefix + U("statusCode"), m_StatusCode));
        
    }
    if(m_StatusCodeValueIsSet)
    {
        multipart->add(ModelBase::toHttpContent(namePrefix + U("statusCodeValue"), m_StatusCodeValue));
    }
}

void ResponseEntity::fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix)
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix[namePrefix.size() - 1] != U('.'))
    {
        namePrefix += U(".");
    }

    if(multipart->hasContent(U("body")))
    {
        if(multipart->hasContent(U("body")))
        {
            std::shared_ptr<Object> newItem(nullptr);
            newItem->fromMultiPart(multipart, U("body."));
            setBody( newItem );
        }
    }
    if(multipart->hasContent(U("statusCode")))
    {
        setStatusCode(ModelBase::stringFromHttpContent(multipart->getContent(U("statusCode"))));
    }
    if(multipart->hasContent(U("statusCodeValue")))
    {
        setStatusCodeValue(ModelBase::int32_tFromHttpContent(multipart->getContent(U("statusCodeValue"))));
    }
}

std::shared_ptr<Object> ResponseEntity::getBody() const
{
    return m_Body;
}


void ResponseEntity::setBody(std::shared_ptr<Object> value)
{
    m_Body = value;
    m_BodyIsSet = true;
}
bool ResponseEntity::bodyIsSet() const
{
    return m_BodyIsSet;
}

void ResponseEntity::unsetBody()
{
    m_BodyIsSet = false;
}

utility::string_t ResponseEntity::getStatusCode() const
{
    return m_StatusCode;
}


void ResponseEntity::setStatusCode(utility::string_t value)
{
    m_StatusCode = value;
    m_StatusCodeIsSet = true;
}
bool ResponseEntity::statusCodeIsSet() const
{
    return m_StatusCodeIsSet;
}

void ResponseEntity::unsetStatusCode()
{
    m_StatusCodeIsSet = false;
}

int32_t ResponseEntity::getStatusCodeValue() const
{
    return m_StatusCodeValue;
}


void ResponseEntity::setStatusCodeValue(int32_t value)
{
    m_StatusCodeValue = value;
    m_StatusCodeValueIsSet = true;
}
bool ResponseEntity::statusCodeValueIsSet() const
{
    return m_StatusCodeValueIsSet;
}

void ResponseEntity::unsetStatusCodeValue()
{
    m_StatusCodeValueIsSet = false;
}

}
}
}
}
