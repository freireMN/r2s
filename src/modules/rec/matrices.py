import scipy.sparse as spa


class R2S_coo():

    _row = None
    _col = None
    _data = None
    _datatype = None

    def __init__(self, row, col, data, datatype):
        self._row = row
        self._col = col
        self._data = data
        self._datatype = datatype 

    def load_coo(self, source):
        _mtrow = source[self._row].values
        _mtcol = source[self._col].values
        _mtdata = source[self._data].values.astype(self._datatype)
        print('Setting a sparse matrix of ratings (rows {} and columns {})  '.format(len(_mtrow),len(_mtcol)))

        return spa.coo_matrix((_mtdata, (_mtrow, _mtcol)))


