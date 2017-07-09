import unittest
from algorithm import mutate
from algorithm import crossover
from algorithm import fitnessFuntion


def myrandInt1(minLen, maxLen):
    return 0


def myrandInt2(minLen, maxLen):
    return maxLen


def myrandInt3(minLen, maxLen):
    return maxLen / 2


def myrandIntRobust(minLen, maxLen):
    return maxLen / 3


def myrand():
    return 1


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_noMutation(self):
        chromosome = mutate([1, 1, 0], 0, myrand)
        self.assertEqual([1, 1, 0], chromosome)

    def test_mutationPositive(self):
        chromosome = mutate([1, 1, 0], 1, myrand)
        self.assertEqual([0, 0, 1], chromosome)

    def test_nocrossOver(self):
        chromosomeA = [1, 1, 1, 1]
        chromosomeB = [0, 0, 0, 0]
        (newChromosomeA, newChromosomeB) = crossover(chromosomeA, chromosomeB, 0, myrand, myrandInt1)
        self.assertEqual(newChromosomeA, chromosomeA)
        self.assertEqual(newChromosomeB, chromosomeB)

    def test_crossoverLen0(self):
        chromosomeA = [1, 1, 1, 1]
        chromosomeB = [0, 0, 0, 0]
        (newChromosomeA, newChromosomeB) = crossover(chromosomeA, chromosomeB, 1, myrand, myrandInt1)
        self.assertEqual(newChromosomeA, chromosomeB)
        self.assertEqual(newChromosomeB, chromosomeA)

    def test_crossoverLenN(self):
        chromosomeA = [1, 1, 1, 1]
        chromosomeB = [0, 0, 0, 0]
        (newChromosomeA, newChromosomeB) = crossover(chromosomeA, chromosomeB, 1, myrand, myrandInt2)
        self.assertEqual(newChromosomeA, chromosomeA)
        self.assertEqual(newChromosomeB, chromosomeB)

    def test_crossoverMiddle(self):
        chromosomeA = [1, 1, 1, 1]
        chromosomeB = [0, 0, 0, 0]
        expectedChromosomeA = [1, 1, 0, 0]
        expectedChromosomeB = [0, 0, 1, 1]
        (newChromosomeA, newChromosomeB) = crossover(chromosomeA, chromosomeB, 1, myrand, myrandInt3)
        self.assertEqual(expectedChromosomeA, newChromosomeA)
        self.assertEqual(expectedChromosomeB, newChromosomeB)

    def test_crossoverMiddleChars(self):
        chromosomeA = ['a', 'b', 'c', 'd']
        chromosomeB = ['e', 'f', 'g', 'h']
        expectedChromosomeA = ['a', 'b', 'g', 'h']
        expectedChromosomeB = ['e', 'f', 'c', 'd']
        (newChromosomeA, newChromosomeB) = crossover(chromosomeA, chromosomeB, 1, myrand, myrandInt3)
        self.assertEqual(expectedChromosomeA, newChromosomeA)
        self.assertEqual(expectedChromosomeB, newChromosomeB)

    def test_crossoverRobust(self):
        chromosomeA = [1, 1, 0, 1, 0, 1, 0, 1, 0]
        chromosomeB = [0, 0, 0, 0, 1, 0, 1, 1, 0]
        expectedChromosomeA = [1, 1, 0, 0, 1, 0, 1, 1, 0]
        expectedChromosomeB = [0, 0, 0, 1, 0, 1, 0, 1, 0]
        (newChromosomeA, newChromosomeB) = crossover(chromosomeA, chromosomeB, 1, myrand, myrandIntRobust)
        self.assertEqual(expectedChromosomeA, newChromosomeA)
        self.assertEqual(expectedChromosomeB, newChromosomeB)

    def test_fitnessFuntion(self):
        chromosomeA = [1, 1, 0, 1, 0, 1, 0, 1, 0]
        chromosomeB = [0, 0, 0, 0, 1, 0, 1, 1, 0]
        expectedChromosomeA = [1, 1, 0, 0, 1, 0, 1, 1, 0]
        expectedChromosomeB = [0, 0, 0, 1, 0, 1, 0, 1, 0]
        self.assertEqual(5, fitnessFuntion(chromosomeA))
        self.assertEqual(3, fitnessFuntion(chromosomeB))
        self.assertEqual(5, fitnessFuntion(expectedChromosomeA))
        self.assertEqual(3, fitnessFuntion(expectedChromosomeB))


if __name__ == '__main__':
    unittest.main()
