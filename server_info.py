#!/usr/bin/env python
# Created by Scott Stephenson
# Prints to STDOUT in CSV format
# Use Excel, Google Spreadsheet, or other spreadsheet program to view, sort, etc
# Usage: sysinfo.py <ssh-key> <server1> <server2> ...

import subprocess
import sys

ssh_key_filename = sys.argv[1]
user_with_hostnames = sys.argv[2:]
hostnames = []

release_version_cmd = 'lsb_release -r'
dns_search_path_cmd = "grep search /etc/resolv.conf"
updates_cmd = '/usr/lib/update-notifier/apt-check 2>&1'
output = {}

def initialize(user_with_hostnames):
    for user_with_hostname in user_with_hostnames:
        user, hostname = user_with_hostname.split('@')
        output[hostname] = {}
        output[hostname]['user'] = user
        hostnames.append(hostname)
    return output

def get_versions(hostnames, full_cmd):
  counter = 0
  for host in hostnames:
    user = output[host]['user']
    ssh_cmd = "ssh -i %s %s@%s %s" % (ssh_key_filename, user, host, full_cmd)
    version_long = subprocess.check_output(ssh_cmd, shell=True)
    header, version = version_long.split()
    output[host]['version'] = version
  return output

def get_available_updates(hostnames, full_cmd):
  for host in hostnames:
    user = output[host]['user']
    ssh_cmd = "ssh -i %s %s@%s %s" % (ssh_key_filename, user, host, full_cmd)
    updates = subprocess.check_output(ssh_cmd, shell=True)
    if updates == '0;0':
      output[host]['available_updates'] = "NO UPDATES AVAILABLE"
    else:
      output[host]['available_updates']= "UPDATES AVAILABLE"
  return output

def get_dns_search_path(hostnames, full_cmd):
  for host in hostnames:
    user = output[host]['user']
    ssh_cmd = "ssh -i %s %s@%s %s" % (ssh_key_filename, user, host, full_cmd)
    unparsed = subprocess.check_output(ssh_cmd, shell=True)
    tmp = unparsed.split()
    value = tmp[1]
    output[host]['dns_search_path'] = value
  return output

def print_report(output):
  print "HOST, UBUNTU VERSION, UPDATES, DNS SEARCH PATH"
  for host in hostnames:
    print "%s, %s, %s, %s" % (host, output[host]['version'], output[host]['available_updates'], output[host]['dns_search_path'])
  return True


if __name__ == "__main__":
  initialize(user_with_hostnames)
  get_versions(hostnames, release_version_cmd)
  get_available_updates(hostnames, updates_cmd)
  get_dns_search_path(hostnames, dns_search_path_cmd)
  print_report(output)
