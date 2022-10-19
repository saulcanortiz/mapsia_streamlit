from turtle import right
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="MAPSIA", page_icon=":rocket:")



image = Image.open('images/logo.jpeg')
st.image(image, width=600)




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_t26law.json")

with st.container():
    st.title("Welcome to MAPSIA")
    st.write("The objective of MAPSIA is to locate and classify pavement superficial defects using Deep Learning algorithms, by means of images collected by a low-cost vehicle-mounted system.")
    st.write("""
        The two main problems of the state-of-the-art studies on automated pavement distress detection and categorization are:
        - :x: Lack of public, standard, comprehensive and practical pavement distress datasets.
        - :x: High price of commercial acquistion devices such as Pavement Inspection Vehicles (around $1M).
        """
    )
    st.write("""
        Our approach alleviates these constraints:
        - :white_check_mark:  7099 images with 13 distress types collected under different illumination conditions, and annotated in several formats for object detection models.
        - :white_check_mark: Establishment of low-cost, non-destructive, fast-acquisition vehicle-mounted system.
        """
    )
    st.write("Dowload the dataset depending on a suitable format. Happy coding! ")
    


with st.container():
    st_lottie(lottie_coding, height=100, key="coding")
    left_column, right_column,left_column1, right_column1 = st.columns(4)
    with left_column:
        st.write("[COCO](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EbxQVZqH1v9AmO-11jK06NcB_Vi4bVriPfn5_8WANAS7wA?e=0eS01Z)")
        
            
    with right_column:
        st.write("[PASCAL VOC](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EUXHXG6SVypIiqBQg3g-fYsB1Ct_IbkPbulHUI0ghbWSDQ?e=4cSuph)")
        
    with left_column1:
        st.write("[YOLO Darknet](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/Ec_uDo77kSlKtCkmow9U3PEB16dOz4WmyVfwrSva0OcpTQ?e=PsH5sr)")
        
    with right_column1:
        st.write("[YOLOV3 Keras](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EWyWhzzJ6_hBlkfaU4Ee6gwBAtJVUcMxJ3cCuomY3C9BUA?e=k2uc6Q)")
        
    left_column2, right_column2,left_column3, right_column3 = st.columns(4)
    with left_column2:
        st.write("[YOLOv4 PyTorch](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EZaXi3Wu9uVBvWaRMchEugIB5t29m6YLrF-E6pwt1YwJJQ?e=XJW5A6)")
            
    with right_column2:
        st.write("[YOLOv5 PyTorch](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EXZhPyZU7tlCkftVzfj3EW0BybXmJKDm7AO6yYXTie6dnw?e=eszHyP)")
            
    with left_column3:
        st.write("[YOLO v6 PyTorch](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EfDwNUSTwGhDl8ENGK7yVjoBQkf7sXozPUDf_i8-O2959A?e=s7jPFi)")
            
    with right_column3:
        st.write("[YOLOv7 PyTorch](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EQHdvfSfuj5FtrPOTE9YIY0B5xhgpjSe7R4qPUwSgdZMcw?e=KlPETS)")
        
            
    left_column4, right_column4,left_column5, right_column5 = st.columns(4)
    with left_column4:
        st.write("[TF Object Detection](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EXP2IqNLMJJJl5hXAvGcXkABYvIRv_i-elmcexY3booMUA?e=RcEGgr)")
            
    with right_column4:
        st.write("[Retinanet Keras](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/ERNnh0hQIKRKqQr2KAR0sD4BKwSYw-49toNG3YGHgytbrQ?e=cBoXb6)")
            
    with left_column5:
        st.write("[TFRecord](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EQVM_5ZzqOlKo4fUqKIcdHEBkoVaYEY1iubB3fvq5nKCTA?e=OxSyFx)")
            
    with right_column5:
        st.write("[CreateML](https://unican-my.sharepoint.com/:u:/g/personal/canos_unican_es/EUGDl1RauAtAjd-Z15kmHx0BxvqBsqNGa8iQDXclbdwmNA?e=JYF0wn)")
         
           

