#!/usr/bin/env python3
"""
    Representation of problem used by LEAP individuals
"""
from collections import namedtuple

from leap_ec.representation import Representation
from leap_ec.individual import RobustIndividual
from leap_ec.decoder import Decoder
from leap_ec.int_rep.initializers import create_int_vector
from leap_ec.real_rep.initializers import create_real_vector

from individual import MNISTIndividual

# We could have used plain ole tuples, but namedtuples add a little more self-
# documentation to the code since now we can refer to individual genes by name.
MNISTPhenotype = namedtuple('MNISTPhenotype',
                            ['digit'])


class MNISTDecoder(Decoder):
    """ Responsible for decoding from genome to phenome for evals """
    def __init__(self):
        super().__init__()

    def decode(self, genome, *args, **kwargs):
        """ decode the given individual

        :returns: named tuple of phenotypic traits
        """
        phenome = MNISTPhenotype(digit=genome[0])

        return phenome


class MNISTRepresentation(Representation):
    """ Encapsulates MNIST internals
    """
    # This says we have one gene that's an integer in the range [0,9].
    genome_bounds = MNISTPhenotype(digit=(0,9))

    def __init__(self):
        super().__init__(
            initialize=create_int_vector(MNISTRepresentation.genome_bounds),
            decoder=MNISTDecoder(),
            individual_cls=MNISTIndividual)
