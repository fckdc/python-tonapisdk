# EncryptedComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_type** | **str** |  | 
**cipher_text** | **str** |  | 

## Example

```python
from fdtapi.models.encrypted_comment import EncryptedComment

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptedComment from a JSON string
encrypted_comment_instance = EncryptedComment.from_json(json)
# print the JSON string representation of the object
print EncryptedComment.to_json()

# convert the object into a dict
encrypted_comment_dict = encrypted_comment_instance.to_dict()
# create an instance of EncryptedComment from a dict
encrypted_comment_form_dict = encrypted_comment.from_dict(encrypted_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


