
import gooeypie as gp
import Results_window
import boolean_retriever
import backend


# var needed
ret = [] # the returned doc_ids
# types of retrieval
docs = []

boolean_retriever.connect(dbname = 'mimic', user = 'postgres', password = '05170029LCy')
# def perform_retrieval(button=gp.Button):
def perform_retrieval("double_click"):

    global txt_box,ret, docs

    query = txt_box.text
    if query== None :
        return
    no_to_get = txt_box2.text

    try:
        val = int(no_to_get)
        if val >20:
            val=20
    except ValueError:
        val = 20
    
    ret = backend.search(query,val,insurance=dd1.selected,ethnicity= dd2.selected,religion= dd3.selected,gender= dd4.selected,marital_status = dd5.selected)

    if len(ret)== 0 :
        return
    Results_window.display_results(query,ret,doc_ids = None,insurance=dd1.selected,ethnicity= dd2.selected,religion= dd3.selected,gender= dd4.selected,marital_status = dd5.selected)

# Set up the application Window
ui = gp.GooeyPieApp("MIMIC Retriever")
ui.width = 500
ui.height = 750

# setup the picture
pic = gp.Image(ui,'/Users/chenyuli/My_Pitt/INFSCI 2140/Project/MIMIC-notes-indexing/retrieval_tool/mimicpic.png')

# Set up the search button
search_button = gp.Button(ui,"Search", perform_retrieval)
search_button.click("double_click")
# Setup the input box
txt_box  = gp.Input(ui)
txt_box.width=40

txt_box2  = gp.Input(ui)
txt_box2.width=10

lbl01 = gp.Label(ui,"How many notes to retrieve")

# Setup the Label
lbl = gp.StyleLabel(ui,"Enter the cohort \nyou wish to search for here")

# Setup check boxes
ins_levels= ["Medicare","Government","Private","Medicaid","Self Pay"]
dd1= gp.Dropdown(ui,ins_levels)

e_levles=["WHITE","BLACK/AFRICAN AMERICAN","HISPANIC/LATINO - PUERTO RICAN","OTHER","ASIAN","HISPANIC OR LATINO","UNKNOWN/NOT SPECIFIED","PATIENT DECLINED TO ANSWER","ASIAN - CHINESE","AMERICAN INDIAN/ALASKA NATIVE","MULTI RACE ETHNICITY","WHITE - EASTERN EUROPEAN","BLACK/CAPE VERDEAN","WHITE - RUSSIAN","BLACK/HAITIAN","CARIBBEAN ISLAND","UNABLE TO OBTAIN","BLACK/AFRICAN"]
dd2= gp.Dropdown(ui,e_levles)

rel_levles=["EPISCOPALIAN","OTHER","JEWISH","NOT SPECIFIED","CATHOLIC","UNOBTAINABLE","PROTESTANT QUAKER","GREEK ORTHODOX","JEHOVAH'S WITNESS ","UNITARIAN-UNIVERSALIST","null","7TH DAY ADVENTIST","BAPTIST","BUDDHIST","MUSLIM","METHODIST","HEBREW","CHRISTIAN SCIENTIST","ROMANIAN EAST. ORTH","HINDU","LUTHERAN"]
dd3= gp.Dropdown(ui,rel_levles)

g_levles=["M","F"]
dd4= gp.Dropdown(ui,g_levles)

m_levles=["DIVORCED","SINGLE","MARRIED","WIDOWED","SEPARATED","null","UNKNOWN (DEFAULT)","LIFE PARTNER"]
dd5= gp.Dropdown(ui,m_levles)

# Setup the UI
ui.set_grid(10,3)

ui.add(pic,1,2,)
ui.add(lbl,2,1,)
ui.add(txt_box,2,2)
ui.add(lbl01,4,1)
ui.add(txt_box2,4,2)
ui.add(search_button,5,2,)

ui.add(dd1,6,1, align = 'left')
ui.add(dd2,7,1,align = 'left')
ui.add(dd3,8,1,align = 'left')
ui.add(dd4,9,1,align = 'left')
ui.add(dd5,10,1,align = 'left')

lbl1 = gp.Label(ui,"Insurance")
lbl2 = gp.Label(ui,"Ethnicity")
lbl3 = gp.Label(ui,"Religion")
lbl4 = gp.Label(ui,"Gender")
lbl5 = gp.Label(ui,"Marital status")

ui.add(lbl1,6,2, align = 'left')
ui.add(lbl2,7,2,align = 'left')
ui.add(lbl3,8,2,align = 'left')
ui.add(lbl4,9,2,align = 'left')
ui.add(lbl5,10,2,align = 'left')

# Run the UI
ui.run()
