# 导入带有模块的包时注意事项
import package1
import calc
# 使用 import 方式进行导入时，只能跟包名或模块名

from package1 import moduleA
from package1.moduleA import a
# 使用 from...import 可以导入包、模块、函数、变量
