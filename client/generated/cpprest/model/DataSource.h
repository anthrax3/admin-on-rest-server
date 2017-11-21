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
 * DataSource.h
 *
 * 
 */

#ifndef DataSource_H_
#define DataSource_H_


#include "ModelBase.h"

#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  DataSource
    : public ModelBase
{
public:
    DataSource();
    virtual ~DataSource();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// DataSource members

    /// <summary>
    /// 
    /// </summary>
    utility::string_t getClusterName() const;
    bool clusterNameIsSet() const;
    void unsetClusterName();
    void setClusterName(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    bool getCurrent() const;
    bool currentIsSet() const;
    void unsetCurrent();
    void setCurrent(bool value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getDbName() const;
    bool dbNameIsSet() const;
    void unsetDbName();
    void setDbName(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getId() const;
    bool idIsSet() const;
    void unsetId();
    void setId(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getIndexName() const;
    bool indexNameIsSet() const;
    void unsetIndexName();
    void setIndexName(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getJdbcUrl() const;
    bool jdbcUrlIsSet() const;
    void unsetJdbcUrl();
    void setJdbcUrl(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getMySqlDbName() const;
    bool mySqlDbNameIsSet() const;
    void unsetMySqlDbName();
    void setMySqlDbName(utility::string_t value);
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
    utility::string_t getType() const;
    bool typeIsSet() const;
    void unsetType();
    void setType(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getUsername() const;
    bool usernameIsSet() const;
    void unsetUsername();
    void setUsername(utility::string_t value);

protected:
    utility::string_t m_ClusterName;
    bool m_ClusterNameIsSet;
    bool m_Current;
    bool m_CurrentIsSet;
    utility::string_t m_DbName;
    bool m_DbNameIsSet;
    utility::string_t m_Id;
    bool m_IdIsSet;
    utility::string_t m_IndexName;
    bool m_IndexNameIsSet;
    utility::string_t m_JdbcUrl;
    bool m_JdbcUrlIsSet;
    utility::string_t m_MySqlDbName;
    bool m_MySqlDbNameIsSet;
    utility::string_t m_Password;
    bool m_PasswordIsSet;
    utility::string_t m_Type;
    bool m_TypeIsSet;
    utility::string_t m_Username;
    bool m_UsernameIsSet;
};

}
}
}
}

#endif /* DataSource_H_ */