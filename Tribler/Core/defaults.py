"""
Default values for all configurable parameters of the Core.

Author(s): Arno Bakker, Bram Cohen, Egbert Bouman
"""

# WARNING:
#    As we have release Tribler 4.5.0 you must now take into account that
#    people have stored versions of these params on their disk. Make sure
#    you change the version number of the structure and provide upgrade code
#    such that your code won't barf because we loaded an older version from
#    disk that does not have your new fields.
#

import sys
from collections import OrderedDict

from Tribler.Core.Video.defs import PLAYBACKMODE_EXTERNAL_DEFAULT

DEFAULTPORT = 7760

#
# Session opts
#
# History:
#  Version 2: as released in Tribler 4.5.0
#  Version 3: cleanup unused params
#  Version 4: remove swift
#  Version 7: exitnode optin switch added
#  Version 10: BarterCommunity settings added (disabled by default)
#  Version 11: Added a default whether we should upgrade or not.
#  Version 12: Added watch folder options.
#  Version 13: Added HTTP API options.
#  Version 14: Added option to enable/disable channel, previewchannel and tunnel community.
#  Version 15: Added credit mining options
#  Version 16: Changed default VLC video player to external (due to the removal of the wx player).
#  Version 17: Added an option to limit the amount of connections per download.
#  Version 18: Added max upload/download rates for libtorrent.
#  Version 19: Added resource monitor settings.
#  Version 20: Added log directory.
#  Version 21: Removed upgrader settings.

SESSDEFAULTS_VERSION = 21
sessdefaults = OrderedDict()

# General Tribler settings
sessdefaults['general'] = OrderedDict()
sessdefaults['general']['version'] = SESSDEFAULTS_VERSION
sessdefaults['general']['state_dir'] = None
sessdefaults['general']['install_dir'] = u'.'
sessdefaults['general']['ip'] = '0.0.0.0'
sessdefaults['general']['minport'] = DEFAULTPORT
sessdefaults['general']['maxport'] = DEFAULTPORT
sessdefaults['general']['bind'] = []
# allow the client to connect to peers via IPv6 (currently not supported)
sessdefaults['general']['ipv6_enabled'] = 0
# set if an IPv6 server socket won't also field IPv4 connections (default = set automatically)
sessdefaults['general']['ipv6_binds_v4'] = None
sessdefaults['general']['timeout'] = 300.0
sessdefaults['general']['timeout_check_interval'] = 60.0
sessdefaults['general']['eckeypairfilename'] = None
sessdefaults['general']['megacache'] = True
sessdefaults['general']['nickname'] = 'Tribler User'
sessdefaults['general']['mugshot'] = None
sessdefaults['general']['videoanalyserpath'] = None
sessdefaults['general']['peer_icon_path'] = None
sessdefaults['general']['live_aux_seeders'] = []
# Log directory
sessdefaults['general']['log_dir'] = None

# AllChannel community section
sessdefaults['allchannel_community'] = OrderedDict()
sessdefaults['allchannel_community']['enabled'] = True

# Channel community section
sessdefaults['channel_community'] = OrderedDict()
sessdefaults['channel_community']['enabled'] = True

# PreviewChannel community section
sessdefaults['preview_channel_community'] = OrderedDict()
sessdefaults['preview_channel_community']['enabled'] = True

# Search community section
sessdefaults['search_community'] = OrderedDict()
sessdefaults['search_community']['enabled'] = True

# Tunnel community section
sessdefaults['tunnel_community'] = OrderedDict()
sessdefaults['tunnel_community']['socks5_listen_ports'] = [-1] * 5
sessdefaults['tunnel_community']['exitnode_enabled'] = False
sessdefaults['tunnel_community']['enabled'] = True

# Multichain community section
sessdefaults['multichain'] = OrderedDict()
sessdefaults['multichain']['enabled'] = True

# Metadata section
sessdefaults['metadata'] = OrderedDict()
sessdefaults['metadata']['enabled'] = True
sessdefaults['metadata']['store_dir'] = None

# Mainline DHT settings
sessdefaults['mainline_dht'] = OrderedDict()
sessdefaults['mainline_dht']['enabled'] = True
sessdefaults['mainline_dht']['mainline_dht_port'] = -1

