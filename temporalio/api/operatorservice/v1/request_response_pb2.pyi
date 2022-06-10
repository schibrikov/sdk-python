"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import temporalio.api.enums.v1.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AddSearchAttributesRequest(google.protobuf.message.Message):
    """(-- Search Attribute --)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class SearchAttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def search_attributes(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        typing.Text, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
    ]:
        """Mapping between search attribute name and its IndexedValueType."""
        pass
    def __init__(
        self,
        *,
        search_attributes: typing.Optional[
            typing.Mapping[
                typing.Text,
                temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType,
            ]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "search_attributes", b"search_attributes"
        ],
    ) -> None: ...

global___AddSearchAttributesRequest = AddSearchAttributesRequest

class AddSearchAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___AddSearchAttributesResponse = AddSearchAttributesResponse

class RemoveSearchAttributesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def search_attributes(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Search attribute names to delete."""
        pass
    def __init__(
        self,
        *,
        search_attributes: typing.Optional[typing.Iterable[typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "search_attributes", b"search_attributes"
        ],
    ) -> None: ...

global___RemoveSearchAttributesRequest = RemoveSearchAttributesRequest

class RemoveSearchAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___RemoveSearchAttributesResponse = RemoveSearchAttributesResponse

class ListSearchAttributesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___ListSearchAttributesRequest = ListSearchAttributesRequest

class ListSearchAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class CustomAttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    class SystemAttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    class StorageSchemaEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    CUSTOM_ATTRIBUTES_FIELD_NUMBER: builtins.int
    SYSTEM_ATTRIBUTES_FIELD_NUMBER: builtins.int
    STORAGE_SCHEMA_FIELD_NUMBER: builtins.int
    @property
    def custom_attributes(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        typing.Text, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
    ]:
        """Mapping between custom (user-registered) search attribute name to its IndexedValueType."""
        pass
    @property
    def system_attributes(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        typing.Text, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
    ]:
        """Mapping between system (predefined) search attribute name to its IndexedValueType."""
        pass
    @property
    def storage_schema(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Mapping from the attribute name to the visibility storage native type."""
        pass
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[
            typing.Mapping[
                typing.Text,
                temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType,
            ]
        ] = ...,
        system_attributes: typing.Optional[
            typing.Mapping[
                typing.Text,
                temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType,
            ]
        ] = ...,
        storage_schema: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "custom_attributes",
            b"custom_attributes",
            "storage_schema",
            b"storage_schema",
            "system_attributes",
            b"system_attributes",
        ],
    ) -> None: ...

global___ListSearchAttributesResponse = ListSearchAttributesResponse

class DeleteNamespaceRequest(google.protobuf.message.Message):
    """(-- api-linter: core::0135::request-unknown-fields=disabled
        aip.dev/not-precedent: DeleteNamespace RPC doesn't follow Google API format. --)
    (-- api-linter: core::0135::request-name-required=disabled
        aip.dev/not-precedent: DeleteNamespace RPC doesn't follow Google API format. --)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    def __init__(
        self,
        *,
        namespace: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["namespace", b"namespace"]
    ) -> None: ...

global___DeleteNamespaceRequest = DeleteNamespaceRequest

class DeleteNamespaceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DELETED_NAMESPACE_FIELD_NUMBER: builtins.int
    deleted_namespace: typing.Text
    """Temporary namespace name that is used during reclaim resources step."""

    def __init__(
        self,
        *,
        deleted_namespace: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "deleted_namespace", b"deleted_namespace"
        ],
    ) -> None: ...

global___DeleteNamespaceResponse = DeleteNamespaceResponse