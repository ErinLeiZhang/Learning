# -*- coding: utf-8 -*-

import jenkins
import urllib2
import xml.etree.ElementTree as ET
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build

url = 'http://jenkins.shishike.com/jenkins/'
username = 'onstore'
password = 'pass4you'
job_name = ['store/automation',
            'store/master-store-crm-build',
            'store/store-hrm-build',
            ]

class jenkins_tools():

    def __init__(self):
        pass

    def login_jenkins(self):
        url = 'http://jenkins.test.com/jenkins/'
        username = 'username'
        password = 'password'
        job_name = 'store/automation'
        self.server = jenkins.Jenkins(url, username, password)

    def get_jenkins_version(self):
        return self.server.get_version()

    def get_branch_name(self, job_name):

        my_job = self.server.get_job_config(job_name)
        my_job = str(my_job.encode('utf-8'))
        root = ET.fromstring(my_job)

        ele = root.findall('.//branches/hudson.plugins.git.BranchSpec/name')

        for e in ele:
            return e.text

    def get_all_jobs(self):
        all_jobs_li = self.server.get_all_jobs()
        for item in all_jobs_li:
            print ('name: %s' % item['name'], 'URL: ', item['url'])

    def get_jobs(self, job_name):
        print self.server.get_job_name(job_name)

    def get_count(self):
        result_xml = urllib2.urlopen('http://jenkins.test.com/jenkins/job/automation/139/api/python?pretty=true')
        print result_xml

test = jenkins_tools()
test.login_jenkins()
test.get_count()




