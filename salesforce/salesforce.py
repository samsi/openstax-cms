from simple_salesforce import Salesforce as SimpleSalesforce
from django.conf import settings
from contextlib import ContextDecorator
from django.contrib.sessions.backends.db import SessionStore
from django.conf import settings


class Salesforce(SimpleSalesforce, ContextDecorator):
    _default_session_key = 0

    def __init__(self, *args, **kwargs):
        session_store = SessionStore(session_key=self._default_session_key)
        if 'sf_instance' in session_store.keys() and 'sf_session_id' in session_store.keys():
            try:
                super(Salesforce, self).__init__(instance=session_store['sf_instance'],
                                                 session_id=session_store['sf_session_id'])
            except:
                raise RuntimeError("salesforce session failed")
        else:
            try:
                super(Salesforce, self).__init__(**settings.SALESFORCE)
            except AttributeError:
                super(Salesforce, self).__init__(*args, **kwargs)
            except TypeError:
                raise RuntimeError("salesforce init failed")
            session_store['sf_instance'] = self.sf_instance
            session_store['sf_session_id'] = self.session_id
            session_store.save()
            self.update_session_key(session_store.session_key)

    @classmethod
    def update_session_key(cls, key):
        cls._default_session_key = key

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        if not exc == (None, None, None):
            session_store = SessionStore(session_key=self._default_session_key)
            session_store.delete()
            self.update_session_key(None)
        return False

    def faculty_status(self, accounts_id=None):
        """Return a list of confirmed accounts ids from salesforce.  If the
        parameter is 'None', then all confirmed faculty will be returned.
        """
        if accounts_id is None:
            command = "SELECT Accounts_ID__c FROM Contact WHERE Faculty_Verified__c = 'Confirmed' AND Accounts_ID__c != null"
        else:
            command = "SELECT Accounts_ID__c FROM Contact WHERE Faculty_Verified__c = 'Confirmed' AND Accounts_ID__c = '{}'".format(
                accounts_id)
        response = self.query(command)
        faculty_list = response['records']
        while 'nextRecordsUrl' in response.keys():
            response = self.query_more(response['nextRecordsUrl'], True)
            faculty_list = faculty_list + response['records']
        faculty_list = [contact['Accounts_ID__c'] for contact in faculty_list]
        return faculty_list

    def adopters(self):
        """Return a list of adopters from salesforce"""
        # Field 'Id' is generated by salesforce
        command = "SELECT Id, Name, Description, Website FROM Account WHERE Number_of_Adoptions__c > 0"
        response = self.query(command)
        adopters_list = response['records']
        while 'nextRecordsUrl' in response.keys():
            response = self.query_more(response['nextRecordsUrl'], True)
            adopters_list = adopters_list + response['records']
        return adopters_list

