# swagger_client.RobotApi

All URIs are relative to *http://localhost/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_robot**](RobotApi.md#add_robot) | **POST** /id&#x3D;{problem_id}/Robot/ver&#x3D;{version}/ | Add a new robot to the list
[**delete_robot**](RobotApi.md#delete_robot) | **DELETE** /id&#x3D;{problem_id}/Robot/rid&#x3D;{robot_id}/ver&#x3D;{version}/ | Delete Robot
[**get_robot**](RobotApi.md#get_robot) | **GET** /id&#x3D;{problem_id}/Robot/rid&#x3D;{robot_id} | Get a robot by the ID
[**get_robots**](RobotApi.md#get_robots) | **GET** /id&#x3D;{problem_id}/Robot | Robot
[**update_robot**](RobotApi.md#update_robot) | **PUT** /id&#x3D;{problem_id}/Robot/rid&#x3D;{robot_id}/ver&#x3D;{version}/ | Update the existing robot value


# **add_robot**
> int add_robot(problem_id, version, robot)

Add a new robot to the list



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
problem_id = 56 # int | The id of the problem being manipulated
version = 56 # int | The version of the obstacle to be updated.
robot = swagger_client.Robot() # Robot | Obstacle object that needs to be added to the list.

try: 
    # Add a new robot to the list
    api_response = api_instance.add_robot(problem_id, version, robot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->add_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **version** | **int**| The version of the obstacle to be updated. | 
 **robot** | [**Robot**](Robot.md)| Obstacle object that needs to be added to the list. | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_robot**
> delete_robot(problem_id, robot_id, version)

Delete Robot

This removes the robot by the given ID

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
problem_id = 56 # int | The id of the problem being manipulated
robot_id = 56 # int | The ID of the Obstacle that needs to be deleted.
version = 56 # int | The version of the obstacle to be updated.

try: 
    # Delete Robot
    api_instance.delete_robot(problem_id, robot_id, version)
except ApiException as e:
    print("Exception when calling RobotApi->delete_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **robot_id** | **int**| The ID of the Obstacle that needs to be deleted. | 
 **version** | **int**| The version of the obstacle to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_robot**
> Robot get_robot(problem_id, robot_id)

Get a robot by the ID



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
problem_id = 56 # int | The id of the problem being manipulated
robot_id = 56 # int | Robot object that needs to be updated.

try: 
    # Get a robot by the ID
    api_response = api_instance.get_robot(problem_id, robot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **robot_id** | **int**| Robot object that needs to be updated. | 

### Return type

[**Robot**](Robot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_robots**
> list[Robot] get_robots(problem_id)

Robot

Returns a description of the robots, including the current location 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
problem_id = 56 # int | The id of the problem being manipulated

try: 
    # Robot
    api_response = api_instance.get_robots(problem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_robots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 

### Return type

[**list[Robot]**](Robot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_robot**
> update_robot(problem_id, version, robot, robot_id)

Update the existing robot value



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
problem_id = 56 # int | The id of the problem being manipulated
version = 56 # int | The version of the obstacle to be updated.
robot = swagger_client.Robot() # Robot | Robot object that needs to be updated.
robot_id = 56 # int | Robot object that needs to be updated.

try: 
    # Update the existing robot value
    api_instance.update_robot(problem_id, version, robot, robot_id)
except ApiException as e:
    print("Exception when calling RobotApi->update_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **version** | **int**| The version of the obstacle to be updated. | 
 **robot** | [**Robot**](Robot.md)| Robot object that needs to be updated. | 
 **robot_id** | **int**| Robot object that needs to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

