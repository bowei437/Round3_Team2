# swagger_client.GoalApi

All URIs are relative to *http://localhost/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_goal**](GoalApi.md#get_goal) | **GET** /id&#x3D;{problem_id}/Goal | Goal Location
[**update_goal**](GoalApi.md#update_goal) | **PUT** /id&#x3D;{problem_id}/Goal/ver&#x3D;{version}/ | Update the existing goal value


# **get_goal**
> Goal get_goal(problem_id)

Goal Location

Returns a description of the goal location. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GoalApi()
problem_id = 56 # int | The id of the problem being manipulated

try: 
    # Goal Location
    api_response = api_instance.get_goal(problem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalApi->get_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 

### Return type

[**Goal**](Goal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal**
> update_goal(problem_id, version, goal)

Update the existing goal value



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GoalApi()
problem_id = 56 # int | The id of the problem being manipulated
version = 56 # int | The version of the obstacle to be updated.
goal = swagger_client.Goal() # Goal | Goal object that needs to be updated.

try: 
    # Update the existing goal value
    api_instance.update_goal(problem_id, version, goal)
except ApiException as e:
    print("Exception when calling GoalApi->update_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **version** | **int**| The version of the obstacle to be updated. | 
 **goal** | [**Goal**](Goal.md)| Goal object that needs to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

