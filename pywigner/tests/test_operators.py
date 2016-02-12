import openpathsampling as paths
import pywigner as lsc
import dynamiq_engine as dynq
import numpy as np
from pywigner.operators import *


from nose.tools import (
    raises, assert_equal, assert_almost_equal, assert_not_equal
)
from nose.plugins.skip import SkipTest

class OperatorTester(object):
    def __init__(self):
        topology = paths.ToyTopology(n_atoms=2, n_spatial=3, 
                                     masses=np.array([1.5, 2.5]), pes=None)
        self.previous_trajectory = [
            dynq.Snapshot(
                coordinates=np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]),
                momenta=np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]),
                topology=topology
            ),
            dynq.Snapshot(
                coordinates=np.array([[0.1, 0.0, 0.0], [0.0, 0.0, 0.0]]),
                momenta=np.array([[0.1, 0.0, 0.0], [0.0, 0.0, 0.0]]),
                topology=topology)
        ]


class testOperator(OperatorTester):
    def setup(self):
        self.op = Operator()

    @raises(NotImplementedError)
    def test_sample_initial_conditions(self):
        self.op.sample_initial_conditions(self.previous_trajectory)

    @raises(NotImplementedError)
    def test_correction(self):
        self.op.correction(self.previous_trajectory[0])

    @raises(NotImplementedError)
    def test_call(self):
        self.op.sample_initial_conditions(self.previous_trajectory[0])

class testCoherentProjection(OperatorTester):
    def setup(self):
        topology = paths.ToyTopology(n_atoms=2, n_spatial=3, 
                                     masses=np.array([1.5, 2.5]), pes=None)
        snap0 = paths.Snapshot(
            coordinates=np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
            velocities=np.array([[-0.5, 0.25, 0.25], [0.1, 0.0, -0.1]]),
            topology=topology
        )
        p0 = [vel * mass
              for (vel, mass) in zip(snap0.velocities, snap0.topology.masses)]
        self.op = CoherentProjection(
            x0=snap0.coordinates,
            p0=np.array(p0),
            gamma=np.array([[4.0, 4.0, 4.0], [2.0, 2.0, 2.0]])
        )

    def test_initialization(self):
        raise SkipTest
    
    def test_sample_initial_conditions(self):
        # not much we can do here except check that the resulting snapshot
        # exists and has the right number of attributes
        #snap = self.op.sample_initial_conditions(self.previous_trajectory)
        raise SkipTest

    def test_correction(self):
        assert_equal(self.op.correction(self.previous_trajectory[0]), 1.0)

    def test_call(self):
        raise SkipTest



