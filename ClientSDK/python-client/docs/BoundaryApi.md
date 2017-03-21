# swagger_client.BoundaryApi

All URIs are relative to *http://localhost/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_boundary**](BoundaryApi.md#get_boundary) | **GET** /id&#x3D;{problem_id}/Boundary | Boundary
[**update_boundary**](BoundaryApi.md#update_boundary) | **PUT** /id&#x3D;{problem_id}/Boundary/ver&#x3D;{version}/ | Update the existing boundary value


# **get_boundary**
> Boundary get_boundary(problem_id)

Boundary

Returns a description of the boundary

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BoundaryApi()
problem_id = 56 # int | The id of the problem being manipulated

try: 
    # Boundary
    api_response = api_instance.get_boundary(problem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BoundaryApi->get_boundary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 

### Return type

[**Boundary**](Boundary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_boundary**
> update_boundary(problem_id, version, boundary)

Update the existing boundary value



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BoundaryApi()
problem_id = 56 # int | The id of the problem being manipulated
version = 56 # int | The version of the obstacle to be updated.
boundary = swagger_client.Boundary() # Boundary | Boundary object that needs to be updated.

try: 
    # Update the existing boundary value
    api_instance.update_boundary(problem_id, version, boundary)
except ApiException as e:
    print("Exception when calling BoundaryApi->update_boundary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **version** | **int**| The version of the obstacle to be updated. | 
 **boundary** | [**Boundary**](Boundary.md)| Boundary object that needs to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

