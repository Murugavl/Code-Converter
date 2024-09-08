import streamlit as st

st.set_page_config(page_title='Code Converter App')
def binary_to_decimal(d):
        num=d
        sums=0
        places=0
        while num!=0:
              r=num%10
              sums=sums+(r*pow(2,places))
              places+=1
              num=num//10
        return sums

def binary_to_octal(d):
               deci=binary_to_decimal(d)
               sums=decimal_to_octal(deci)
               return sums 

def binary_to_hexadecimal(d):
               deci=binary_to_decimal(d)
               sums=decimal_to_hexadecimal(deci)
               return sums           
    
def decimal_to_binary(d):
        num=d
        binary_list=[]
        while num!=0:
                r=num%2
                binary_list.append(str(r))
                num=num//2
        binary_list.reverse()
        binary=int(''.join(binary_list))
        return binary
        
    

def decimal_to_octal(d):
            O=d
            n3=O
            octa_list=[]
            while n3!=0:
                r=n3%8
                octa_list.append(str(r))
                n3=n3//8
            octa_list.reverse()
            octanum=int(''.join(octa_list))
            return octanum


def decimal_to_hexadecimal(d):
            n2=d
            hexa_list=[]
            while n2!=0:
                    r=n2%16
                    if r==10:
                        hexa_list.append('A')
                    elif r==11:
                        hexa_list.append('B')
                    elif r==12:
                        hexa_list.append('C')
                    elif r==13:
                        hexa_list.append('D')
                    elif r==14:
                        hexa_list.append('E')
                    elif r==15:
                        hexa_list.append('F')
                    else:
                      hexa_list.append(str(r))
                    n2=n2//16
            hexa_list.reverse()
            hexanum=(''.join(hexa_list))
            return hexanum
        
def octal_to_decimal(d):
                    n4=d
                    decimal_list=[]
                    place=0
                    sums=0
                    while n4!=0:
                             r=n4%10
                             sums=sums+(r*pow(8,place))
                             place+=1
                             n4=n4//10       
                    return sums

def octal_to_hexadecimal(d):
           deci=octal_to_decimal(d)
           sums=decimal_to_hexadecimal(deci)
           return sums

def octal_to_binary(d):
         deci=octal_to_decimal(d)
         sums=decimal_to_binary(deci)
         return sums

def hexadecimal_to_decimal(d):
    u=d
    char_list=[str(i) for i in u]      
    char_list.reverse()
    places=0
    sums=0
    for i in char_list:
        
        if i=='A':
               y=10
               sums=sums+(y*pow(16,places))
        elif i=='B':
               y=11
               sums=sums+(y*pow(16,places))
        elif i=='C':
               y=12
               sums=sums+(y*pow(16,places))       
        elif i=='D':
               y=13
               sums=sums+(y*pow(16,places))
        elif i=='E':
               y=14
               sums=sums+(y*pow(16,places))
        elif i=='F':
               y=15
               sums=sums+(y*pow(16,places))
        else:
            y=int(i)
            sums=sums+(y*pow(16,places))
        places+=1
    
    return sums

def hexadecimal_to_octal(d):
        deci=hexadecimal_to_decimal(d)
        sums=decimal_to_octal(deci)
        return sums

def hexadecimal_to_binary(d):
            deci=hexadecimal_to_decimal(d)
            sums=decimal_to_binary(deci)
            return sums
 
        
st.title('Code Converter')
st.markdown('_Hello! Welcome to our code conversion tool, designed to assist you in effortlessly transforming numbers between various systems. We hope you find it useful and efficient in saving you time. Thank you for choosing our application!_')

h=st.selectbox('From',['decimal','octal','hexadecimal','binary'])
h2=st.selectbox('To',['decimal','octal','hexadecimal','binary'])

if (h=='decimal' and h2=='binary'):
      ft=st.number_input('Enter a decimal value',step=1)
      submit=st.button('Convert')
      try:
          
          ans= decimal_to_binary(ft)
          
          if submit:
                  st.success('The binary equivalent is {}'.format(str(ans)))
      except ValueError:
          if submit:
                  st.warning("Give a valid decimal value")  
                  
if (h=='decimal' and h2=='octal'):
      ft=st.number_input('Enter a decimal value',step=1)
      submit=st.button('Convert')
      try: 
          ans= decimal_to_octal(ft) 
          if submit:
                  st.success('The octal equivalent is {}'.format(str(ans)))
      except ValueError:
          if submit:
                  st.warning("Give a valid decimal value")  

