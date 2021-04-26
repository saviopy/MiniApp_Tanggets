import streamlit as st


st.title('Tanggets')

st.markdown('**Escolha se deseja calcular a quandidade de nuggets ou hambúrguer feitos com filé ou CMS (Carne Mecanicamente Separada) de pescado.**' )

ingredientes = [0.03, 0.035, 0.07, 0.012, 0.005, 0.002, 0.002, 0.002, 0.002, 0.002, 0.82]

a_milho = ingredientes[0]
pt_soja = ingredientes[1]
agua_g = ingredientes[2]
g_vegetal = ingredientes[3]
g_monossodico = ingredientes[4]
sal = ingredientes[5]
cebola = ingredientes[6]
alho = ingredientes[7]
cebolinha = ingredientes[8]
salsinha = ingredientes[9]
proteina = ingredientes[10]
radio = st.radio('Qual Proteina ?', ['Filé', 'Cms'])

if radio == 'Filé'  :
    file_kg = st.number_input('Quantidade de filé em kg')
    quantidade = file_kg * 1000
    escolha = st.radio('Qual Produto ?', ['Nugget', 'Hamburguer'])
    if escolha == 'Nugget':
        st.image('nuggetspeixe.jpg')
        if quantidade > 0 :
            quantidade_nuggte = quantidade / 41
            st.markdown('Número de Nuggets ')
            st.markdown(str(int(quantidade_nuggte)))
            st.markdown('**Lista dos ingredientes em gramas **')
            a_milho = quantidade * a_milho
            a_milho = round(a_milho, 1)
            st.markdown('Amido de milho ')
            st.markdown(str(a_milho))
            pt_soja = quantidade * pt_soja
            pt_soja = round(pt_soja, 1)
            st.markdown('Proteína Texeturizada')
            st.markdown(str(pt_soja))  
            agua_g = quantidade * agua_g
            agua_g = round(agua_g, 1)
            st.markdown('Água gelada')
            st.markdown(str(agua_g)) 
            g_vegetal = quantidade * g_vegetal
            g_vegetal = round(g_vegetal, 1)    
            st.markdown('Gordura vegetal')
            st.markdown(str(g_vegetal))  
            g_monossodico = quantidade * g_monossodico
            g_monossodico = round(g_monossodico, 1)
            st.markdown('Glutamato ')
            st.markdown(str(g_monossodico))
            sal = quantidade * sal
            sal = round(sal, 1)
            st.markdown('Sal')
            st.markdown(str(sal)) 
            cebola = quantidade * cebola
            cebola = round(cebola, 1)
            st.markdown('Cebola')
            st.markdown(str(cebola)) 
            alho = quantidade * alho
            alho = round(alho, 1)
            st.markdown('Alho')
            st.markdown(str(alho)) 
            cebolinha = quantidade * cebolinha
            cebolinha = round(cebolinha, 1)
            st.markdown('Cebolinha')
            st.write(str(cebolinha))
            salsinha = quantidade * salsinha
            salsinha = round(salsinha,1)
            st.markdown('Salsinha')
            st.markdown(str(salsinha))

    if escolha == 'Hamburguer':
        st.image('hamburguerpeixe.jpg')
        if quantidade > 0 :
            quantidade_blend = quantidade / 165
            st.markdown('Número de Hamburguers')
            st.markdown(str(int(quantidade_blend)))
            st.markdown('**Lista dos ingredientes em gramas **')
            a_milho = quantidade * a_milho
            a_milho = round(a_milho, 1)
            st.markdown('Amido de milho ')
            st.markdown(str(a_milho))
            pt_soja = quantidade * pt_soja
            pt_soja = round(pt_soja, 1)
            st.markdown('Proteína Texeturizada')
            st.markdown(str(pt_soja))  
            agua_g = quantidade * agua_g
            agua_g = round(agua_g, 1)
            st.markdown('Água gelada')
            st.markdown(str(agua_g)) 
            g_vegetal = quantidade * g_vegetal
            g_vegetal = round(g_vegetal, 1)    
            st.markdown('Gordura vegetal')
            st.markdown(str(g_vegetal))  
            g_monossodico = quantidade * g_monossodico
            g_monossodico = round(g_monossodico, 1)
            st.markdown('Glutamato ')
            st.markdown(str(g_monossodico))
            sal = quantidade * sal
            sal = round(sal, 1)
            st.markdown('Sal')
            st.markdown(str(sal)) 
            cebola = quantidade * cebola
            cebola = round(cebola, 1)
            st.markdown('Cebola')
            st.markdown(str(cebola)) 
            alho = quantidade * alho
            alho = round(alho, 1)
            st.markdown('Alho')
            st.markdown(str(alho)) 
            cebolinha = quantidade * cebolinha
            cebolinha = round(cebolinha, 1)
            st.markdown('Cebolinha')
            st.write(str(cebolinha))
            salsinha = quantidade * salsinha
            salsinha = round(salsinha,1)
            st.markdown('Salsinha')
            st.markdown(str(salsinha))


        