# Torrent checking settings
sessdefaults['torrent_checking'] = OrderedDict()
sessdefaults['torrent_checking']['enabled'] = 1

# Torrent store settings
sessdefaults['torrent_store'] = OrderedDict()
sessdefaults['torrent_store']['enabled'] = True
sessdefaults['torrent_store']['dir'] = None

# Torrent collecting settings
sessdefaults['torrent_collecting'] = OrderedDict()
sessdefaults['torrent_collecting']['enabled'] = True
sessdefaults['torrent_collecting']['dht_torrent_collecting'] = True
sessdefaults['torrent_collecting']['torrent_collecting_max_torrents'] = 50000
sessdefaults['torrent_collecting']['torrent_collecting_dir'] = None
sessdefaults['torrent_collecting']['stop_collecting_threshold'] = 200

# Libtorrent settings
sessdefaults['libtorrent'] = OrderedDict()
sessdefaults['libtorrent']['enabled'] = True
sessdefaults['libtorrent']['lt_proxytype'] = 0  # no proxy server is used by default
sessdefaults['libtorrent']['lt_proxyserver'] = None
sessdefaults['libtorrent']['lt_proxyauth'] = None
sessdefaults['libtorrent']['utp'] = True
sessdefaults['libtorrent']['max_connections_download'] = -1
sessdefaults['libtorrent']['max_download_rate'] = 0
sessdefaults['libtorrent']['max_upload_rate'] = 0

# Anonymous libtorrent
sessdefaults['libtorrent']['anon_listen_port'] = -1
sessdefaults['libtorrent']['anon_proxytype'] = 0
sessdefaults['libtorrent']['anon_proxyserver'] = None
sessdefaults['libtorrent']['anon_proxyauth'] = None

# Dispersy config
sessdefaults['dispersy'] = OrderedDict()
sessdefaults['dispersy']['enabled'] = True
sessdefaults['dispersy']['dispersy_port'] = DEFAULTPORT - 1

# Video config
sessdefaults['video'] = OrderedDict()
sessdefaults['video']['enabled'] = True
sessdefaults['video']['path'] = None
sessdefaults['video']['port'] = -1
sessdefaults['video']['preferredmode'] = PLAYBACKMODE_EXTERNAL_DEFAULT

# Watch folder config
sessdefaults['watch_folder'] = OrderedDict()
sessdefaults['watch_folder']['enabled'] = False
sessdefaults['watch_folder']['watch_folder_dir'] = None

# HTTP API config
sessdefaults['http_api'] = OrderedDict()
sessdefaults['http_api']['enabled'] = False
sessdefaults['http_api']['port'] = -1

# Credit mining config
sessdefaults['credit_mining'] = OrderedDict()
sessdefaults['credit_mining']['enabled'] = False
sessdefaults['credit_mining']['max_torrents_per_source'] = 20
sessdefaults['credit_mining']['max_torrents_active'] = 50
sessdefaults['credit_mining']['source_interval'] = 100
sessdefaults['credit_mining']['swarm_interval'] = 100
sessdefaults['credit_mining']['share_mode_target'] = 3
sessdefaults['credit_mining']['tracker_interval'] = 200
sessdefaults['credit_mining']['logging_interval'] = 60
# By default we want to automatically boost legal-predetermined channel.
sessdefaults['credit_mining']['boosting_sources'] = ["http://bt.etree.org/rss/bt_etree_org.rdf"]
sessdefaults['credit_mining']['boosting_enabled'] = ["http://bt.etree.org/rss/bt_etree_org.rdf"]
sessdefaults['credit_mining']['boosting_disabled'] = []
sessdefaults['credit_mining']['archive_sources'] = []
sessdefaults['credit_mining']['policy'] = "seederratio"

# Resource monitor settings
sessdefaults['resource_monitor'] = OrderedDict()
sessdefaults['resource_monitor']['enabled'] = True
sessdefaults['resource_monitor']['poll_interval'] = 5
sessdefaults['resource_monitor']['history_size'] = 20

