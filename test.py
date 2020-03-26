import model 

def test():
    assert 2 > 1

def test_dk(): 
    m=model.Model()
    assert m.dk(0.1,0.1) == (0.1,0)


def test_dk(): 
    m=model.Model()
    assert m.dk(0.5,0.5) == (0.5,0)

def test_dk(): 
    m=model.Model()
    assert m.dk(0.32,0.17) == (0.245,0.075)


def test_dk(): 
    m=model.Model()
    assert m.dk(0.75,0.75) == (0.75,0)




def test_ik(): 
    m=model.Model()
    assert m.ik(10,0) == (10,10)

def test_ik(): 
    m=model.Model()
    assert m.ik(0.75,0) == (0.75,0.75)

def test_ik(): 
    m=model.Model()
    assert m.ik(0.245,0.075) == (0.32,0.17)

def test_ik(): 
    m=model.Model()
    assert m.ik(0.5,0) == (0.5,0.5)

def test_update():
      m=model.Model()
      m.m1.speed = 25
      m.m2.speed = 25
      m.update(1/25)
    assert (m.x, m.y) == (1,0)