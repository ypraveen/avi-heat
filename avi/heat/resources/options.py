# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *



class IpAddr(object):
    # all schemas
    addr_schema = properties.Schema(
        properties.Schema.STRING,
        _("IP address"),
        required=True,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['V4', 'DNS']),
        ],
    )

    # properties list
    PROPERTIES = (
        'addr',
        'type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'addr': addr_schema,
        'type': type_schema,
    }




class IpAddrPrefix(object):
    # all schemas
    ip_addr_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    mask_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip_addr',
        'mask',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_addr': ip_addr_schema,
        'mask': mask_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip_addr': getattr(IpAddr, 'field_references', {}),
    }

