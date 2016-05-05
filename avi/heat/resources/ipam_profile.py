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


class DNSInternalNSRecord(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Nameserver for NS record"),
        required=True,
        update_allowed=True,
    )
    ip_address_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of the Nameserver"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'ip_address',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'ip_address': ip_address_schema,
    }




class InfobloxProfile(object):
    # all schemas
    wapi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("WAPI version"),
        required=False,
        update_allowed=True,
    )
    dns_view_schema = properties.Schema(
        properties.Schema.STRING,
        _("DNS view"),
        required=False,
        update_allowed=True,
    )
    network_view_schema = properties.Schema(
        properties.Schema.STRING,
        _("Network view"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'wapi_version',
        'dns_view',
        'network_view',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'wapi_version': wapi_version_schema,
        'dns_view': dns_view_schema,
        'network_view': network_view_schema,
    }




class IpamAwsProfile(object):
    # all schemas
    region_schema = properties.Schema(
        properties.Schema.STRING,
        _("AWS region"),
        required=False,
        update_allowed=True,
    )
    vpc_schema = properties.Schema(
        properties.Schema.STRING,
        _("VPC name"),
        required=False,
        update_allowed=True,
    )
    vpc_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("VPC ID"),
        required=True,
        update_allowed=True,
    )
    use_iam_roles_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    access_key_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("AWS access key ID"),
        required=False,
        update_allowed=True,
    )
    secret_access_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("AWS secret access key"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'region',
        'vpc',
        'vpc_id',
        'use_iam_roles',
        'access_key_id',
        'secret_access_key',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'region': region_schema,
        'vpc': vpc_schema,
        'vpc_id': vpc_id_schema,
        'use_iam_roles': use_iam_roles_schema,
        'access_key_id': access_key_id_schema,
        'secret_access_key': secret_access_key_schema,
    }




class IpamInternalProfile(object):
    # all schemas
    service_domain_schema = properties.Schema(
        properties.Schema.STRING,
        _("Authority Domain Name for Service Discovery.Services will be registered as service_name.service_domain"),
        required=False,
        update_allowed=True,
    )
    service_record_ttl_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("TTL value for service records."),
        required=False,
        update_allowed=True,
    )
    ns_records_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DNSInternalNSRecord.properties_schema,
        required=True,
        update_allowed=False,
    )
    ns_records_schema = properties.Schema(
        properties.Schema.LIST,
        _("NameServer records for non Avi authoritative domains."),
        schema=ns_records_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'service_domain',
        'service_record_ttl',
        'ns_records',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'service_domain': service_domain_schema,
        'service_record_ttl': service_record_ttl_schema,
        'ns_records': ns_records_schema,
    }




class IpamProfile(AviResource):
    resource_name = "ipamprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The name of the IPAM profile"),
        required=True,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of IPAM profile"),
        required=True,
        update_allowed=True,
    )
    ip_address_schema = properties.Schema(
        properties.Schema.MAP,
        _("IPAM_TYPE_INFOBLOX address of IPAM appliance"),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    username_schema = properties.Schema(
        properties.Schema.STRING,
        _("Username for API access for IPAM appliance"),
        required=False,
        update_allowed=True,
    )
    password_schema = properties.Schema(
        properties.Schema.STRING,
        _("Username for API access for IPAM appliance"),
        required=False,
        update_allowed=True,
    )
    infoblox_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=InfobloxProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    internal_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpamInternalProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    aws_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpamAwsProfile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'type',
        'ip_address',
        'username',
        'password',
        'infoblox_profile',
        'internal_profile',
        'aws_profile',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'type': type_schema,
        'ip_address': ip_address_schema,
        'username': username_schema,
        'password': password_schema,
        'infoblox_profile': infoblox_profile_schema,
        'internal_profile': internal_profile_schema,
        'aws_profile': aws_profile_schema,
    }




def resource_mapping():
    return {
        'Avi::IpamProfile': IpamProfile,
    }
