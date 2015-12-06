# -*- coding: utf-8 -*-

###############################################################################
#
# SetOnce
# Sets the properties of a profile, but will not overwrite existing properties.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SetOnce(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetOnce Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetOnce, self).__init__(temboo_session, '/Library/Mixpanel/Profiles/SetOnce')


    def new_input_set(self):
        return SetOnceInputSet()

    def _make_result_set(self, result, path):
        return SetOnceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetOnceChoreographyExecution(session, exec_id, path)

class SetOnceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetOnce
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DistinctID(self, value):
        """
        Set the value of the DistinctID input for this Choreo. ((required, string) Used to uniquely identify the profile you want to update.)
        """
        super(SetOnceInputSet, self)._set_input('DistinctID', value)
    def set_IP(self, value):
        """
        Set the value of the IP input for this Choreo. ((optional, string) An IP address string associated with the profile (e.g., 127.0.0.1). When set to 0 (the default) Mixpanel will ignore IP information.)
        """
        super(SetOnceInputSet, self)._set_input('IP', value)
    def set_IgnoreTime(self, value):
        """
        Set the value of the IgnoreTime input for this Choreo. ((optional, boolean) When set to true, Mixpanel will not automatically update the "Last Seen" property of the profile. Otherwise, Mixpanel will add a "Last Seen" property associated with any set, append, or add requests.)
        """
        super(SetOnceInputSet, self)._set_input('IgnoreTime', value)
    def set_ProfileProperties(self, value):
        """
        Set the value of the ProfileProperties input for this Choreo. ((conditional, json) A JSON object containing names and values of custom profile properties. Note that properties existing already will not be overwritten.)
        """
        super(SetOnceInputSet, self)._set_input('ProfileProperties', value)
    def set_Time(self, value):
        """
        Set the value of the Time input for this Choreo. ((optional, date) A unix timestamp representing the time of the profile update. If not provided, Mixpanel will use the time the update arrives at the server.)
        """
        super(SetOnceInputSet, self)._set_input('Time', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The token provided by Mixpanel. You can find your Mixpanel token in the project settings dialog in the Mixpanel app.)
        """
        super(SetOnceInputSet, self)._set_input('Token', value)
    def set_Verbose(self, value):
        """
        Set the value of the Verbose input for this Choreo. ((optional, boolean) When set to 1, the response will contain more information describing the success or failure of the tracking call.)
        """
        super(SetOnceInputSet, self)._set_input('Verbose', value)

class SetOnceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetOnce Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class SetOnceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetOnceResultSet(response, path)
