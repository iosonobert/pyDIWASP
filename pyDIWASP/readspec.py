import numpy as np

def readspec(filename, funit='hz', dunit='cart'):
    """
    Read a DIWASP spec file
    
    Translated from Matlab by by Andrew
    """
    
    print('in')
    with open(filename) as f:
        print('open')

        datain = f.readlines()
    print('read')

    datain = [float(x.split()[0]) for x in datain]
    datain = np.array(datain)
    
    print('comprehended')
    
    SM = {}
    SM['xaxisdir'] = datain[0]
    
    nfreq=int(datain[1])
    ndirs=int(datain[2])
    
    SM['freqs'] = datain[np.arange(3, nfreq+3)]
    SM['funit'] = funit

    SM['dirs'] = datain[np.arange(nfreq+3, nfreq+3+ndirs)]
    SM['dunit'] = dunit

    headercheck=datain[nfreq+ndirs+3];
    if headercheck!=999:
       raise(Exception('corrupt file header'))
    
    mat=datain[np.arange(nfreq+ndirs+4, nfreq+ndirs+4+(nfreq*ndirs))];
    S = np.reshape(mat, [nfreq, ndirs])
    SM['S'] = S
    
    return SM
