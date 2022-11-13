import logging

from camply.config import RIDBConfig
from camply.containers.api_responses import CampsiteResponse
from camply.providers.recreation_dot_gov.recdotgov_provider import RecreationDotGovBase

logger = logging.getLogger(__name__)


class RecreationDotGov(RecreationDotGovBase):
    facility_type = RIDBConfig.CAMPGROUND_FACILITY_FIELD_QUALIFIER
    resource_api_path = RIDBConfig.CAMPSITE_API_PATH
    activity_name = "CAMPING"
    api_response_class = CampsiteResponse
