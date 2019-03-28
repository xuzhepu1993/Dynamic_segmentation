# -*- coding: cp936 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

#接收参数
#input_raster_str:选择的特征层完整路径
#input_raster_name：特征层名称
#env_path_str：工作空间路径
input_raster_str=arcpy.GetParameterAsText(0)
input_raster_name=input_raster_str.split('\\')[-1]
env_path_str=input_raster_str[:(len(input_raster_str)-len(input_raster_name)-1)]
arcpy.env.workspace=env_path_str

#新建7个列表，用来存放筛选的数据
list_level1_id=[]
list_level2_id=[]
list_level3_id=[]
list_level4_id=[]
list_level5_id=[]
list_level6_id=[]
list_level7_id=[]
list_level8_id=[]
list_level9_id=[]
list_level10_id=[]
list_level11_id=[]
list_level12_id=[]
list_level13_id=[]
list_level14_id=[]
list_level15_id=[]
list_level16_id=[]
list_level17_id=[]
list_level18_id=[]
list_level19_id=[]
list_level20_id=[]
list_level21_id=[]
list_level22_id=[]
list_level23_id=[]
list_level24_id=[]
list_level25_id=[]
list_level26_id=[]
list_level27_id=[]

#遍历input_raster，将id值分级放到列表中
#注意，下面将input_raster，即输入的特征层用reclassify_east2_all_contour表达了
mapdoc=arcpy.mapping.MapDocument("CURRENT")
listLayers=arcpy.mapping.ListLayers(mapdoc)
for layer in listLayers:
    if layer.name==input_raster_name:
        reclassify_east2_all_contour=layer

#准备好7个梯度的contour值
level1_tokens=[111]
level2_tokens=[112]
level3_tokens=[113]
level4_tokens=[121]
level5_tokens=[122]
level6_tokens=[123]
level7_tokens=[131]
level8_tokens=[132]
level9_tokens=[133]
level10_tokens=[211]
level11_tokens=[212]
level12_tokens=[213]
level13_tokens=[221]
level14_tokens=[222]
level15_tokens=[223]
level16_tokens=[231]
level17_tokens=[232]
level18_tokens=[233]
level19_tokens=[311]
level20_tokens=[312]
level21_tokens=[313]
level22_tokens=[321]
level23_tokens=[322]
level24_tokens=[323]
level25_tokens=[331]
level26_tokens=[332]
level27_tokens=[333]


cursor=arcpy.da.SearchCursor(reclassify_east2_all_contour,["Id","Contour"])
for row in cursor:
    if row[1] in level1_tokens:
        list_level1_id.append(row[0])
    if row[1] in level2_tokens:
        list_level2_id.append(row[0])
    if row[1] in level3_tokens:
        list_level3_id.append(row[0])
    if row[1] in level4_tokens:
        list_level4_id.append(row[0])
    if row[1] in level5_tokens:
        list_level5_id.append(row[0])
    if row[1] in level6_tokens:
        list_level6_id.append(row[0])
    if row[1] in level7_tokens:
        list_level7_id.append(row[0])
    if row[1] in level8_tokens:
        list_level8_id.append(row[0])
    if row[1] in level9_tokens:
        list_level9_id.append(row[0])
    if row[1] in level10_tokens:
        list_level10_id.append(row[0])
    if row[1] in level11_tokens:
        list_level11_id.append(row[0])
    if row[1] in level12_tokens:
        list_level12_id.append(row[0])
    if row[1] in level13_tokens:
        list_level13_id.append(row[0])
    if row[1] in level14_tokens:
        list_level14_id.append(row[0])
    if row[1] in level15_tokens:
        list_level15_id.append(row[0])
    if row[1] in level16_tokens:
        list_level16_id.append(row[0])
    if row[1] in level17_tokens:
        list_level17_id.append(row[0])
    if row[1] in level18_tokens:
        list_level18_id.append(row[0])
    if row[1] in level19_tokens:
        list_level19_id.append(row[0])
    if row[1] in level20_tokens:
        list_level20_id.append(row[0])
    if row[1] in level21_tokens:
        list_level21_id.append(row[0])
    if row[1] in level22_tokens:
        list_level22_id.append(row[0])
    if row[1] in level23_tokens:
        list_level23_id.append(row[0])
    if row[1] in level24_tokens:
        list_level24_id.append(row[0])
    if row[1] in level25_tokens:
        list_level25_id.append(row[0])
    if row[1] in level26_tokens:
        list_level26_id.append(row[0])
    if row[1] in level27_tokens:
        list_level27_id.append(row[0])

