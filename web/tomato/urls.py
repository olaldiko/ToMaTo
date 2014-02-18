# -*- coding: utf-8 -*-

# ToMaTo (Topology management software) 
# Copyright (C) 2010 Dennis Schwerdel, University of Kaiserslautern
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'tomato.main.index'),
	(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'fonts'}),
	(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'img'}),
	(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'js'}),
	(r'^style/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'style'}),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^help$', 'tomato.help.help'),
	(r'^help/contact$', 'tomato.help.contact_form'),
	(r'^help/(?P<page>.*)$', 'tomato.help.help'),
	(r'^login$', 'tomato.main.login'),
	(r'^logout$', 'tomato.main.logout'),
	(r'^account/register$', 'tomato.account.register'),	
	url(r'^account/list$', 'tomato.account.list', {"organization": True}, name="account_list"),	
	url(r'^account/list/all$', 'tomato.account.list', {"organization": False}, name="account_list_all"),	
	url(r'^account/registrations$', 'tomato.account.list', {"organization": True, "with_flag": "new_account"}, name="account_list_registrations"),	
	url(r'^account/registrations/all$', 'tomato.account.list', {"organization": False, "with_flag": "new_account"}, name="account_list_registrations_all"),	
	url(r'^organization/(?P<organization>\w+)/accounts$', 'tomato.account.list', name="organization_accounts"),
	(r'^account$', 'tomato.account.info'),	
	(r'^account/(?P<id>[^/]+)$', 'tomato.account.info'),	
	(r'^account/(?P<id>[^/]+)/accept$', 'tomato.account.accept'),	
	(r'^account/(?P<id>[^/]+)/edit$', 'tomato.account.edit'),	
	(r'^account/(?P<id>[^/]+)/remove$', 'tomato.account.remove'),	
	(r'^account/(?P<id>[^/]+)/reset_password$', 'tomato.account.reset_password'),	
	url(r'^topology$', 'tomato.topology.list', {"show_all": False}, name="topology_list"),
	url(r'^topology/all$', 'tomato.topology.list', {"show_all": True}, name="topology_list_all"),
	url(r'^organization/(?P<organization>\w+)/topologies$', 'tomato.topology.list', {"show_all": True}, name="organization_topologies"),
	(r'^topology/(?P<id>\d+)$', 'tomato.topology.info'),
	(r'^topology/(?P<id>\d+)/export$', 'tomato.topology.export'),
	(r'^topology/(?P<id>\d+)/usage$', 'tomato.topology.usage'),
	(r'^topology/create$', 'tomato.topology.create'),
	(r'^topology/import$', 'tomato.topology.import_'),
	(r'^tutorial$', 'tomato.tutorial.list'),
	(r'^tutorial/start$', 'tomato.tutorial.start'),
	(r'^connection/(?P<id>\d+)/usage$', 'tomato.connection.usage'),
	(r'^element/(?P<id>\d+)/usage$', 'tomato.element.usage'),
	(r'^element/(?P<id>\d+)/rextfv_status$', 'tomato.element.rextfv_status'),
	(r'^element/(?P<id>\d+)/console$', 'tomato.element.console'),
	(r'^element/(?P<id>\d+)/console_novnc$', 'tomato.element.console_novnc'),
	(r'^map/$', 'tomato.site.map'),
	(r'^map.kml$', 'tomato.site.map_kml'),
	(r'^link_stats/(?P<site>\w+)$', 'tomato.site.details_site'),
	(r'^link_stats/(?P<src>\w+)/(?P<dst>\w+)$', 'tomato.site.details_link'),
	url(r'^host/$', 'tomato.host.list', {"organization": None, "site": None}, name="host_list"),
	url(r'^organization/(?P<organization>\w+)/hosts$', 'tomato.host.list', name="organization_hosts"),
	url(r'^site/(?P<site>\w+)/hosts$', 'tomato.host.list', name="site_hosts"),
	(r'^host/add$', 'tomato.host.add'),
	(r'^host/(?P<address>[^/]+)$', 'tomato.host.info'),
	(r'^host/(?P<address>[^/]+)/edit$', 'tomato.host.edit'),
	(r'^host/(?P<address>[^/]+)/remove$', 'tomato.host.remove'),
	(r'^organization/$', 'tomato.organization.list'),
	(r'^organization/add$', 'tomato.organization.add'),
	(r'^organization/(?P<name>\w+)$', 'tomato.organization.info'),
	(r'^organization/(?P<name>\w+)/edit$', 'tomato.organization.edit'),
	(r'^organization/(?P<name>\w+)/remove$', 'tomato.organization.remove'),
	(r'^organization/(?P<organization>\w+)/add_site$', 'tomato.site.add'),
	(r'^site/(?P<name>\w+)/edit$', 'tomato.site.edit'),
	(r'^site/(?P<name>\w+)/remove$', 'tomato.site.remove'),
	url(r'^template/$', 'tomato.template.list', {"tech": None}, name="template_list"),
	url(r'^template/bytech/(?P<tech>\w+)$', 'tomato.template.list', name="template_list_bytech"),
	(r'^template/add$', 'tomato.template.add'),
	(r'^template/(?P<res_id>\d+)$', 'tomato.template.info'),
	(r'^template/(?P<res_id>\d+)/edit$', 'tomato.template.edit'),
	(r'^template/(?P<res_id>\d+)/edit/torrent$', 'tomato.template.edit_torrent'),
	(r'^template/(?P<res_id>\d+)/remove$', 'tomato.template.remove'),
	url(r'^profile/$', 'tomato.profile.list', {"tech": None}, name="profile_list"),
	url(r'^profile/bytech/(?P<tech>\w+)$', 'tomato.profile.list', name="profile_list_bytech"),
	(r'^profile/add/$', 'tomato.profile.add'),
	(r'^profile/(?P<res_id>\d+)$', 'tomato.profile.info'),
	(r'^profile/(?P<res_id>\d+)/edit$', 'tomato.profile.edit'),
	(r'^profile/(?P<res_id>\d+)/remove$', 'tomato.profile.remove'),
	(r'^external_network/$', 'tomato.external_network.list'),
	(r'^external_network/add/$', 'tomato.external_network.add'),
	(r'^external_network/(?P<res_id>\d+)/edit$', 'tomato.external_network.edit'),
	(r'^external_network/(?P<res_id>\d+)/remove$', 'tomato.external_network.remove'),
	url(r'^external_network/(?P<network>\d+)/instances$', 'tomato.external_network_instance.list', name="external_network_instances"),
	url(r'^external_network_instance$', 'tomato.external_network_instance.list', name="external_network_instances_all"),
	(r'^external_network_instance/add$', 'tomato.external_network_instance.add'),
	(r'^external_network_instance/(?P<res_id>\d+)/edit$', 'tomato.external_network_instance.edit'),
	(r'^external_network_instance/(?P<res_id>\d+)/remove$', 'tomato.external_network_instance.remove'),
	url(r'^host/(?P<host>[^/]+)/external_networks$', 'tomato.external_network_instance.list', name="host_external_networks"),
	url(r'^host/(?P<host>[^/]+)/external_network/(?P<network>\d+)$', 'tomato.external_network_instance.list', name="host_external_network"),
	url(r'^site/(?P<site>[^/]+)/external_networks$', 'tomato.external_network_instance.list', name="site_external_networks"),
	url(r'^site/(?P<site>[^/]+)/external_network/(?P<network>\d+)$', 'tomato.external_network_instance.list', name="site_external_network"),
	url(r'^organization/(?P<organization>[^/]+)/external_networks$', 'tomato.external_network_instance.list', name="organization_external_networks"),
	url(r'^organization/(?P<organization>[^/]+)/external_network/(?P<network>\d+)$', 'tomato.external_network_instance.list', name="organization_external_network"),
	(r'^ajax/topology/(?P<id>\d+)/info$', 'tomato.ajax.topology_info'),
	(r'^ajax/topology/(?P<id>\d+)/action$', 'tomato.ajax.topology_action'),
	(r'^ajax/topology/(?P<id>\d+)/modify$', 'tomato.ajax.topology_modify'),
	(r'^ajax/topology/(?P<id>\d+)/permission$', 'tomato.ajax.topology_permission'),
	(r'^ajax/topology/(?P<id>\d+)/remove$', 'tomato.ajax.topology_remove'),
	(r'^ajax/element/(?P<id>\d+)/info$', 'tomato.ajax.element_info'),
	(r'^ajax/topology/(?P<topid>\d+)/create_element$', 'tomato.ajax.element_create'),
	(r'^ajax/element/(?P<id>\d+)/action$', 'tomato.ajax.element_action'),
	(r'^ajax/element/(?P<id>\d+)/modify$', 'tomato.ajax.element_modify'),
	(r'^ajax/element/(?P<id>\d+)/remove$', 'tomato.ajax.element_remove'),
	(r'^ajax/element/(?P<id>\d+)/rextfv_status$', 'tomato.ajax.element_rextfv_status'),
	(r'^ajax/connection/(?P<id>\d+)/info$', 'tomato.ajax.connection_info'),
	(r'^ajax/connection/create$', 'tomato.ajax.connection_create'),
	(r'^ajax/connection/(?P<id>\d+)/action$', 'tomato.ajax.connection_action'),
	(r'^ajax/connection/(?P<id>\d+)/modify$', 'tomato.ajax.connection_modify'),
	(r'^ajax/connection/(?P<id>\d+)/remove$', 'tomato.ajax.connection_remove'),
	(r'^ajax/account/(?P<name>.*)/info', 'tomato.ajax.account_info'),
)
