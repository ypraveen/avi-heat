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


class HSMSafenetClientInfo(object):
    # all schemas
    client_priv_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("Client Private Key generated by createCert"),
        required=False,
        update_allowed=True,
    )
    client_cert_schema = properties.Schema(
        properties.Schema.STRING,
        _("Client Certificate generated by createCert"),
        required=False,
        update_allowed=True,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name prepended to client key and certificate filename"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'client_priv_key',
        'client_cert',
        'client_ip',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'client_priv_key': client_priv_key_schema,
        'client_cert': client_cert_schema,
        'client_ip': client_ip_schema,
    }




class HSMThalesRFS(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of the RFS server from where to sync the Thales encrypted private key"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Port at which the RFS server accepts the sync request from clients for Thales encrypted private key"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip',
        'port',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'port': port_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip': getattr(IpAddr, 'field_references', {}),
    }



class HSMThalesNetHsm(object):
    # all schemas
    remote_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of the netHSM device"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    remote_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Port at which the netHSM device accepts the connection"),
        required=False,
        update_allowed=True,
    )
    esn_schema = properties.Schema(
        properties.Schema.STRING,
        _("Electronic serial number of the netHSM device. Use Thales anonkneti utility to find the netHSM ESN"),
        required=True,
        update_allowed=True,
    )
    module_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Local module id of the netHSM device"),
        required=False,
        update_allowed=True,
    )
    keyhash_schema = properties.Schema(
        properties.Schema.STRING,
        _("Hash of the key that netHSM device uses to authenticate itself. Use Thales anonkneti utility to find the netHSM keyhash"),
        required=True,
        update_allowed=True,
    )
    priority_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Priority class of the nethsm in an high availability setup. 1 is the highest priority and 100 is the lowest priority"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'remote_ip',
        'remote_port',
        'esn',
        'module_id',
        'keyhash',
        'priority',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'remote_ip': remote_ip_schema,
        'remote_port': remote_port_schema,
        'esn': esn_schema,
        'module_id': module_id_schema,
        'keyhash': keyhash_schema,
        'priority': priority_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'remote_ip': getattr(IpAddr, 'field_references', {}),
    }



class HSMSafenetLunaServer(object):
    # all schemas
    remote_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("IP address of the Safenet/Gemalto HSM device"),
        required=True,
        update_allowed=True,
    )
    server_cert_schema = properties.Schema(
        properties.Schema.STRING,
        _("CA certificate of the server"),
        required=True,
        update_allowed=True,
    )
    partition_passwd_schema = properties.Schema(
        properties.Schema.STRING,
        _("Password of the partition assigned to this client"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'remote_ip',
        'server_cert',
        'partition_passwd',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'remote_ip': remote_ip_schema,
        'server_cert': server_cert_schema,
        'partition_passwd': partition_passwd_schema,
    }




class HSMSafenetLuna(object):
    # all schemas
    server_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HSMSafenetLunaServer.properties_schema,
        required=True,
        update_allowed=False,
    )
    server_schema = properties.Schema(
        properties.Schema.LIST,
        _("SafeNet/Gemalto HSM Servers used for crypto operations"),
        schema=server_item_schema,
        required=False,
        update_allowed=True,
    )
    is_ha_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Set to indicate HA across more than one servers"),
        required=True,
        update_allowed=True,
    )
    node_info_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HSMSafenetClientInfo.properties_schema,
        required=True,
        update_allowed=False,
    )
    node_info_schema = properties.Schema(
        properties.Schema.LIST,
        _("Node specific information"),
        schema=node_info_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server',
        'is_ha',
        'node_info',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server': server_schema,
        'is_ha': is_ha_schema,
        'node_info': node_info_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'node_info': getattr(HSMSafenetClientInfo, 'field_references', {}),
        'server': getattr(HSMSafenetLunaServer, 'field_references', {}),
    }



class HardwareSecurityModule(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("HSM type to use"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HSM_TYPE_THALES_NETHSM', 'HSM_TYPE_SAFENET_LUNA']),
        ],
    )
    rfs_schema = properties.Schema(
        properties.Schema.MAP,
        _("Thales Remote File Server (RFS), used for the netHSMs, configuration"),
        schema=HSMThalesRFS.properties_schema,
        required=False,
        update_allowed=True,
    )
    nethsm_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HSMThalesNetHsm.properties_schema,
        required=True,
        update_allowed=False,
    )
    nethsm_schema = properties.Schema(
        properties.Schema.LIST,
        _("Thales netHSM specific configuration"),
        schema=nethsm_item_schema,
        required=False,
        update_allowed=True,
    )
    sluna_schema = properties.Schema(
        properties.Schema.MAP,
        _("Safenet/Gemalto Luna/Gem specific configuration"),
        schema=HSMSafenetLuna.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'rfs',
        'nethsm',
        'sluna',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'rfs': rfs_schema,
        'nethsm': nethsm_schema,
        'sluna': sluna_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rfs': getattr(HSMThalesRFS, 'field_references', {}),
        'sluna': getattr(HSMSafenetLuna, 'field_references', {}),
        'nethsm': getattr(HSMThalesNetHsm, 'field_references', {}),
    }



class HardwareSecurityModuleGroup(AviResource):
    resource_name = "hardwaresecuritymodulegroup"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the HSM Group configuration object"),
        required=True,
        update_allowed=True,
    )
    hsm_schema = properties.Schema(
        properties.Schema.MAP,
        _("Hardware Security Module configuration"),
        schema=HardwareSecurityModule.properties_schema,
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'hsm',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'hsm': hsm_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'hsm': getattr(HardwareSecurityModule, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::HardwareSecurityModuleGroup': HardwareSecurityModuleGroup,
    }