#准备好所有的特征层,根据输出层的名称，生成7个特征层
output_raster_str=arcpy.GetParameterAsText(1)
output_raster_name=output_raster_str.split('\\')[-1]
output_path_str=output_raster_str[:(len(output_raster_str)-len(output_raster_name)-1)]

level_1_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level1',"POLYLINE")
arcpy.AddField_management(level_1_east2,'Id',"SHORT")
arcpy.AddField_management(level_1_east2,'Contour',"SHORT")

level_2_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level2',"POLYLINE")
arcpy.AddField_management(level_2_east2,'Id',"SHORT")
arcpy.AddField_management(level_2_east2,'Contour',"SHORT")

level_3_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level3',"POLYLINE")
arcpy.AddField_management(level_3_east2,'Id',"SHORT")
arcpy.AddField_management(level_3_east2,'Contour',"SHORT")

level_4_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level4',"POLYLINE")
arcpy.AddField_management(level_4_east2,'Id',"SHORT")
arcpy.AddField_management(level_4_east2,'Contour',"SHORT")

level_5_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level5',"POLYLINE")
arcpy.AddField_management(level_5_east2,'Id',"SHORT")
arcpy.AddField_management(level_5_east2,'Contour',"SHORT")

level_6_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level6',"POLYLINE")
arcpy.AddField_management(level_6_east2,'Id',"SHORT")
arcpy.AddField_management(level_6_east2,'Contour',"SHORT")

level_7_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level7',"POLYLINE")
arcpy.AddField_management(level_7_east2,'Id',"SHORT")
arcpy.AddField_management(level_7_east2,'Contour',"SHORT")

level_8_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level8',"POLYLINE")
arcpy.AddField_management(level_8_east2,'Id',"SHORT")
arcpy.AddField_management(level_8_east2,'Contour',"SHORT")

level_9_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level9',"POLYLINE")
arcpy.AddField_management(level_9_east2,'Id',"SHORT")
arcpy.AddField_management(level_9_east2,'Contour',"SHORT")

level_10_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level10',"POLYLINE")
arcpy.AddField_management(level_10_east2,'Id',"SHORT")
arcpy.AddField_management(level_10_east2,'Contour',"SHORT")

level_11_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level11',"POLYLINE")
arcpy.AddField_management(level_11_east2,'Id',"SHORT")
arcpy.AddField_management(level_11_east2,'Contour',"SHORT")

level_12_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level12',"POLYLINE")
arcpy.AddField_management(level_12_east2,'Id',"SHORT")
arcpy.AddField_management(level_12_east2,'Contour',"SHORT")

level_13_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level13',"POLYLINE")
arcpy.AddField_management(level_13_east2,'Id',"SHORT")
arcpy.AddField_management(level_13_east2,'Contour',"SHORT")

level_14_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level14',"POLYLINE")
arcpy.AddField_management(level_14_east2,'Id',"SHORT")
arcpy.AddField_management(level_14_east2,'Contour',"SHORT")

level_15_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level15',"POLYLINE")
arcpy.AddField_management(level_15_east2,'Id',"SHORT")
arcpy.AddField_management(level_15_east2,'Contour',"SHORT")

level_16_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level16',"POLYLINE")
arcpy.AddField_management(level_16_east2,'Id',"SHORT")
arcpy.AddField_management(level_16_east2,'Contour',"SHORT")

