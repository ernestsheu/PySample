''' This is test '''
# -*- coding: utf8 -*-
# coding: utf8
import logging
import traceback

#===============================================================================
# try:
#     import cupy as nnp
#     _GPU_NUMPY = True
#     print('CUDA numpy enabled.')
# except:
#     import numpy as nnp
#     _GPU_NUMPY = False
#     print('CPU numpy enabled.')
#===============================================================================
import numpy as nnp

_GPU_NUMPY = False

class EnvironDetect(object):
    ''' Which operating environment to detect '''

    @property
    def var1(self):
        return self.__nnp

    @property
    def var2(self):
        return _GPU_NUMPY

    def __init__(self, tag = 'Evn', environ = 'auto'):
        self.__unused = False
        self.__used = tag

    def _tag(self, msg):
        abc = self.__used
        return '[%s] %s' % (self.__tag, msg)

    def func1(qwe, ert, yui, *args, **kwargs):
        def _test(aaa, bbb):
            pass
        
        _test(qwe, ert)
        

    def loginfo(self, msg, *args, **kwargs):
        abc = 111
        xyz = True
        dict_a = {'abcedfg': 1234, 'xyz': 'abcdf'}
        list_a = ['abc ddfgeg', 'xyz']
        
        list_a[0] = 'qwert'
        dict_a['xyz'] = 1111
        
        self.func1(dict_a['xyz'], list_a[0], dict_a[list_a[1]])


if __name__ == '__main__':
  run_main()
