#!/usr/bin/python


DOCUMENTATION = '''
---

module: ansible_plugin
short_description: Download plugins from proveided URL to dest folder with dependencies

'''

EXAMPLES = '''
- name: Stop jenkins before updates
  service:
    name: jenkins
    state: stopped

- name: Download plugins
  jenkins_download_plugin:
    name:
      - greenballs
      - job-dsl
    update_url: {{ update_url }}
    dest: /var/lib/jenkins/plugins

- name: Immediately restart Jenkins after installed plugins
  service:
    name: jenkins
    state: restarted

- name: Wait for Jenkins to start up
  uri:
    url: "{{ jenkins_url }}"
    status_code: 200
    timeout: 5
    validate_certs: no
  register: jenkins_service_status
  retries: 60
  delay: 5
  until: >
    'status' in jenkins_service_status and
    jenkins_service_status['status'] == 200

'''


import os
import re
import sys
import urllib2
import zipfile
import contextlib

from ansible.module_utils.basic import AnsibleModule

class JenkinsPlugin:

    def __init__(self, param_list):
        self.param_list = param_list
        self.return_json = {
                "changed" : True,
                "msg"     : ""
            }

        self.downloaded_plugins = set()

    def get_plugin(self):
        for plugin_name in self.param_list['name']:
            self._download_plugin(plugin_name)

        return self.return_json

    def _download_plugin(self, plugin_name):

        if (plugin_name not in self.downloaded_plugins):

            print("Download plugin: " + self._plugin_url(plugin_name))
            with open(self._path_to_plugin(plugin_name), 'wb') as output:
                output.write(urllib2.urlopen(self._plugin_url(plugin_name)).read())

            self.downloaded_plugins.add(plugin_name)

            with contextlib.closing(zipfile.ZipFile(self._path_to_plugin(plugin_name), 'r')) as unziped_plugin:
                for child_plugin in self._dependencies_from_list(unziped_plugin.open('META-INF/MANIFEST.MF').read()):
                    self._download_plugin(child_plugin)

    def _plugin_url(self, plugin_name):
        return os.path.join(self.param_list['update_url'], plugin_name + '.hpi')

    def _path_to_plugin(self, plugin_name):
        return os.path.join(self.param_list['dest'], plugin_name + '.hpi')

    def _dependencies_from_list(self, lines):

        dep_match = re.search('Plugin-Dependencies:\s(.*\n(\s.*\n)*)', lines)

        if dep_match:
            one_line_dependecies = ''.join([x.strip() for x in dep_match.group(1).split()])
            return [el.split(':')[0] for el in one_line_dependecies.split(',')]
        else:
            return []

def main():

    module = AnsibleModule(
        argument_spec=dict(
            name       = dict(require=True, type='list'),
            update_url = dict(require=True),
            dest       = dict(require=True, type='path')
        )
    )

    jenkins_plugin = JenkinsPlugin(module.params)
    module.exit_json(**jenkins_plugin.get_plugin())

if __name__ == '__main__':
    main()
