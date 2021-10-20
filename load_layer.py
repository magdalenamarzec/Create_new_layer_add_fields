""" Poniższy skrypt służy do szybkiego dodania wielu warstw do projektu """
from qgis import *
parent = iface.mainWindow()
homeP = QgsProject.instance().homePath()

file_dir = QFileDialog.getExistingDirectory(parent, "Folder to save layers", homeP)
print(file_dir)
geometr_list = ['Point', 'Line', 'Polygon']


while True:
    name, ok = QInputDialog.getText(parent, 'Nowa warstwa', 'Podaj nazwę warstwy')
    layer_dir = f'{file_dir}\{name}.shp'
    if ok == False:
        break
    else:
        print("Nazwa warstwy: ", name)
        geometr, ok2 = QInputDialog.getItem(parent, 'Typ geometrii', 'Jaką geometrię ma mieć warstwa?', geometr_list, editable=False)
        layerFields = QgsFields()
        
        if geometr == 'Point':
            writer = QgsVectorFileWriter(layer_dir, 'UTF-8', layerFields, QgsWkbTypes.Point, QgsCoordinateReferenceSystem('EPSG:2180'), 'ESRI Shapefile')
        elif geometr == 'Line':
            writer = QgsVectorFileWriter(layer_dir, 'UTF-8', layerFields, QgsWkbTypes.LineString, QgsCoordinateReferenceSystem('EPSG:2180'), 'ESRI Shapefile')
        elif geometr == 'Polygon':
            writer = QgsVectorFileWriter(layer_dir, 'UTF-8', layerFields, QgsWkbTypes.MultiPolygon, QgsCoordinateReferenceSystem('EPSG:2180'), 'ESRI Shapefile')
        
        iface.addVectorLayer(layer_dir, f'{name}', 'ogr')
        
        
        del(writer)

    
""" Poniższy skrypt służy do szybkiego dodania pól do istniejących warstw """

layers = iface.mapCanvas().layers()
for layer in layers:
    add_cells = QMessageBox.question(parent, 'Dodawanie pól', f'Czy chcesz dodać pola do warstwy {layer}?')
    if add_cells == 16384:
        while True:
            cell_name, ok3 = QInputDialog.getText(parent, 'Nazwa pola', 'Podaj nazwę pola: ')
            if ok3 == True:
                layer_provider = layer.dataProvider()
                layer_provider.addAttributes([QgsField(cell_name, QVariant.String)])
                layer.updateFields()
            elif ok3 == False:
                break
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
