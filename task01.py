# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 16:49
# @Author  : Hehang
# @Email   : 2937630572@qq.com
# @File    : task01.py
# @Software: PyCharm
import sqlite3

# 创建规则库
def createRuleBase():
   cursor.execute('CREATE TABLE IF NOT EXISTS rule(name text, assumption text, conclusion text)')
   connect.commit()
   print("规则数据库初始化完成...")

# 增加规则
def addRuleBase(ruleName, ruleAssumption, ruleConclusion):
    cursor.execute("INSERT INTO rule(name, assumption, conclusion)VALUES ('%s', '%s', '%s')" % (ruleName, ruleAssumption, ruleConclusion))
    connect.commit()
    print("规则" + ruleName + "添加成功！")

# 删除规则
def deleteRuleBase(ruleName):
    cursor.execute("DELETE  FROM rule WHERE name='%s'" % ruleName)
    connect.commit()
    print(ruleName+"删除规则成功")

# 修改规则
def updateRuleBase(ruleName, ruleAssumption, ruleConclusion):
    cursor.execute("UPDATE rule set assumption='%s', conclusion='%s' WHERE name='%s'" % (ruleAssumption, ruleConclusion, ruleName))
    connect.commit()
    print("规则" + ruleName + "修改成功！")

# 查看规则
def showRuleBase():
    cursor.execute("SELECT * FROM rule")
    result = cursor.fetchall()
    if result == []:
        print("规则数据库为空...")
    else:
        print(result)

# 创建综合数据库
def createDataBase():
    cursor.execute('CREATE TABLE IF NOT EXISTS data(id int, content text)')
    connect.commit()
    print("综合数据库初始化完成...")

# 增加数据
def addDataBase(content):
    id = len(cursor.fetchall())
    cursor.execute("INSERT INTO data(id, content)VALUES ('%d', '%s')" % (id, content))
    connect.commit()
    print(content + "增加成功!")

# 删除数据
def deleteDataBase(id):
    cursor.execute("DELETE  FROM data WHERE id='%d'" % id)
    connect.commit()
    print(str(id) + "删除成功")

# 更新数据
def updateDataBase(id, content):
    cursor.execute("UPDATE data set content='%s' WHERE id='%d'" % (content, id))
    connect.commit()
    print(str(id) + "修改成功!")

# 查看数据
def showDataBase():
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    print(result)

def addRules():
    ruleName = input("【请输入规则名】：\n")
    ruleFirst = input("【请输入规则的假设】：\n")
    ruleSecond = input("【请输入规则的假设】：\n")
    addRuleBase(ruleName, ruleFirst, ruleSecond)

def delRules():
    ruleName = input("【请输入要删除的规则名】：\n")
    deleteRuleBase(ruleName)

def updateRules():
    rule = []
    ruleName = input("【请输入要修改的规则名】：\n")
    ruleFirst = input("【请输入规则的假设】：\n")
    ruleSecond = input("【请输入规则的假设】：\n")
    updateRuleBase(ruleName, ruleFirst, ruleSecond)

def showRules():
    showRuleBase()

def addData():
    i = input("请输入要添加到综合数据库中的数据：\n")
    addDataBase(i)

def delData():
    i = int(input("【请输入要删除的数据编号】：\n"))
    deleteDataBase(i)


def updateData():
    i = int(input("【请输入要修改的数据编号】：\n"))
    s = input("请输入要修改并添加到综合数据库中的数据：\n")
    updateDataBase(i, s)


def showData():
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    if result == []:
        print("综合数据库为空...")
    else:
        print(result)


def info():
    print("* * * * * * * * * * * * *")
    print("* 1.    【添加规则】     *")
    print("* 2.    【删除规则】     *")
    print("* 3.    【修改规则】     *")
    print("* 4.    【查看规则】     *")
    print("* 5.【添加综合数据库数据】*")
    print("* 6.【删除综合数据库数据】*")
    print("* 7.【修改综合数据库数据】*")
    print("* 8.【查看综合数据库数据】*")
    print("* 9.【本地文本中添加规则】*")
    print("* 0.   【退       出】   *")
    print("* * * * * * * * * * * * *")
    print("【请选择要执行的操作】：")

def end():
    cursor.close()
    connect.close()
    print("程序退出结束...")
    exit()

def readRules():
    fileName = input("请输入需要规则读取文件的名称：\n")
    fo = open(fileName, 'r', encoding='utf-8')
    lines = fo.readlines()
    for line in lines:
        item = line.strip('\n').split(' ')
        ruleName = item[0]
        ruleAssumption = "".join(item[2:item.index('THEN')])
        ruleConclusion = item[-1]
        # print(ruleName, ruleAssumption, ruleConclusion)
        addRuleBase(ruleName, ruleAssumption, ruleConclusion)

if __name__ == "__main__":
    connect = sqlite3.connect('./ruleBase.db')
    cursor = connect.cursor()
    createRuleBase()
    createDataBase()
    while True:
        info()
        s = int(input())
        if s == 1:
            addRules()
        elif s == 2:
            delRules()
        elif s == 3:
            updateRules()
        elif s == 4:
            showRules()
        elif s == 5:
            addData()
        elif s == 6:
            delData()
        elif s == 7:
            updateData()
        elif s == 8:
            showData()
        elif s == 9:
            readRules()
        else:
            end()