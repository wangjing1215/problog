# -*- coding: utf-8 -*-
def parsex(la):
    j=1
    temp = ''
    lasts = ''
    for i in la:
        temp = temp+i
        if j % 2 == 0:
            lasts = lasts+str(int(temp, 16))
            temp = ''
        j=j+1
    return  lasts
def timeparsex(la):
    j=1
    temp = ''
    lasts = ''
    for i in la:
        temp = temp+i
        if j  == 2:
            lasts = lasts+str(int(temp, 16))+'年'
            temp = ''
        if j  == 4:
            lasts = lasts+str(int(temp, 16))+'月'
            temp = ''
        if j  == 6:
            lasts = lasts+str(int(temp, 16))+'日 '
            temp = ''
        if j  == 8:
            lasts = lasts+str(int(temp, 16))+'h:'
            temp = ''
        if j  == 10:
            lasts = lasts+str(int(temp, 16))+'m:'
            temp = ''
        if j  == 12:
            lasts = lasts+str(int(temp, 16))+'s'
        j=j+1
    return  lasts
# 绑定/解绑
def lockorunlock1(ordata):
    print '绑定/解绑'
    orderid=ordata[56:58]
    orderid_ex = ''
    if orderid == '55':
        orderid_ex = '0x55: 绑定'
    elif orderid == 'AA':
        orderid_ex = '0xAA: 解绑'
    print '唯一识别码: ' + parsex(ordata[4:38])
    print 'time: ' + timeparsex(ordata[44:56])
    print '命令ID为：' + orderid_ex
    if len(ordata) > 98:
        print 'SIM卡 ICCID号: '+parsex(ordata[58:98])
    if len(ordata) > 106:
        print '终端ID: '+parsex(ordata[98:106])
    if len(ordata) > 140:
        print 'VIN: '+parsex(ordata[106:140])
    if len(ordata) > 180:
        print '平台编号: '+parsex(ordata[140:180])
    if len(ordata) > 184:
            print 'ECU 类型: '+parsex(ordata[180:184])
    if parsex(ordata[106:140])==parsex(ordata[4:38]):
        print '解析成功，唯一标识码与VIN码一致'
    else:
        print '唯一标识码与VIN码不一致，请检查包是否有误'
# 绑定/解绑 结果应答
def lockorunlock2(ordata):
    print '# 绑定/解绑 结果应答'
    orderid = ordata[56:58]
    # 命令ID
    orderid_ex = ''
    if orderid == '55':
        orderid_ex = '0x55: 绑定'
    elif orderid == 'AA':
        orderid_ex = '0xAA: 解绑'
    # 当前状态
    f1 = ordata[184:186]
    print f1
    f1_dict={'00':'绑定','01':'未绑定'}
    if f1 in f1_dict.keys():
        f1_ex = f1_dict[f1]
    else:
        f1_ex = '未匹配'
    # 指令是否成功执行
    f2 = ordata[186:188]
    f2_dict = {'00': '成功', '01': '失败'}
    if f2 in f2_dict.keys():
        f2_ex = f2_dict[f2]
    else:
        f2_ex = '未匹配'
    # 失败原ying
    f3 = ordata[188:190]
    f3_dict = {'00': '未失败', '01': '参数失误','02': '超时', '03': '命令ID错误','04':'ECU故障','05': '设备与ECU已绑定',
               '06': 'TBOX已激活','07': 'ECU已激活','08': '设备未激活', '09': 'ECU未激活', '10': 'ECU握手失败'}
    if f3 in f3_dict.keys():
        f3_ex = f3_dict[f3]
    else:
        f3_ex = '未匹配'
    print 'VIN: ' + parsex(ordata[4:38])
    print 'time: ' + timeparsex(ordata[44:56])
    print '命令ID为：' + orderid_ex
    if len(ordata) > 98:
        print 'SIM卡 ICCID号: '+parsex(ordata[58:98])
    if len(ordata) > 106:
        print '终端ID: '+parsex(ordata[98:106])
    if len(ordata) > 140:
        print 'VIN: '+parsex(ordata[106:140])
    if parsex(ordata[106:140])==parsex(ordata[4:38]):
        print '解析成功，唯一标识码与VIN码一致'
    else:
        print '唯一标识码与VIN码不一致，请检查包是否有误'
    if len(ordata) > 180:
        print '平台编号: '+parsex(ordata[140:180])
    if len(ordata) > 184:
            print 'ECU 类型: '+parsex(ordata[180:184])
    print '当前状态：' + f1_ex
    print '指令是否成功执行：' + f2_ex
    print '失败原因：' + f3_ex