if (h=='decimal' and h2=='hexadecimal'):
      ft=st.number_input('Enter a decimal value',step=1)
      submit=st.button('Convert')
      try: 
          ans= decimal_to_hexadecimal(ft) 
          if submit:
                  st.success('The Hexadecimal equivalent is {}'.format(str(ans)))
      except ValueError:
          if submit:
                  st.warning("Give a valid decimal value")  

if (h=='octal' and h2=='decimal'):
      ft=st.number_input('Enter an octal value',step=1)
      submit=st.button('Convert')
      try: 
          ans= octal_to_decimal(ft) 
          if submit:
                  st.success('The Decimal equivalent is {}'.format(str(ans)))
      except ValueError:
          if submit:
                  st.warning("Give a valid octal value")  
                  
if (h=='hexadecimal' and h2=='decimal'):
      ft=st.text_input('Enter a Hexadecimal value')
      submit=st.button('Convert')
      try: 
          ans= hexadecimal_to_decimal(ft) 
          if submit:
                  st.success('The Decimal equivalent is {}'.format(str(ans)))
      except ValueError:
          if submit:
                  st.warning("Give a valid hexadecimal value") 

if (h=='decimal' and h2=='decimal'):
             st.success("Both are of same type --> {}. Please Choose different types. So that we can proceed further!!".format(h2))

if (h=='octal' and h2=='octal'):
             st.success("Both are of same type --> {}. Please Choose different types. So that we can proceed further!!".format(h2))

if (h=='hexadecimal' and h2=='hexadecimal'):
             st.success("Both are of same type --> {}. Please Choose different types. So that we can proceed further!!".format(h2))
             
if (h=='binary' and h2=='binary'):
             st.success("Both are of same type --> {}. Please Choose different types. So that we can proceed further!!".format(h2))
             
if (h=='binary' and h2=='decimal'):
        ft=st.number_input("Enter a binary value",step=1)
        submit=st.button('Convert')
        
        try:
                ans=binary_to_decimal(ft)
                if submit:
                        st.success('The decimal equivalent is {}'.format(str(ans)))
        except ValueError:
                 if submit:
                       st.warning('Give a valid binary value')
 
if(h=='octal' and h2=='hexadecimal'):
          ft=st.number_input('Enter an octal value',step=1)
          submit=st.button('Convert')
          
          try:
                 ans=octal_to_hexadecimal(ft)
                 if submit:
                       st.success('The Hexadecimal equivalent is {}'.format(str(ans)))
                       
          except ValueError:
                  if submit:
                         st.warning('Give a valid octal value')

if(h=='octal' and h2=='binary'):
          ft=st.number_input('Enter an octal value',step=1)
          submit=st.button('Convert')
          
          try:
                 ans=octal_to_binary(ft)
                 if submit:
                       st.success('The binary equivalent is {}'.format(str(ans)))
                       
          except ValueError:
                  if submit:
                         st.warning('Give a valid octal value')
                         
if(h=='hexadecimal' and h2=='octal'):
          ft=st.text_input('Enter a Hexadecimal value')
          submit=st.button('Convert')
          
          try:
                 ans=hexadecimal_to_octal(ft)
                 if submit:
                       st.success('The octal equivalent is {}'.format(str(ans)))
                       
          except ValueError:
                  if submit:
                         st.warning('Give a valid hexadecimal value')

if(h=='hexadecimal' and h2=='binary'):
          ft=st.text_input('Enter a Hexadecimal value')
          submit=st.button('Convert')
          
          try:
                 ans=hexadecimal_to_binary(ft)
                 if submit:
                       st.success('The binary equivalent is {}'.format(str(ans)))
                       
          except ValueError:
                  if submit:
                         st.warning('Give a valid hexadecimal value')
                         
if(h=='binary' and h2=='octal'):
          ft=st.number_input('Enter a binary value',step=1)
          submit=st.button('Convert')
          
          try:
                 ans=binary_to_octal(ft)
                 if submit:
                       st.success('The octal equivalent is {}'.format(str(ans)))
                       
          except ValueError:
                  if submit:
                         st.warning('Give a valid binary value')
                         
if(h=='binary' and h2=='hexadecimal'):
          ft=st.number_input('Enter a binary value',step=1)
          submit=st.button('Convert')
          
          try:
                 ans=binary_to_hexadecimal(ft)
                 if submit:
                       st.success('The hexadecimal equivalent is {}'.format(str(ans)))
                       
          except ValueError:
                  if submit:
                         st.warning('Give a valid binary value')