from nearest_square import nearestPerfectSquare

def test_nearest_square_5():
    assert(nearestPerfectSquare(5)==4)
def test_nearest_square_n12():
    assert(nearestPerfectSquare(-12)==0)
def test_nearest_square_9():
    assert(nearestPerfectSquare(9)==9)
def test_nearest_square_23():
    assert(nearestPerfectSquare(23)==16)
