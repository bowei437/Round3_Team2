# swagger_client.ObstaclesApi

All URIs are relative to *http://localhost/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_obstacle**](ObstaclesApi.md#add_obstacle) | **POST** /id&#x3D;{problem_id}/Obstacles/ver&#x3D;{version}/ | Add a new obstacle to the list
[**delete_obstacle**](ObstaclesApi.md#delete_obstacle) | **DELETE** /id&#x3D;{problem_id}/Obstacles/obstacle_id&#x3D;{obstacle_id}/ver&#x3D;{version}/ | Delete Obstacle
[**get_obstacle**](ObstaclesApi.md#get_obstacle) | **GET** /id&#x3D;{problem_id}/Obstacles/obstacle_id&#x3D;{obstacle_id} | Obstacles
[**get_obstacles**](ObstaclesApi.md#get_obstacles) | **GET** /id&#x3D;{problem_id}/Obstacles | Obstacles
[**update_obstacle**](ObstaclesApi.md#update_obstacle) | **PUT** /id&#x3D;{problem_id}/Obstacles/obstacle_id&#x3D;{obstacle_id}/ver&#x3D;{version}/ | Update an existing obstacle


# **add_obstacle**
> int add_obstacle(problem_id, version, obstacle)

Add a new obstacle to the list



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObstaclesApi()
problem_id = 56 # int | The id of the problem being manipulated
version = 56 # int | The version of the obstacle to be updated.
obstacle = swagger_client.Obstacle() # Obstacle | Obstacle object that needs to be added to the list.

try: 
    # Add a new obstacle to the list
    api_response = api_instance.add_obstacle(problem_id, version, obstacle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObstaclesApi->add_obstacle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **version** | **int**| The version of the obstacle to be updated. | 
 **obstacle** | [**Obstacle**](Obstacle.md)| Obstacle object that needs to be added to the list. | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_obstacle**
> delete_obstacle(problem_id, obstacle_id, version)

Delete Obstacle

This removes the obstacle by the given ID

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObstaclesApi()
problem_id = 56 # int | The id of the problem being manipulated
obstacle_id = 56 # int | The ID of the Obstacle that needs to be deleted.
version = 56 # int | The version of the obstacle to be updated.

try: 
    # Delete Obstacle
    api_instance.delete_obstacle(problem_id, obstacle_id, version)
except ApiException as e:
    print("Exception when calling ObstaclesApi->delete_obstacle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **obstacle_id** | **int**| The ID of the Obstacle that needs to be deleted. | 
 **version** | **int**| The version of the obstacle to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obstacle**
> Obstacle get_obstacle(problem_id, obstacle_id)

Obstacles

Returns an obstacle 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObstaclesApi()
problem_id = 56 # int | The id of the problem being manipulated
obstacle_id = 56 # int | The id of the obstacle to be updated.

try: 
    # Obstacles
    api_response = api_instance.get_obstacle(problem_id, obstacle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObstaclesApi->get_obstacle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **obstacle_id** | **int**| The id of the obstacle to be updated. | 

### Return type

[**Obstacle**](Obstacle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obstacles**
> list[Obstacle] get_obstacles(problem_id)

Obstacles

Returns a list of all of the obstacles in the problem. This can be an empty list. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObstaclesApi()
problem_id = 56 # int | The id of the problem being manipulated

try: 
    # Obstacles
    api_response = api_instance.get_obstacles(problem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObstaclesApi->get_obstacles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 

### Return type

[**list[Obstacle]**](Obstacle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_obstacle**
> update_obstacle(problem_id, obstacle_id, version, updated_obstacle=updated_obstacle)

Update an existing obstacle



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObstaclesApi()
problem_id = 56 # int | The id of the problem being manipulated
obstacle_id = 56 # int | The id of the obstacle to be updated.
version = 56 # int | The version of the obstacle to be updated.
updated_obstacle = swagger_client.Obstacle() # Obstacle | Obstacle object that needs to be added to the list. (optional)

try: 
    # Update an existing obstacle
    api_instance.update_obstacle(problem_id, obstacle_id, version, updated_obstacle=updated_obstacle)
except ApiException as e:
    print("Exception when calling ObstaclesApi->update_obstacle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_id** | **int**| The id of the problem being manipulated | 
 **obstacle_id** | **int**| The id of the obstacle to be updated. | 
 **version** | **int**| The version of the obstacle to be updated. | 
 **updated_obstacle** | [**Obstacle**](Obstacle.md)| Obstacle object that needs to be added to the list. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

