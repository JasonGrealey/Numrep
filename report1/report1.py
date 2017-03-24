from scipy import misc
import matplotlib.pyplot as plt
import numpy as np 
import math

def main():
    #         Get the filename as string
    f1 = "desync1.pgm"
    #         Read file it np array
    img = misc.imread(f1)
    imgtest=misc.imread(f1)
    #storing old version
    imgold = misc.imread(f1)
    length1=len(img)
    print(len(img))
    #print(img[0][0])
    #print(img)



#=================================================================================
    #         Get the filename as string
    f2 = "desync2.pgm"
    #         Read file it np array
    img2 = misc.imread(f2)
    #storing old version
    img2old = misc.imread(f2)
    print(len(img2))
    length2=len(img2)
    #print(img[0][0])
    #print(img)


#=================================================================================
    #         Get the filename as string
    f3 = "desync3.pgm"
    #         Read file it np array
    img3 = misc.imread(f3)
    #storing old version
    img3old = misc.imread(f3)
    print(len(img3))
    length3=len(img3)
    #print(img[0][0])
    #print(img)

#=================================================================================
    #         Get the filename as string
    f4 = "desync4.pgm"
    #         Read file it np array
    img4 = misc.imread(f4)
    #storing old version
    img4old = misc.imread(f4)
    print(len(img4))
    length4=len(img4)
    #print(img[0][0])
    #print(img)

    #phase correlation function taking two rows from image file
    #returns the position of the peak of the correlation
    def corr(row1,row2):#calculates the shift of two rows using fft and takes the peak of the distribution(np.argmax) to give the shift 
        ft = np.fft.fft(row1)
        fshift= np.fft.fftshift(ft)
        fcom= np.conj(fshift)
        ft2 = np.fft.fft(row2)
        fshift2= np.fft.fftshift(ft2)
        mult = np.multiply(fcom,fshift2)
        imult= np.fft.ifft(mult)
        return(np.argmax(imult))

    def shift(row1,row2,length,tolerance):#tolerance is the fraction of the diagram a shift has to be smaller than to be implemented
        value=corr(row1,row2)#shifting back
        if abs(value-length)<length*tolerance:#no shift is larger than around a fifth of the diagram
            row2=np.roll(row2,-value)
            return row2
        else:
            return row2
            
        
    #storing non-shifted vals
    shiftvals1=[]
    shiftvals2=[]
    shiftvals3=[]
    shiftvals4=[]
    shiftvals1.append(0)#assuming first line is not shifted as stated in report
    shiftvals2.append(0)
    shiftvals3.append(0)
    shiftvals4.append(0)
    for i in range(len(img)-1):
        shiftvals1.append(corr(img[i],img[i+1]))
    #print(shiftvals1)
    
    
    for i in range(len(img2)-1):
        shiftvals2.append(corr(img2[i],img2[i+1]))
    #print(shiftvals2)
    
    
    for i in range(len(img3)-1):
        shiftvals3.append(corr(img3[i],img3[i+1]))
    #print(shiftvals3)
    
    
    for i in range(len(img4)-1):
        shiftvals4.append(corr(img4[i],img4[i+1]))
    #print(shiftvals4)
    
    #shifting row by row
    for i in range(length1-1):
        img[i+1]=shift(img[i],img[i+1],length1,0.25)
    for i in range(length2-1):
        img2[i+1]=shift(img2[i],img2[i+1],length2,1)
    for i in range(length3-1):
        img3[i+1]=shift(img3[i],img3[i+1],length3,1)
    for i in range(length4-1):
        img4[i+1]=shift(img4[i],img4[i+1],length4,1)
        
    #here I have to do more stuff on the castle image
    #I compare it to the original image (ignoring error rows) to replace it in it's original position
    newshiftvals1=[]
    #now comparing with original image for the Castle
    for i in range(length1-1):
        valnew=corr(img[i],imgold[i])
        if shiftvals1[i]==0:
            #here original image line was not shifted
            newshiftvals1.append(valnew)
            img[i]=np.roll(img[i],valnew)#shifting new line back to orignal space
        else:#here orignial line image was shifted
            #therefore i shift it by the same amount as I shifted the most recent non-shifted line in the original image
            img[i]=np.roll(img[i],newshiftvals1[-1])
        #print(newshiftvals1)


    plt.imshow(img, cmap = 'gray')
    plt.title('Castle After'), plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imshow(imgold, cmap = 'gray')
    plt.title('Castle Before'), plt.xticks([]), plt.yticks([])
    plt.show()
    
    plt.imshow(img2, cmap = 'gray')
    plt.title('Tractor After'), plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imshow(img2old, cmap = 'gray')
    plt.title('Tractor Before'), plt.xticks([]), plt.yticks([])
    plt.show()

    plt.imshow(img3, cmap = 'gray')
    plt.title('Airfield After'), plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imshow(img3old, cmap = 'gray')
    plt.title('Airfield Before'), plt.xticks([]), plt.yticks([])
    plt.show() 

    plt.imshow(img4, cmap = 'gray')
    plt.title('City After'), plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imshow(img4old, cmap = 'gray')
    plt.title('City Before'), plt.xticks([]), plt.yticks([])
    plt.show()
    


    


main()