if radio == 'Cms'   :
    st.text('Adicione os dados para caulcular o rendimento do CMS')    
    peso_cms = st.number_input('Quantidade de CMS em (kg) ?')
    peso_carcaca = st.number_input('Peso da carcaça em (kg)')
    escolha = st.radio('Qual produto ?', ['Nugget', 'Hamburguer'])
    if escolha == 'Nugget':
        st.image('nuggetspeixe.jpg')
        if peso_carcaca > 0 :
            peso_carcaca = peso_carcaca * 1000
            peso_cms = peso_cms * 1000  
            r_cms = (peso_cms * 100) / peso_carcaca
            st.markdown('Valor aproveitado em %')
            st.markdown(str(int(r_cms)))
            quantidade_nuggte = peso_cms / 41
            st.markdown('Número de Nuggets')
            st.markdown(str(int(quantidade_nuggte)))
            st.markdown('**Lista dos ingredientes em gramas **')
            a_milho = peso_cms * a_milho
            a_milho = round(a_milho, 1)
            st.markdown('Amido de milho ')
            st.markdown(str(a_milho))
            pt_soja = peso_cms * pt_soja
            pt_soja = round(pt_soja, 1)
            st.markdown('Proteína Texeturizada')
            st.markdown(str(pt_soja))  
            agua_g = peso_cms * agua_g
            agua_g = round(agua_g, 1)
            st.markdown('Água gelada')
            st.markdown(str(agua_g)) 
            g_vegetal = peso_cms * g_vegetal
            g_vegetal = round(g_vegetal, 1)    
            st.markdown('Gordura vegetal')
            st.markdown(str(g_vegetal))  
            g_monossodico = peso_cms * g_monossodico
            g_monossodico = round(g_monossodico, 1)
            st.markdown('Glutamato ')
            st.markdown(str(g_monossodico))
            sal = peso_cms * sal
            sal = round(sal, 1)
            st.markdown('Sal')
            st.markdown(str(sal)) 
            cebola = peso_cms * cebola
            cebola = round(cebola, 1)
            st.markdown('Cebola')
            st.markdown(str(cebola)) 
            alho = peso_cms * alho
            alho = round(alho, 1)
            st.markdown('Alho')
            st.markdown(str(alho)) 
            cebolinha = peso_cms * cebolinha
            cebolinha = round(cebolinha, 1)
            st.markdown('Cebolinha')
            st.write(str(cebolinha))
            salsinha = peso_cms * salsinha
            salsinha = round(salsinha,1)
            st.markdown('Salsinha')
            st.markdown(str(salsinha))



             
        
    if escolha == 'Hamburguer':
        st.image('hamburguerpeixe.jpg')
        if peso_carcaca > 0 :
            peso_carcaca = peso_carcaca * 1000
            peso_cms = peso_cms * 1000  
            r_cms = (peso_cms * 100) / peso_carcaca
            st.markdown('Valor aproveitado em %')
            st.markdown(str(int(r_cms)))
            quantidade_nuggte = peso_cms / 165
            st.markdown('Quantidade de Hamburguers ')
            st.markdown(str(int(quantidade_nuggte)))
            st.markdown('**Lista dos ingredientes em gramas **')
            a_milho = peso_cms * a_milho
            a_milho = round(a_milho, 1)
            st.markdown('Amido de milho ')
            st.markdown(str(a_milho))
            pt_soja = peso_cms * pt_soja
            pt_soja = round(pt_soja, 1)
            st.markdown('Proteína Texeturizada')
            st.markdown(str(pt_soja))  
            agua_g = peso_cms * agua_g
            agua_g = round(agua_g, 1)
            st.markdown('Água gelada')
            st.markdown(str(agua_g)) 
            g_vegetal = peso_cms * g_vegetal
            g_vegetal = round(g_vegetal, 1)    
            st.markdown('Gordura vegetal')
            st.markdown(str(g_vegetal))  
            g_monossodico = peso_cms * g_monossodico
            g_monossodico = round(g_monossodico, 1)
            st.markdown('Glutamato ')
            st.markdown(str(g_monossodico))
            sal = peso_cms * sal
            sal = round(sal, 1)
            st.markdown('Sal')
            st.markdown(str(sal)) 
            cebola = peso_cms * cebola
            cebola = round(cebola, 1)
            st.markdown('Cebola')
            st.markdown(str(cebola)) 
            alho = peso_cms * alho
            alho = round(alho, 1)
            st.markdown('Alho')
            st.markdown(str(alho)) 
            cebolinha = peso_cms * cebolinha
            cebolinha = round(cebolinha, 1)
            st.markdown('Cebolinha')
            st.write(str(cebolinha))
            salsinha = peso_cms * salsinha
            salsinha = round(salsinha,1)
            st.markdown('Salsinha')
            st.markdown(str(salsinha))


             
    
        
    


    