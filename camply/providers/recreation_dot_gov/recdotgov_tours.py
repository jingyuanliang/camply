import logging

from camply.config import RIDBConfig
from camply.containers.api_responses import TourResponse
from camply.providers.recreation_dot_gov.recdotgov_provider import RecreationDotGovBase

logger = logging.getLogger(__name__)


class RecreationDotGovTours(RecreationDotGovBase):
    resource_api_path = RIDBConfig.TOUR_API_PATH
    api_response_class = TourResponse


class RecreationDotGovTicket(RecreationDotGovTours):
    facility_type = RIDBConfig.TICKET_FACILITY_FIELD_QUALIFIER


class RecreationDotGovTimedEntry(RecreationDotGovTours):
    facility_type = RIDBConfig.TIMED_ENTRY_FACILITY_FIELD_QUALIFIER
