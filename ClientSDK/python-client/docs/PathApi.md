# swagger_client.PathApi

All URIs are relative to *http://localhost/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_path**](PathApi.md#get_path) | **GET** /id&#x3D;{problem_id}/Path | Path


# **get_path**
> Path get_path(problem_id)

Path

Returns a description of the path from the robot's current location to the goal.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathApi()
problem_id = 56 # int | The id of the problem being manipulated

try: 
    # Path
    api_response = api_instance.get_path(problem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathApi->get_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 

### Return type

[**Path**](Path.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

