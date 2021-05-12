# import module -> module.object, module.func()
# import module as m
# from module import x -> x
# from . import module 优先本地，否则优先基础包
# modname = "string"
# exec("import "+modname)
#
# reload ====================================================
# from imp import reload
# reload(module) #不会递归的reload所有模块
#
# 屏蔽变量 ====================================================
# _X # from* 无法导入此变量
# __all__ = [X,Y,Z] # from* 只能导入这些变量
#
# main ======================================================
# if __name__ == '__main__':
#   print('I am running')    # only when run not when imported
#
# 修改path搜索路径 =============================================
# import sys
# sys.path.append('C:\\sourcedir') # 临时修改path
#
# metaprogram ================================================
# M.name
# M.__dict__['name']
# sys.modules['M'].name
# getattr(M,'name')