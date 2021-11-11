from happytransformer import HappyTextToText, TTSettings
import torch
import streamlit as st


st.title('Grammar & Spell Checker')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

happy_tt=torch.load('happy_tt.pt')

args = TTSettings(num_beams=5, min_length=1)

if st.button('Correct Sentence'):
    if text == '':
        st.write('Please enter text for checking') 
    else:
        try: 
            result = happy_tt.generate_text("grammar: "+text, args=args)
            
            st.markdown('**Corrected Sentence - **' + result.text)
        except:
            st.write('Please check internet connectivity')
else:
     pass