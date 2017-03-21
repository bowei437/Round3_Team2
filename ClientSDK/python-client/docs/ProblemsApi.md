# swagger_client.ProblemsApi

All URIs are relative to *http://localhost/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_problem**](ProblemsApi.md#add_problem) | **POST** / | Creates a new problem and returns a problemID
[**delete_problem**](ProblemsApi.md#delete_problem) | **DELETE** /id&#x3D;{problem_id}/ver&#x3D;{version}/ | Delete Problem
[**get_problem**](ProblemsApi.md#get_problem) | **GET** /id&#x3D;{problem_id}/ | Problems


# **add_problem**
> int add_problem()

Creates a new problem and returns a problemID



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProblemsApi()

try: 
    # Creates a new problem and returns a problemID
    api_response = api_instance.add_problem()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemsApi->add_problem: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_problem**
> delete_problem(problem_id, version)

Delete Problem

This removes the problem by the given ID

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProblemsApi()
problem_id = 56 # int | The id of the problem being manipulated
version = 56 # int | The version of the obstacle to be updated.

try: 
    # Delete Problem
    api_instance.delete_problem(problem_id, version)
except ApiException as e:
    print("Exception when calling ProblemsApi->delete_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **version** | **int**| The version of the obstacle to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_problem**
> Problem get_problem(problem_id)

Problems

Returns a specific problem 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProblemsApi()
problem_id = 56 # int | The id of the problem being manipulated

try: 
    # Problems
    api_response = api_instance.get_problem(problem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemsApi->get_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 

### Return type

[**Problem**](Problem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