with st.container():
    st.write("---")
    st.title("The Mosquito System")
    left_column, right_column = st.columns(2)
    with left_column:
        
        image = Image.open('images/2022-08-10_103751.jpg')
        st.image(image)
    with right_column:
        image = Image.open('images/2022-08-10_103854.jpg')
        st.image(image)

    st.write("It is an UAV mounted on a 3D printing structure that is placed on the rear window of the vehicle by means of a suction cup system. It is priced at $626, provides high quality geo-referenced images for vehicle speeds up to 120 km/h, fits any vehicle, has a battery life of 5 hours per battery, storage capacity depends on the microSD card, the camera can rotate and its optical parameters can be changed with the co-driver's remote control.")

    left_column1, right_column1 = st.columns(2)
    with left_column1:
        
        image = Image.open('images/20220810_130809.jpg')
        st.image(image)
    with right_column1:
        image = Image.open('images/20220810_143316.jpg')
        st.image(image)   

with st.container():
    st.write("---")
    st.title("The Mosquito dataset")

    st.write("The Mosquitonet contains a high-volume of images, 7099, collected in Cantabria (Spain) with adequate resolution (1080p) and size (1920x1080). It is a multiclass and approximately balanced dataset with 13 superficial road defects under several lighting conditions. One of the aspects that makes a distinction is the quality of distress labelling, where to avoid any confusion, the Distress Identification Manual for the Long-Term Pavement Performance Program of the FHWA has been used, by pavement experts.")
    l1,l2,l3 = st.columns(3)
    with l1:
        image = Image.open('images/D1.jpg')
        st.image(image, caption="D1")
    with l2:
        image = Image.open('images/D2.jpg')
        st.image(image, caption="D2")
    with l3:
        image = Image.open('images/D3.jpg')
        st.image(image, caption="D3")
    

    l4, l5, l6 = st.columns(3)
    with l4:
        image = Image.open('images/D4.jpg')
        st.image(image, caption="D4")
    with l5:
        image = Image.open('images/D5.jpg')
        st.image(image, caption="D5")
    with l6:
        image = Image.open('images/D6.jpg')
        st.image(image, caption="D6")
    l7, l8, l9 = st.columns(3)
    with l7:
        image = Image.open('images/D7.jpg')
        st.image(image, caption="D7")
    with l8:
        image = Image.open('images/D8.jpg')
        st.image(image, caption="D8")
    with l9:
        image = Image.open('images/D9.jpg')
        st.image(image, caption="D9")
    l10, l11, l12 = st.columns(3)
    with l10:
        image = Image.open('images/D10.jpg')
        st.image(image, caption="D10")
    with l11:
        image = Image.open('images/D11.jpg')
        st.image(image, caption="D11")
    with l12:
        image = Image.open('images/D12.jpg')
        st.image(image, caption="D12")
    image = Image.open('images/D13.jpg')
    st.image(image, caption="D13", width=225)
    st.write("D1 = Block crack, D2 = Alligator crack, D3 = Diagonal crack, D4 = Longitudinal crack, D5 = Isolated crack, D6 = Transversal crack, D7 = Central longitudinal crack, D8 = Patch, D9 = Pothole, D10/D11 = Manholes, D12 = Ravelling, D13 = Sealed crack.")


with st.container():
    st.write("---")
    st.title("About Us")
    l, r = st.columns(2)
    lottie_coding2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_vsiy6ziu.json")
    

    with l:
        st.write("The MAPSIA Rocket Team is composed of Saúl Cano-Ortiz, Daniel Castro-Fresno and Pablo Martínez Ruiz del Árbol. ")
        st.write("Saúl is a physicist with a Master in Data Science and is a PhD candidate. His role is Data Scientist.")
        st.write("Daniel is a civil engineer, professor, director of GITECO and of the Faculty of Civil Engineering. His role is pavement expert and PhD director.")
        st.write("Pablo is a physicist, professor and Data Scientist. His role is Data Science expert and PhD co-director.")
    with r:
        st_lottie(lottie_coding2, height=300, key="coding4")

    st.write("The project was developed at the University of Cantabria. Also, there are collaborators: Pedro de la Lastra-González (image annotation validator) and Adolfo Cobo-García (expert in image acquisition devices and geolocation).")
    
    

with st.container():
    st.write("---")
    st.title("Related papers")
    st.write("""
        - [Machine Learning for monitoring pavement performance (Automation in Construction)](https://www.sciencedirect.com/science/article/pii/S0926580522001820).""")
    

    