import math



## Import tutorial custom function ##

from  import Hashfunction as custom_RSHash

from  import JSHash as custom_JSHash

from  import ELFHash as custom_ELFHash

from  import BKDHash as custom_BKDHash

from  import SDBMHash as custom_SDBMHash

from  import DJBHash as custom_DJBHash

from  import DKEHash as custom_DKEHash

from zeng_qidong.ZENG_Qidong.APHash import APHash as custom_APHash

if __name__ == '__main__':

  nums = 'qwertyuiopasdfghjklzxcvbnm'


  ## RSHash function ##

  x = custom_RSHash.RSHash(nums)

  assert math.isclose(x, 900485739), "RSHash function does not work correctly"


  ## JSHash function ##

  x = custom_JSHash(nums)

  assert math.isclose(x, 787808349), "JSHash function does not work correctly"


  ## ELFHash function ##

  x = custom_ELFHash(x)

  assert math.isclose(x, 148675701), "ELFHash function does not work correctly"


  ## BKDRHash function ##

  xx =custom_BKDRHash(x)

  assert math.isclose(x, 113), "BKDRHash function does not work correctly"


  ## SDBMHash function ##

  x = custom_SDBMHash(x)

  assert math.isclose(x, 113), "SDBMHash function does not work correctly"


  ## DJBHash function ##

  x = custom_DJBHash(x)

  assert math.isclose(x, 177686), "DJBHash function does not work correctly"


  ## DEKHash function ##

  x = custom_DEKHash(x)

  assert math.isclose(x, 817), "DEKHash function does not work correctly"


  ## APHash function ##

  # x = custom_APHash(x)

  # assert math.isclose(x, 2147252218), "APHash function does not work correctly"


  

  print("All functions work correctly!")