# 上锁／解锁
def lockorunlock3(ordata):
    print '上锁／解锁'
    orderid=ordata[56:58]
    orderid_ex = ''
    if orderid == '80':
        orderid_ex = '0x80: 锁死'
    elif orderid == '81':
        orderid_ex = '0x81: 限速'
    elif orderid == '81':
        orderid_ex = '0x82: 限扭矩'
    elif orderid == '81':
        orderid_ex = '0x90: 解锁'
    print 'VIN: ' + parsex(ordata[4:38])
    print 'time: ' + timeparsex(ordata[44:56])
    print '命令ID为：' + orderid_ex
    if len(ordata) > 98:
        print 'SIM卡 ICCID号: '+parsex(ordata[58:98])
    if len(ordata) > 106:
        print '终端ID: '+parsex(ordata[98:106])
    if len(ordata) > 140:
        print 'VIN: '+parsex(ordata[106:140])
    if parsex(ordata[106:140])==parsex(ordata[4:38]):
        print '解析成功，唯一标识码与VIN码一致'
    else:
        print '唯一标识码与VIN码不一致，请检查包是否有误'
    if len(ordata) > 180:
        print '平台编号: '+parsex(ordata[140:180])
    if len(ordata) > 184:
        print '限转速: '+parsex(ordata[180:184])
    if len(ordata) > 186:
        print '限扭矩: '+parsex(ordata[184:186])
# 上锁/解锁 结果应答的应答
def lockorunlock4(ordata):
    print '上锁/解锁 结果应答的应答'
    # 判断命令ID
    orderid=ordata[56:58]
    orderid_ex=''
    if orderid == '80':
        orderid_ex = '锁死'
    elif orderid == '81':
        orderid_ex = '限速'
    elif orderid == '82':
        orderid_ex = '限扭矩'
    elif orderid == '90':
        orderid_ex = '解锁'
    print 'VIN: ' + parsex(ordata[4:38])
    print 'time: ' + timeparsex(ordata[44:56])
    print '命令ID为：' + orderid_ex
    if len(ordata) > 98:
        print 'SIM卡 ICCID号: '+parsex(ordata[58:98])
    if len(ordata) > 106:
        print '终端ID: '+parsex(ordata[98:106])
    if len(ordata) > 140:
        print 'VIN: '+parsex(ordata[106:140])
    if parsex(ordata[106:140])==parsex(ordata[4:38]):
        print '解析成功，唯一标识码与VIN码一致'
    else:
        print '唯一标识码与VIN码不一致，请检查包是否有误'
    if len(ordata) > 180:
        print '平台编号: '+parsex(ordata[140:180])
    # 判断当前状态
    status = ordata[180:182]
    status_ex = ''
    if status == '00':
        status_ex = '锁定状态'
    elif status == '01':
        status_ex = '解锁状态'
    print '当前状态： '+status_ex
    # 判断指令是否成功执行
    isokdone = ordata[182:184]
    isokdone_ex = ''
    if isokdone == '00':
        isokdone_ex = '成功'
    elif isokdone == '01':
        isokdone_ex = '失败'
    print '指令执行状态： '+isokdone_ex
    # 失败原因
    resone = ordata[184:186]
    resone_ex = ''
    if resone == '00':
        resone_ex = '未失败'
    elif resone == '01':
        resone_ex = '参数错误'
    elif resone == '02':
        resone_ex = '超时'
    elif resone == '03':
        resone_ex = '命令ID错误'
    elif resone == '04':
        resone_ex = 'ECU 故障'
    elif resone == '05':
        resone_ex = '设备未激活'
    elif resone == '06':
        resone_ex = 'ECU 握手失败'
    elif resone == '07':
        resone_ex = 'ECU 已主动锁车'
    elif resone == '08':
        resone_ex = 'ECU 未主动锁车'
    print '失败原因： ' + resone_ex
    print '*' * 30
while 1:
    print '*' * 15+'the function start'+'*' * 15
    ordata = raw_input("please input data:\n")
    ordata = ordata[5:]
    datatype = ordata[:4]
    vin = ordata[4:38]
    if len(ordata) > 56:
        time = ordata[44:56]
    else:
        time = ''
    if len(ordata) > 58:
        flag = ordata[56:58]
    else:
        flag = ''
    if datatype == '82fe' and (flag == '55' or flag == 'AA'):
        '''
        进入绑定/解绑 包分析
        '''
        lockorunlock1(ordata)
    if datatype == '09fe' and (flag == '55' or flag == 'AA'):
        '''
        进入绑定/解绑 结果应答 包分析
        '''
        lockorunlock2(ordata)
    if datatype == '82fe' and (flag == '80' or flag == '81' or flag == '82' or flag == '90'):
        '''
        进入上锁／解锁 包分析
        '''
        lockorunlock3(ordata)
    if datatype == '09fe' and (flag == '80' or flag == '81' or flag == '82' or flag == '90'):
        '''
        进入上锁／解锁 结果应答 包分析
        '''
        lockorunlock4(ordata)




    iscon = raw_input('是否继续程序？是：1 否：其他\n')
    if iscon == '1':
        pass
    else:
        break