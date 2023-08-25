#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        folder_dialog = ui.createFolderDialog()
        folder_dialog.title = "Select Destination Folder"
        if folder_dialog.showDialog() == adsk.core.DialogResults.DialogOK:
            destination_folder = folder_dialog.folder
        else:
            return
        design = adsk.fusion.Design.cast(app.activeProduct)
        if design==None:
            ui.messageBox('Must be in design workspace to use this function')
            return
        
        sketches = design.rootComponent.sketches
        sketch_list = []
        for sketch in sketches:
            sketch_list.append(sketch.name)

        try:
            export_idx = sketch_list.index('export_start')
        except:
            ui.messageBox('missing sketch with the name "export_start"')
            return
        file_idx = 0
        for idx in range(export_idx,len(sketch_list)):
            resp = sketches.item(idx).saveAsDXF(f'{destination_folder}/s{file_idx}.dxf')
            file_idx+=1

        ui.messageBox(f'a total of {len(sketch_list)-export_idx} file(s) exported')            

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
