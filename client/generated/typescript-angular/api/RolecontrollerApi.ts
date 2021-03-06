/**
 * DataHive RESTful APIs
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

import * as models from '../model/models';

/* tslint:disable:no-unused-variable member-ordering */

export class RolecontrollerApi {
    protected basePath = 'https://localhost:8080';
    public defaultHeaders : any = {};

    static $inject: string[] = ['$http', '$httpParamSerializer', 'basePath'];

    constructor(protected $http: ng.IHttpService, protected $httpParamSerializer?: (d: any) => any, basePath?: string) {
        if (basePath !== undefined) {
            this.basePath = basePath;
        }
    }

    /**
     * 
     * @summary addRole
     * @param role role
     */
    public addRoleUsingPOST (role: models.Role, extraHttpRequestParams?: any ) : ng.IHttpPromise<models.Role> {
        const localVarPath = this.basePath + '/role/_roles';

        let queryParameters: any = {};
        let headerParams: any = (<any>Object).assign({}, this.defaultHeaders);
        // verify required parameter 'role' is not null or undefined
        if (role === null || role === undefined) {
            throw new Error('Required parameter role was null or undefined when calling addRoleUsingPOST.');
        }
        let httpRequestParams: ng.IRequestConfig = {
            method: 'POST',
            url: localVarPath,
            data: role,
                        params: queryParameters,
            headers: headerParams
        };

        if (extraHttpRequestParams) {
            httpRequestParams = (<any>Object).assign(httpRequestParams, extraHttpRequestParams);
        }

        return this.$http(httpRequestParams);
    }
    /**
     * 
     * @summary editRole
     * @param id id
     * @param role role
     */
    public editRoleUsingPUT (id: string, role: models.Role, extraHttpRequestParams?: any ) : ng.IHttpPromise<models.Role> {
        const localVarPath = this.basePath + '/role/_roles/put/{id}'
            .replace('{' + 'id' + '}', String(id));

        let queryParameters: any = {};
        let headerParams: any = (<any>Object).assign({}, this.defaultHeaders);
        // verify required parameter 'id' is not null or undefined
        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling editRoleUsingPUT.');
        }
        // verify required parameter 'role' is not null or undefined
        if (role === null || role === undefined) {
            throw new Error('Required parameter role was null or undefined when calling editRoleUsingPUT.');
        }
        let httpRequestParams: ng.IRequestConfig = {
            method: 'PUT',
            url: localVarPath,
            data: role,
                        params: queryParameters,
            headers: headerParams
        };

        if (extraHttpRequestParams) {
            httpRequestParams = (<any>Object).assign(httpRequestParams, extraHttpRequestParams);
        }

        return this.$http(httpRequestParams);
    }
    /**
     * 
     * @summary findRole
     * @param roleId roleId
     */
    public findRoleUsingGET1 (roleId: string, extraHttpRequestParams?: any ) : ng.IHttpPromise<models.Role> {
        const localVarPath = this.basePath + '/role/_roles/{roleId}'
            .replace('{' + 'roleId' + '}', String(roleId));

        let queryParameters: any = {};
        let headerParams: any = (<any>Object).assign({}, this.defaultHeaders);
        // verify required parameter 'roleId' is not null or undefined
        if (roleId === null || roleId === undefined) {
            throw new Error('Required parameter roleId was null or undefined when calling findRoleUsingGET1.');
        }
        let httpRequestParams: ng.IRequestConfig = {
            method: 'GET',
            url: localVarPath,
                                    params: queryParameters,
            headers: headerParams
        };

        if (extraHttpRequestParams) {
            httpRequestParams = (<any>Object).assign(httpRequestParams, extraHttpRequestParams);
        }

        return this.$http(httpRequestParams);
    }
    /**
     * 
     * @summary list
     */
    public listUsingGET2 (extraHttpRequestParams?: any ) : ng.IHttpPromise<Array<models.Role>> {
        const localVarPath = this.basePath + '/role/_roles';

        let queryParameters: any = {};
        let headerParams: any = (<any>Object).assign({}, this.defaultHeaders);
        let httpRequestParams: ng.IRequestConfig = {
            method: 'GET',
            url: localVarPath,
                                    params: queryParameters,
            headers: headerParams
        };

        if (extraHttpRequestParams) {
            httpRequestParams = (<any>Object).assign(httpRequestParams, extraHttpRequestParams);
        }

        return this.$http(httpRequestParams);
    }
}
