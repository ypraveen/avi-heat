# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class HdrPersistenceProfile(object):
    # all schemas
    prst_hdr_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Header name for custom header persistence"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prst_hdr_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prst_hdr_name': prst_hdr_name_schema,
    }




class IPPersistenceProfile(object):
    # all schemas
    ip_persistent_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The length of time after a client's connections have closed before expiring the client's persistence to a server."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip_persistent_timeout',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_persistent_timeout': ip_persistent_timeout_schema,
    }




class HttpCookiePersistenceKey(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("name to use for cookie encryption"),
        required=False,
        update_allowed=True,
    )
    aes_key_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    hmac_key_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'aes_key',
        'hmac_key',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'aes_key': aes_key_schema,
        'hmac_key': hmac_key_schema,
    }




class HttpCookiePersistenceProfile(object):
    # all schemas
    encryption_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("Key name to use for cookie encryption"),
        required=False,
        update_allowed=True,
    )
    cookie_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("HTTP cookie name for cookie persistence"),
        required=False,
        update_allowed=True,
    )
    key_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HttpCookiePersistenceKey.properties_schema,
        required=True,
        update_allowed=False,
    )
    key_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=key_item_schema,
        required=False,
        update_allowed=True,
    )
    timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The length of time after a client's connections have closed before expiring the client's persistence to a server. No value or 'zero' indicates no timeout."),
        required=False,
        update_allowed=True,
    )
    always_send_cookie_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("If no persistence cookie was received from the client, always send it."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'encryption_key',
        'cookie_name',
        'key',
        'timeout',
        'always_send_cookie',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'encryption_key': encryption_key_schema,
        'cookie_name': cookie_name_schema,
        'key': key_schema,
        'timeout': timeout_schema,
        'always_send_cookie': always_send_cookie_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'key': getattr(HttpCookiePersistenceKey, 'field_references', {}),
    }



class AppCookiePersistenceProfile(object):
    # all schemas
    prst_hdr_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Header or cookie name for application cookie persistence"),
        required=True,
        update_allowed=True,
    )
    timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The length of time after a client's connections have closed before expiring the client's persistence to a server."),
        required=False,
        update_allowed=True,
    )
    encryption_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("Key to use for cookie encryption"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prst_hdr_name',
        'timeout',
        'encryption_key',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prst_hdr_name': prst_hdr_name_schema,
        'timeout': timeout_schema,
        'encryption_key': encryption_key_schema,
    }




class ApplicationPersistenceProfile(AviResource):
    resource_name = "applicationpersistenceprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name for the persistence profile."),
        required=True,
        update_allowed=True,
    )
    server_hm_down_recovery_schema = properties.Schema(
        properties.Schema.STRING,
        _("Specifies behavior when a persistent server has been marked down by a health monitor."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HM_DOWN_CONTINUE_PERSISTENT_SERVER', 'HM_DOWN_PICK_NEW_SERVER', 'HM_DOWN_ABORT_CONNECTION']),
        ],
    )
    persistence_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Method used to persist clients to the same server for a duration of time or a session."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PERSISTENCE_TYPE_CUSTOM_HTTP_HEADER', 'PERSISTENCE_TYPE_CLIENT_IP_ADDRESS', 'PERSISTENCE_TYPE_HTTP_COOKIE', 'PERSISTENCE_TYPE_APP_COOKIE', 'PERSISTENCE_TYPE_CLIENT_IPV6_ADDRESS', 'PERSISTENCE_TYPE_TLS']),
        ],
    )
    ip_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the Client IP Persistence profile parameters."),
        schema=IPPersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    hdr_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the custom HTTP Header Persistence profile parameters."),
        schema=HdrPersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    app_cookie_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the Application Cookie Persistence profile parameters."),
        schema=AppCookiePersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    http_cookie_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the HTTP Cookie Persistence profile parameters."),
        schema=HttpCookiePersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'server_hm_down_recovery',
        'persistence_type',
        'ip_persistence_profile',
        'hdr_persistence_profile',
        'app_cookie_persistence_profile',
        'http_cookie_persistence_profile',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'server_hm_down_recovery': server_hm_down_recovery_schema,
        'persistence_type': persistence_type_schema,
        'ip_persistence_profile': ip_persistence_profile_schema,
        'hdr_persistence_profile': hdr_persistence_profile_schema,
        'app_cookie_persistence_profile': app_cookie_persistence_profile_schema,
        'http_cookie_persistence_profile': http_cookie_persistence_profile_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'http_cookie_persistence_profile': getattr(HttpCookiePersistenceProfile, 'field_references', {}),
        'ip_persistence_profile': getattr(IPPersistenceProfile, 'field_references', {}),
        'app_cookie_persistence_profile': getattr(AppCookiePersistenceProfile, 'field_references', {}),
        'hdr_persistence_profile': getattr(HdrPersistenceProfile, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::ApplicationPersistenceProfile': ApplicationPersistenceProfile,
    }

