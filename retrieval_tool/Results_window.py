import gooeypie as gp

import boolean_retriever

# var needed
ret = [] # the returned doc_ids
gooey_labels = {}
query =""
documents ={}
sub_id = {}

def display_results(query,val,doc_ids,insurance=None, ethnicity = None,religion= None,gender=None,marital_status = None):
    

    ret=val

    ui = gp.GooeyPieApp("Results")
    ui.set_grid(len(val)+5,3)
    ui.width = 500
    ui.height = 750

    lbl = gp.StyleLabel(ui,"Here are the results")
    lbl.font_name='Ariel'
    lbl.font_size = 26
    ui.add(lbl, 1, 2, align='center')

    lbl = gp.StyleLabel(ui, "\""+query+"\"")
    lbl.font_name = 'Ariel'
    lbl.font_size = 20
    ui.add(lbl, 2, 2, align='center')

    str = ""
    if gender:
        str=str+"Gender: " + gender
    if marital_status:
        str = str+ " Marital status: " + marital_status
    if insurance:
        str = str + " Insurance: " + insurance
    if ethnicity:
        str = str +  " Ethnicity: " + ethnicity
    if religion:
        str= str + " Religion: " + religion
    lbl2 = gp.Label(ui,str)
    ui.add(lbl2,3,2)

    i = 4
    while i < len(ret)+4:
        lbl1 = gp.Label(ui, boolean_retriever.get_text((ret[i-4])))
        lbl2 = gp.Label(ui, doc_ids[i-4])
        ui.add(lbl1, i, 3)
        ui.add(lbl2,i,1)
        i= i +1


    # Run the UI
    ui.run()

if __name__ == "__main__":
    display_results(" tester",[" Some doc_ids", "some docuemnts"],["1234","12"])