level_17_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level17',"POLYLINE")
arcpy.AddField_management(level_17_east2,'Id',"SHORT")
arcpy.AddField_management(level_17_east2,'Contour',"SHORT")

level_18_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level18',"POLYLINE")
arcpy.AddField_management(level_18_east2,'Id',"SHORT")
arcpy.AddField_management(level_18_east2,'Contour',"SHORT")

level_19_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level19',"POLYLINE")
arcpy.AddField_management(level_19_east2,'Id',"SHORT")
arcpy.AddField_management(level_19_east2,'Contour',"SHORT")

level_20_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level20',"POLYLINE")
arcpy.AddField_management(level_20_east2,'Id',"SHORT")
arcpy.AddField_management(level_20_east2,'Contour',"SHORT")

level_21_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level21',"POLYLINE")
arcpy.AddField_management(level_21_east2,'Id',"SHORT")
arcpy.AddField_management(level_21_east2,'Contour',"SHORT")

level_22_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level22',"POLYLINE")
arcpy.AddField_management(level_22_east2,'Id',"SHORT")
arcpy.AddField_management(level_22_east2,'Contour',"SHORT")

level_23_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level23',"POLYLINE")
arcpy.AddField_management(level_23_east2,'Id',"SHORT")
arcpy.AddField_management(level_23_east2,'Contour',"SHORT")

level_24_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level24',"POLYLINE")
arcpy.AddField_management(level_24_east2,'Id',"SHORT")
arcpy.AddField_management(level_24_east2,'Contour',"SHORT")

level_25_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level25',"POLYLINE")
arcpy.AddField_management(level_25_east2,'Id',"SHORT")
arcpy.AddField_management(level_25_east2,'Contour',"SHORT")

level_26_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level26',"POLYLINE")
arcpy.AddField_management(level_26_east2,'Id',"SHORT")
arcpy.AddField_management(level_26_east2,'Contour',"SHORT")

level_27_east2=arcpy.CreateFeatureclass_management(output_path_str,output_raster_name+'_level27',"POLYLINE")
arcpy.AddField_management(level_27_east2,'Id',"SHORT")
arcpy.AddField_management(level_27_east2,'Contour',"SHORT")

#遍历大数据表，判断每一行数据，并将数据行复制到对应的特征层当中去
mapdoc=arcpy.mapping.MapDocument("CURRENT")
listLayers=arcpy.mapping.ListLayers(mapdoc)
for layer in listLayers:
    if layer.name=='reclassify_east2_all_contour':
        reclassify_east2_all_contour=layer

cursor=arcpy.da.SearchCursor(reclassify_east2_all_contour,["OID@","SHAPE@","Id","Contour"])
for row in cursor:
    if row[2] in list_level1_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_1_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])
    if row[2] in list_level2_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_2_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])    
    if row[2] in list_level3_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_3_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])    
    if row[2] in list_level4_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_4_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])    
    if row[2] in list_level5_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_5_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])    
    if row[2] in list_level6_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_6_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])
    if row[2] in list_level7_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_7_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level8_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_8_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level9_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_9_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level10_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_10_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level11_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_11_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level12_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_12_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level13_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_13_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level14_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_14_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level15_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_15_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level16_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_16_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level17_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_17_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level18_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_18_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level19_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_19_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level20_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_20_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level21_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_21_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level22_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_22_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level23_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_23_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level24_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_24_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level25_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_25_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level26_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_26_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

    if row[2] in list_level27_id:
        line_array=arcpy.Array()
        for point in row[1].getPart(0):
            point_temp=arcpy.Point()
            point_temp.ID=point.ID
            point_temp.X=point.X
            point_temp.Y=point.Y
            line_array.add(point)
        cursor_temp=arcpy.da.InsertCursor(level_27_east2,["SHAPE@","Id","Contour"])
        polyline=arcpy.Polyline(line_array)
        cursor_temp.insertRow([polyline,row[2],row[3]])

