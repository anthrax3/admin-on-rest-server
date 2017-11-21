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

/*
 * JwtAuthenticationRequest.h
 *
 * 
 */

#ifndef JwtAuthenticationRequest_H_
#define JwtAuthenticationRequest_H_


#include "ModelBase.h"

#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  JwtAuthenticationRequest
    : public ModelBase
{
public:
    JwtAuthenticationRequest();
    virtual ~JwtAuthenticationRequest();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// JwtAuthenticationRequest members

    /// <summary>
    /// 
    /// </summary>
    utility::string_t getPassword() const;
    bool passwordIsSet() const;
    void unsetPassword();
    void setPassword(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getUsername() const;
    bool usernameIsSet() const;
    void unsetUsername();
    void setUsername(utility::string_t value);

protected:
    utility::string_t m_Password;
    bool m_PasswordIsSet;
    utility::string_t m_Username;
    bool m_UsernameIsSet;
};

}
}
}
}

#endif /* JwtAuthenticationRequest_H_ */