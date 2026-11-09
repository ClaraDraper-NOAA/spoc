#!/usr/bin/env python3
import os

import numpy as np

import bufr
from bufr.obs_builder import add_main_functions
from prepbufr_obs_builder import PrepbufrObsBuilder, map_path


MAPPING_PATH = map_path('prepbufr_proflr.yaml')


class ProflrPrepbufrObsBuilder(PrepbufrObsBuilder):
    def __init__(self):
        super().__init__(MAPPING_PATH, log_name=os.path.basename(__file__))

    def make_obs(self, comm, input_path):
        """
        Create the ioda wind profiler prepbufr observations.

        Parameters
        ----------
        comm: object
                The communicator object (e.g., MPI)
        input_path: str
                The input bufr file
        """
        container = super().make_obs(comm, input_path)
        self._replace_timestamp(container, self._get_reference_time(input_path))
        return container


add_main_functions(ProflrPrepbufrObsBuilder)