#最后，将上述图层都添加到地图上显示出来
mapdoc=arcpy.mapping.MapDocument("CURRENT")
dataframe=arcpy.mapping.ListDataFrames(mapdoc)[0]
arcpy.env.workspace=output_path_str

level_1_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level1')
arcpy.mapping.AddLayer(dataframe, level_1_east2_layer, "AUTO_ARRANGE")

level_2_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level2')
arcpy.mapping.AddLayer(dataframe, level_2_east2_layer, "AUTO_ARRANGE")

level_3_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level3')
arcpy.mapping.AddLayer(dataframe, level_3_east2_layer, "AUTO_ARRANGE")

level_4_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level4')
arcpy.mapping.AddLayer(dataframe, level_4_east2_layer, "AUTO_ARRANGE")

level_5_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level5')
arcpy.mapping.AddLayer(dataframe, level_5_east2_layer, "AUTO_ARRANGE")

level_6_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level6')
arcpy.mapping.AddLayer(dataframe, level_6_east2_layer, "AUTO_ARRANGE")

level_7_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level7')
arcpy.mapping.AddLayer(dataframe, level_7_east2_layer, "AUTO_ARRANGE")

level_8_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level8')
arcpy.mapping.AddLayer(dataframe, level_8_east2_layer, "AUTO_ARRANGE")

level_9_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level9')
arcpy.mapping.AddLayer(dataframe, level_9_east2_layer, "AUTO_ARRANGE")

level_10_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level10')
arcpy.mapping.AddLayer(dataframe, level_10_east2_layer, "AUTO_ARRANGE")

level_11_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level11')
arcpy.mapping.AddLayer(dataframe, level_11_east2_layer, "AUTO_ARRANGE")

level_12_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level12')
arcpy.mapping.AddLayer(dataframe, level_12_east2_layer, "AUTO_ARRANGE")

level_13_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level13')
arcpy.mapping.AddLayer(dataframe, level_13_east2_layer, "AUTO_ARRANGE")

level_14_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level14')
arcpy.mapping.AddLayer(dataframe, level_14_east2_layer, "AUTO_ARRANGE")

level_15_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level15')
arcpy.mapping.AddLayer(dataframe, level_15_east2_layer, "AUTO_ARRANGE")

level_16_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level16')
arcpy.mapping.AddLayer(dataframe, level_16_east2_layer, "AUTO_ARRANGE")

level_17_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level17')
arcpy.mapping.AddLayer(dataframe, level_17_east2_layer, "AUTO_ARRANGE")

level_18_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level18')
arcpy.mapping.AddLayer(dataframe, level_18_east2_layer, "AUTO_ARRANGE")

level_19_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level19')
arcpy.mapping.AddLayer(dataframe, level_19_east2_layer, "AUTO_ARRANGE")

level_20_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level20')
arcpy.mapping.AddLayer(dataframe, level_20_east2_layer, "AUTO_ARRANGE")

level_21_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level21')
arcpy.mapping.AddLayer(dataframe, level_21_east2_layer, "AUTO_ARRANGE")

level_22_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level22')
arcpy.mapping.AddLayer(dataframe, level_22_east2_layer, "AUTO_ARRANGE")

level_23_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level23')
arcpy.mapping.AddLayer(dataframe, level_23_east2_layer, "AUTO_ARRANGE")

level_24_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level24')
arcpy.mapping.AddLayer(dataframe, level_24_east2_layer, "AUTO_ARRANGE")

level_25_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level25')
arcpy.mapping.AddLayer(dataframe, level_25_east2_layer, "AUTO_ARRANGE")

level_26_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level26')
arcpy.mapping.AddLayer(dataframe, level_26_east2_layer, "AUTO_ARRANGE")

level_27_east2_layer=arcpy.mapping.Layer(output_raster_name+'_level27')
arcpy.mapping.AddLayer(dataframe, level_27_east2_layer, "AUTO_ARRANGE")