"""
Applications of SLAL
Perspective Rectification
by dynsne


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
