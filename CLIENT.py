from Imports import *
from App_Settings import *


def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)

@app.route('/')
def index():
    """Render the app"""
    return render_template('index.html')


@app.route('/Designer',  methods=['GET','POST'])
def Designer():
    Dynamic_USER = uuid.uuid1().hex


    content =   "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/CONTENT/CONTENT.jpg"
    STYLES_1 =  "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/STYLES/1.jpg"
    STYLES_2 =  "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/STYLES/2.jpg"
    STYLES_3 =  "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/STYLES/3.jpg"
    STYLES_4 =  "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/STYLES/4.jpg"
    STYLES_5 =  "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/STYLES/5.jpg"

    token_file = "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/OTHER_MATERIALS/TOKEN.txt"
    URLS_file = "E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/OTHER_MATERIALS/URLS.txt"
    FILE_COUNT_TXT = f"E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/OTHER_MATERIALS/FILE_COUNT.txt"

    Client_tokens = 'Nihilent_12345'
    URLS = f'http://127.0.0.1:5000/Decode_Design/{Dynamic_USER}'
    FILE_COUNT = str(5)

    print(URLS)
    
    with open(token_file, "w") as text_file:
        text_file.write(Client_tokens)

    with open(URLS_file, "w") as text_file:
        text_file.write(URLS)

    with open(FILE_COUNT_TXT, "w") as text_file:
        text_file.write(FILE_COUNT)
    
    text_file.close()

   
    img_files = {   'CONTENT': open(content, 'rb'),   'STYLES_1':open(STYLES_1, 'rb'), 
                    'STYLES_2':open(STYLES_2, 'rb'),'STYLES_3':open(STYLES_3, 'rb'), 
                    'STYLES_4':open(STYLES_4, 'rb'),'STYLES_5':open(STYLES_5, 'rb'),
                    'TOKEN': open(token_file, 'rb'),'URLS':  open(URLS_file, 'rb'),  
                    'FILE_COUNT': open(FILE_COUNT_TXT, 'rb')}    
   
    # img_files = {   'CONTENT': open(content, 'rb'),'STYLES_1':open(STYLES_1, 'rb'), 
    #                 'STYLES_2':open(STYLES_2, 'rb'),'TOKEN': open(token_file, 'rb'),
    #                 'URLS':  open(URLS_file, 'rb'), 'FILE_COUNT': open(FILE_COUNT_TXT, 'rb')}
    print(img_files)
    res2 = requests.post(F'http://127.0.0.1:8000/CREATION/{Dynamic_USER}', files= img_files)
    print(res2.url)

    print(res2.text)

    print(res2.status_code)
  
    return ('', 204)


@app.route('/Decode_Design/<USER>',  methods=['GET','POST'])
def Decode_Design(USER):
    
    FILE_COUNT = 5
    for i in nums(1, 5):

        PAINTINGS_1 = request.files[f'PAINTINGS_{i}']
        PAINTINGS_FILE_1 = secure_filename(PAINTINGS_1.filename) 
        PAINTINGS_FILE_1 = PAINTINGS_1.save(os.path.join(f'E:/Zeus/Zeus/Zeus_AI/AI_Kalakaar/PRODUCTION_TEST/CLIENT/GENERATED_PAINTINGS/', PAINTINGS_FILE_1)) 

        print(PAINTINGS_1)
        print(PAINTINGS_FILE_1)

    return ('', 204)
   