#
# BT per download opts
#
# History:
#  Version 2: as released in Tribler 4.5.0
#  Version 3:
#  Version 4: allow users to specify a download directory every time
#  Version 6: allow users to overwrite the multifile destination
#  Version 7: swift params
#  Version 8: deleted many of the old params that were not used anymore (due to the switch to libtorrent)
#  Version 9: remove swift
#  Version 10: add default anonymous level
#  Version 11: remove createmerkletorrent, torrentsigkeypairfilename, makehash_md5, makehash_crc32, makehash_sha1
#  Version 12: remove thumb
#  Version 13: remove super_seeder
#  Version 15: add seeding ratio
#  Version 16: added field whether the download has been manually stopped by the user and time added

DLDEFAULTS_VERSION = 16
dldefaults = OrderedDict()

# General download settings
dldefaults['downloadconfig'] = OrderedDict()
dldefaults['downloadconfig']['version'] = DLDEFAULTS_VERSION
dldefaults['downloadconfig']['saveas'] = None  # Set to get_default_destdir()
dldefaults['downloadconfig']['max_upload_rate'] = 0
dldefaults['downloadconfig']['max_download_rate'] = 0
dldefaults['downloadconfig']['mode'] = 0
dldefaults['downloadconfig']['hops'] = 0
dldefaults['downloadconfig']['selected_files'] = []
dldefaults['downloadconfig']['correctedfilename'] = None
dldefaults['downloadconfig']['safe_seeding'] = False
# Valid values: 'forever', 'never', 'ratio', 'time'
dldefaults['downloadconfig']['seeding_mode'] = 'ratio'
dldefaults['downloadconfig']['seeding_ratio'] = 2.0
dldefaults['downloadconfig']['seeding_time'] = 60
dldefaults['downloadconfig']['user_stopped'] = False
dldefaults['downloadconfig']['time_added'] = 0

tdefdictdefaults = {}
tdefdictdefaults['comment'] = None
tdefdictdefaults['created by'] = None
tdefdictdefaults['announce'] = None
tdefdictdefaults['announce-list'] = None
tdefdictdefaults['nodes'] = None  # mainline DHT
tdefdictdefaults['httpseeds'] = None
tdefdictdefaults['url-list'] = None
tdefdictdefaults['encoding'] = None

tdefmetadefaults = {}
tdefmetadefaults['version'] = 1
tdefmetadefaults['piece length'] = 0

TDEF_DEFAULTS = {}
TDEF_DEFAULTS.update(tdefdictdefaults)
TDEF_DEFAULTS.update(tdefmetadefaults)


# Tribler defaults
tribler_defaults = OrderedDict()
tribler_defaults['Tribler'] = OrderedDict()

tribler_defaults['Tribler']['confirmonclose'] = 1
# RateLimitPanel
tribler_defaults['Tribler']['maxuploadrate'] = 0
tribler_defaults['Tribler']['maxdownloadrate'] = 0
# Anon tunnel
tribler_defaults['Tribler']['default_number_hops'] = 1
tribler_defaults['Tribler']['default_anonymity_enabled'] = True
tribler_defaults['Tribler']['default_safeseeding_enabled'] = True
# GUI
tribler_defaults['Tribler']['window_width'] = 1024
tribler_defaults['Tribler']['window_height'] = 670
tribler_defaults['Tribler']['sash_position'] = -185
tribler_defaults['Tribler']['family_filter'] = 1
tribler_defaults['Tribler']['window_x'] = ""
tribler_defaults['Tribler']['window_y'] = ""
# WebUI
tribler_defaults['Tribler']['use_webui'] = 0
tribler_defaults['Tribler']['webui_port'] = 8080
# Emercoin
tribler_defaults['Tribler']['use_emc'] = 0
tribler_defaults['Tribler']['emc_ip'] = '127.0.0.1'
tribler_defaults['Tribler']['emc_port'] = '8332'
tribler_defaults['Tribler']['emc_username'] = 'tribler'
tribler_defaults['Tribler']['emc_password'] = 'tribler'
# Misc
tribler_defaults['Tribler']['showsaveas'] = 1
tribler_defaults['Tribler']['i2ilistenport'] = 57891
tribler_defaults['Tribler']['mintray'] = 2 if sys.platform == 'win32' else 0
tribler_defaults['Tribler']['free_space_threshold'] = 100 * 1024 * 1024
tribler_defaults['Tribler']['version_info'] = {}
tribler_defaults['Tribler']['last_reported_version'] = None
