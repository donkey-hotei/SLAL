"""
Applications of SLAL
Perspective Rectification

The goal of this application is to remove perspective from the image.


"""

    
def move2board(y):
    """
    input:-> a {'y1', 'y2', 'y3'}-vector y, the coordinate representation
           of a point q in whiteboard coordinates
    output:-> a {'y1', 'y2', 'y3'}-vector z, the coordinate representation
             of the point q in camera coordinates
    """
    return Vector({'y1', 'y2', 'y3'},
                  {'y1':y['y1']/y['y3'], 
                   'y2':y['y2']/y['y3'], 
                   'y3':y['y3']/y['y3']}
                   
                   

def make_equations(x1, x2, w1, w2):
    """
    input:-> points (x1, x1) and (w1, w2)
    output:-> a list [ u, v ] such that u*h=0 and v*h=0
    """
    domain { (a, b) for a in {'x1', 'x2', 'x3'} for b in {'y1','y2','y3'} }
    u = Vector( domain, {('y3','x1'): w1*x1,
                         ('y3','x2'): w1*x2,
                         ('y3','x3'): w1
                         ('y1','x1'):-w1
                         ('y1','x2'):-x2
                         ('y1','x3'):-1
                         })
    v = Vector( domain, {('y3','x1'): w2*x1,
                         ('y3','x2'): x2*x2,
                         ('y2','x3'): w2,
                         ('y2','x1'):-x1,
                         ('y2','x2'):-x2
                         ('y2','x3'):-1
                         })
    return [u, v]
