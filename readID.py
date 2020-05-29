import numpy as np

def readID(filename):
    """
    Read ID file

    %  Format
        % 
        % n
        % m (number of data types)
        % depth
        % fs
        % xyz
        % next 3 lines are the xyz row by row
        % /xyz
        % layout
        % next 3 lines are the layout row by row
        % /layout
        % type1
        % next n lines are data type 1
        % type2
        % next n lines are data type 2
        % type3
        % next n lines are data type 3
        % etc

    by Andrew
    """
    
    with open(filename) as f:

        n = int(float(f.readline().split()[0]))
        m = int(float(f.readline().split()[0]))
        depth = int(float(f.readline().split()[0]))
        fs = int(float(f.readline().split()[0]))
        
        # f.readline()
        # l1 = [float(x) for x in f.readline().split()]
        # l2 = [float(x) for x in f.readline().split()]
        # l3 = [float(x) for x in f.readline().split()]
        # xyz = np.array([l1, l2, l3])        
        # f.readline()
        
        print(f.readline())
        l1 = [float(x) for x in f.readline().split()]
        l2 = [float(x) for x in f.readline().split()]
        l3 = [float(x) for x in f.readline().split()]
        layout = np.array([l1, l2, l3])        
        print(f.readline())
        
        datatypes = []
        data = []
        for i in np.arange(0, m):
            datatypes.append(f.readline())
            print(datatypes)
            data.append([float(f.readline().split()[0]) for i in np.arange(0, n)])

        
    ID = {}
    ID['n'] = n
    ID['m'] = m

    ID['depth'] = depth
    ID['fs'] = fs

    # ID['xyz'] = xyz
    ID['layout'] = layout

    ID['datatypes'] = datatypes
    ID['data'] = np.array(data).T

    return ID
    